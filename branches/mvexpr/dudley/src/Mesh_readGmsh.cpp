
/*****************************************************************************
*
* Copyright (c) 2003-2013 by University of Queensland
* http://www.uq.edu.au
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
* Development until 2012 by Earth Systems Science Computational Center (ESSCC)
* Development since 2012 by School of Earth Sciences
*
*****************************************************************************/

/************************************************************************************/

/*   Dudley: read mesh */

/************************************************************************************/

#include "Mesh.h"
#include <stdio.h>

#define FSCANF_CHECK(scan_ret, reason) { if (scan_ret == EOF) { perror(reason); Dudley_setError(IO_ERROR,"scan error while reading dudley file"); return NULL;} }

/************************************************************************************/

/*  reads a mesh from a Dudley file of name fname */

#define MAX_numNodes_gmsh 20

Dudley_Mesh *Dudley_Mesh_readGmsh(char *fname, index_t numDim, index_t order, index_t reduced_order, bool_t optimize,
				  bool_t useMacroElements)
{

    double version = 1.0;
    int format = 0, size = sizeof(double), scan_ret;
    dim_t numNodes, totalNumElements = 0, numTags = 0, numNodesPerElement = 0, numNodesPerElement2, element_dim = 0;
    index_t e, i0, j, gmsh_type, partition_id, itmp, elementary_id;
    index_t numElements = 0, numFaceElements = 0, *id = NULL, *tag = NULL, *vertices = NULL;
    Dudley_Mesh *mesh_p = NULL;
    char line[LenString_MAX + 1];
    char error_msg[LenErrorMsg_MAX];
    double rtmp0, rtmp1;
#ifdef Dudley_TRACE
    double time0 = Dudley_timer();
#endif
    FILE *fileHandle_p = NULL;
    Dudley_ElementTypeId *element_type = NULL;

    Esys_MPIInfo *mpi_info = Esys_MPIInfo_alloc(MPI_COMM_WORLD);
    Dudley_resetError();
    if (mpi_info->size > 1)
    {
	Dudley_setError(IO_ERROR, "reading GMSH with MPI is not supported yet.");
	Esys_MPIInfo_free(mpi_info);
	return NULL;
    }
    else
    {

	/* allocate mesh */

	mesh_p = Dudley_Mesh_alloc(fname, numDim, mpi_info);
	if (!Dudley_noError())
	    return NULL;

	/* get file handle */
	fileHandle_p = fopen(fname, "r");
	if (fileHandle_p == NULL)
	{
	    sprintf(error_msg, "Opening Gmsh file %s for reading failed.", fname);
	    Dudley_setError(IO_ERROR, error_msg);
	    Esys_MPIInfo_free(mpi_info);
	    return NULL;
	}

	/* start reading */
	while (1)
	{
	    if (!Dudley_noError())
		break;
	    /* find line staring with $ */
	    do
	    {
		if (!fgets(line, sizeof(line), fileHandle_p))
		    break;
		if (feof(fileHandle_p))
		    break;
	    }
	    while (line[0] != '$');

	    if (feof(fileHandle_p))
		break;

	    /* format */
	    if (!strncmp(&line[1], "MeshFormat", 10))
	    {
		scan_ret = fscanf(fileHandle_p, "%lf %d %d\n", &version, &format, &size);
		FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
	    }
	    /* nodes are read */
	    if (!strncmp(&line[1], "NOD", 3) || !strncmp(&line[1], "NOE", 3) || !strncmp(&line[1], "Nodes", 5))
	    {

		scan_ret = fscanf(fileHandle_p, "%d", &numNodes);
		FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
		if (!Dudley_noError())
		    break;
		Dudley_NodeFile_allocTable(mesh_p->Nodes, numNodes);
		if (!Dudley_noError())
		    break;
		for (i0 = 0; i0 < numNodes; i0++)
		{
		    if (1 == numDim)
		    {
			scan_ret = fscanf(fileHandle_p, "%d %le %le %le\n", &mesh_p->Nodes->Id[i0],
					  &mesh_p->Nodes->Coordinates[INDEX2(0, i0, numDim)], &rtmp0, &rtmp1);
			FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
		    }
		    else if (2 == numDim)
		    {
			scan_ret = fscanf(fileHandle_p, "%d %le %le %le\n", &mesh_p->Nodes->Id[i0],
					  &mesh_p->Nodes->Coordinates[INDEX2(0, i0, numDim)],
					  &mesh_p->Nodes->Coordinates[INDEX2(1, i0, numDim)], &rtmp0);
			FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
		    }
		    else if (3 == numDim)
		    {
			scan_ret = fscanf(fileHandle_p, "%d %le %le %le\n", &mesh_p->Nodes->Id[i0],
					  &mesh_p->Nodes->Coordinates[INDEX2(0, i0, numDim)],
					  &mesh_p->Nodes->Coordinates[INDEX2(1, i0, numDim)],
					  &mesh_p->Nodes->Coordinates[INDEX2(2, i0, numDim)]);
			FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
		    }
		    mesh_p->Nodes->globalDegreesOfFreedom[i0] = mesh_p->Nodes->Id[i0];
		    mesh_p->Nodes->Tag[i0] = 0;
		}
	    }
	    /* elements */
	    else if (!strncmp(&line[1], "ELM", 3) || !strncmp(&line[1], "Elements", 8))
	    {

		Dudley_ElementTypeId final_element_type = Dudley_NoRef;
		Dudley_ElementTypeId final_face_element_type = Dudley_NoRef;
		numElements = 0;
		numFaceElements = 0;
		scan_ret = fscanf(fileHandle_p, "%d", &totalNumElements);
		FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");

		id = new  index_t[totalNumElements];
		tag = new  index_t[totalNumElements];

		element_type = new  Dudley_ElementTypeId[totalNumElements];
		vertices = new  index_t[totalNumElements * MAX_numNodes_gmsh];
		if (!
		    (Dudley_checkPtr(id) || Dudley_checkPtr(tag) || Dudley_checkPtr(element_type)
		     || Dudley_checkPtr(vertices)))
		{
		    /* read all in */
		    for (e = 0; e < totalNumElements; e++)
		    {
			scan_ret = fscanf(fileHandle_p, "%d %d", &id[e], &gmsh_type);
			FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
			switch (gmsh_type)
			{
			case 1:	/* line order 1 */
			    element_type[e] = Dudley_Line2;
			    element_dim = 1;
			    numNodesPerElement = 2;
			    break;
			case 2:	/* triangle order 1 */
			    element_type[e] = Dudley_Tri3;
			    numNodesPerElement = 3;
			    element_dim = 2;
			    break;
			case 4:	/* tetrahedron order 1 */
			    element_type[e] = Dudley_Tet4;
			    numNodesPerElement = 4;
			    element_dim = 3;
			    break;
			case 15:	/* point */
			    element_type[e] = Dudley_Point1;
			    numNodesPerElement = 1;
			    element_dim = 0;
			    break;
			default:
			    element_type[e] = Dudley_NoRef;
			    sprintf(error_msg, "Unexpected gmsh element type %d in mesh file %s.", gmsh_type, fname);
			    Dudley_setError(IO_ERROR, error_msg);
			}
			if (element_dim == numDim)
			{
			    if (final_element_type == Dudley_NoRef)
			    {
				final_element_type = element_type[e];
			    }
			    else if (final_element_type != element_type[e])
			    {
				sprintf(error_msg, "Dudley can handle a single type of internal elements only.");
				Dudley_setError(IO_ERROR, error_msg);
				break;
			    }
			    numElements++;
			}
			else if (element_dim == numDim - 1)
			{
			    if (final_face_element_type == Dudley_NoRef)
			    {
				final_face_element_type = element_type[e];
			    }
			    else if (final_face_element_type != element_type[e])
			    {
				sprintf(error_msg, "Dudley can handle a single type of face elements only.");
				Dudley_setError(IO_ERROR, error_msg);
				break;
			    }
			    numFaceElements++;
			}

			if (version <= 1.0)
			{
			    scan_ret = fscanf(fileHandle_p, "%d %d %d", &tag[e], &elementary_id, &numNodesPerElement2);
			    FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
			    partition_id = 1;
			    if (numNodesPerElement2 != numNodesPerElement)
			    {
				sprintf(error_msg, "Illegal number of nodes for element %d in mesh file %s.", id[e],
					fname);
				Dudley_setError(IO_ERROR, error_msg);
			    }
			}
			else
			{
			    scan_ret = fscanf(fileHandle_p, "%d", &numTags);
			    FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
			    elementary_id = tag[e] = partition_id = 1;
			    numNodesPerElement2 = -1;
			    for (j = 0; j < numTags; j++)
			    {
				scan_ret = fscanf(fileHandle_p, "%d", &itmp);
				FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
				if (j == 0)
				{
				    tag[e] = itmp;
				}
				else if (j == 1)
				{
				    elementary_id = itmp;
				}
				else if (j == 2)
				{
				    partition_id = itmp;
				}
				/* ignore any other tags */
			    }
			}
			if (!Dudley_noError())
			    break;
			for (j = 0; j < numNodesPerElement; j++)
			{
			    scan_ret = fscanf(fileHandle_p, "%d", &vertices[INDEX2(j, e, MAX_numNodes_gmsh)]);
			    FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
			}
		    }
		    /* all elements have been read, now we have to identify the elements for dudley */

		    if (Dudley_noError())
		    {
			/* first we have to identify the elements to define Elements and FaceElements */
			if (final_element_type == Dudley_NoRef)
			{
			    if (numDim == 1)
			    {
				final_element_type = Dudley_Line2;
			    }
			    else if (numDim == 2)
			    {
				final_element_type = Dudley_Tri3;
			    }
			    else if (numDim == 3)
			    {
				final_element_type = Dudley_Tet4;
			    }
			}
			if (final_face_element_type == Dudley_NoRef)
			{
			    if (numDim == 1)
			    {
				final_face_element_type = Dudley_Point1;
			    }
			    else if (numDim == 2)
			    {
				final_face_element_type = Dudley_Line2;
			    }
			    else if (numDim == 3)
			    {
				final_face_element_type = Dudley_Tri3;
			    }
			}
			mesh_p->Elements = Dudley_ElementFile_alloc(final_element_type, mpi_info);
			mesh_p->FaceElements = Dudley_ElementFile_alloc(final_face_element_type, mpi_info);
			mesh_p->Points = Dudley_ElementFile_alloc(Dudley_Point1, mpi_info);
			if (Dudley_noError())
			{
			    Dudley_ElementFile_allocTable(mesh_p->Elements, numElements);
			    Dudley_ElementFile_allocTable(mesh_p->FaceElements, numFaceElements);
			    Dudley_ElementFile_allocTable(mesh_p->Points, 0);
			    if (Dudley_noError())
			    {
				mesh_p->Elements->minColor = 0;
				mesh_p->Elements->maxColor = numElements - 1;
				mesh_p->FaceElements->minColor = 0;
				mesh_p->FaceElements->maxColor = numFaceElements - 1;
				mesh_p->Points->minColor = 0;
				mesh_p->Points->maxColor = 0;
				numElements = 0;
				numFaceElements = 0;
				for (e = 0; e < totalNumElements; e++)
				{
				    if (element_type[e] == final_element_type)
				    {
					mesh_p->Elements->Id[numElements] = id[e];
					mesh_p->Elements->Tag[numElements] = tag[e];
					mesh_p->Elements->Color[numElements] = numElements;
					mesh_p->Elements->Owner[numElements] = 0;
					for (j = 0; j < mesh_p->Elements-> /*referenceElementSet-> */ numNodes; ++j)
					{
					    mesh_p->Elements->Nodes[INDEX2
								    (j, numElements,
								     mesh_p->
								     Elements-> /*referenceElementSet-> */ numNodes)] =
						vertices[INDEX2(j, e, MAX_numNodes_gmsh)];
					}
					numElements++;
				    }
				    else if (element_type[e] == final_face_element_type)
				    {
					mesh_p->FaceElements->Id[numFaceElements] = id[e];
					mesh_p->FaceElements->Tag[numFaceElements] = tag[e];
					mesh_p->FaceElements->Color[numFaceElements] = numFaceElements;
					mesh_p->FaceElements->Owner[numFaceElements] = 0;
					for (j = 0; j < mesh_p->FaceElements-> /*referenceElementSet-> */ numNodes; ++j)
					{
					    mesh_p->FaceElements->Nodes[INDEX2
									(j, numFaceElements,
									 mesh_p->
									 FaceElements-> /*referenceElementSet-> */
									 numNodes)] =
						vertices[INDEX2(j, e, MAX_numNodes_gmsh)];
					}
					numFaceElements++;
				    }
				}
			    }
			}
		    }
		}
		/* and clean up */
		delete[] id;
		delete[] tag;
		delete[] element_type;
		delete[] vertices;
	    }      
	    /* name tags (thanks to Antoine Lefebvre, antoine.lefebvre2@mail.mcgill.ca ) */
	    else if (!strncmp(&line[1], "PhysicalNames", 13)) {
	        char name[LenString_MAX+1];
	        index_t tag_key;
		scan_ret = fscanf(fileHandle_p, "%d", &numTags);
		FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
		if (! Dudley_noError()) break;
		for (i0 = 0; i0 < numTags; i0++) {
		    scan_ret = fscanf(fileHandle_p, "%d %d %s\n", &itmp, &tag_key, name);
		    FSCANF_CHECK(scan_ret, "fscanf: Dudley_Mesh_readGmsh");
		    if (! (itmp == 2)) Dudley_setError(IO_ERROR,"Dudley_Mesh_readGmsh: expecting two entries per physical name.");
		    if ( strlen(name) < 3 ) Dudley_setError(IO_ERROR,"Dudley_Mesh_readGmsh: illegal tagname (\" missing?)");
		    if (! Dudley_noError()) break;
		    name[strlen(name)-1]='\0';
		    Dudley_Mesh_addTagMap(mesh_p,&name[1],tag_key);
		}
	      }
	    /* search for end of data block */
	    do
	    {
		if (!fgets(line, sizeof(line), fileHandle_p))
		{
		    sprintf(error_msg, "Unexpected end of file in %s", fname);
		    Dudley_setError(IO_ERROR, error_msg);
		}
		if (feof(fileHandle_p))
		{
		    sprintf(error_msg, "Unexpected end of file in %s", fname);
		    Dudley_setError(IO_ERROR, error_msg);
		}
		if (!Dudley_noError())
		    break;
	    }
	    while (line[0] != '$');
	}

	/* close file */
	fclose(fileHandle_p);
	/* clean up */
	if (!Dudley_noError())
	{
	    Dudley_Mesh_free(mesh_p);
	    return NULL;
	}
	/*   resolve id's : */
	if (Dudley_noError())
	    Dudley_Mesh_resolveNodeIds(mesh_p);
	/* rearrange elements: */
	if (Dudley_noError())
	    Dudley_Mesh_prepare(mesh_p, optimize);
	/* free up memory */
	Esys_MPIInfo_free(mpi_info);
	if (!Dudley_noError())
	{
	    Dudley_Mesh_free(mesh_p);
	    return NULL;
	}
	else
	{
	    return mesh_p;
	}
    }
}
