
/* $Id$ */

/*******************************************************
 *
 *           Copyright 2003-2007 by ACceSS MNRF
 *       Copyright 2007 by University of Queensland
 *
 *                http://esscc.uq.edu.au
 *        Primary Business: Queensland, Australia
 *  Licensed under the Open Software License version 3.0
 *     http://www.opensource.org/licenses/osl-3.0.php
 *
 *******************************************************/

/**************************************************************/

/*   Finley: read mesh */

/**************************************************************/

#include "Mesh.h"

/**************************************************************/

/*  reads a mesh from a Finley file of name fname */

Finley_Mesh* Finley_Mesh_read(char* fname,index_t order, index_t reduced_order,  bool_t optimize) 

{

  Paso_MPIInfo *mpi_info = Paso_MPIInfo_alloc( MPI_COMM_WORLD );
  dim_t numNodes, numDim, numEle, i0, i1;
  index_t tag_key;
  Finley_Mesh *mesh_p=NULL;
  char name[LenString_MAX],element_type[LenString_MAX],frm[20];
  char error_msg[LenErrorMsg_MAX];
  double time0=Finley_timer();
  FILE *fileHandle_p = NULL;
  ElementTypeId typeID, faceTypeID, contactTypeID, pointTypeID;
  
  Finley_resetError();

  if (mpi_info->size > 1) { 
     Finley_setError(SYSTEM_ERROR,"Finley_Mesh_read: MPI is not suporrted yet.");
  } else {
     /* get file handle */
     fileHandle_p = fopen(fname, "r");
     if (fileHandle_p==NULL) {
       sprintf(error_msg,"Finley_Mesh_read: Opening file %s for reading failed.",fname);
       Finley_setError(IO_ERROR,error_msg);
       Paso_MPIInfo_free( mpi_info );
       return NULL;
     }
   
     /* read header */
     sprintf(frm,"%%%d[^\n]",LenString_MAX-1);
     fscanf(fileHandle_p, frm, name);
   
     /* get the nodes */
   
     fscanf(fileHandle_p, "%1d%*s %d\n", &numDim,&numNodes);
     /* allocate mesh */
     mesh_p = Finley_Mesh_alloc(name,numDim,order,reduced_order,mpi_info);
     if (Finley_noError()) {
   
        /* read nodes */
        Finley_NodeFile_allocTable(mesh_p->Nodes, numNodes);
        if (Finley_noError()) {
           if (1 == numDim) {
               for (i0 = 0; i0 < numNodes; i0++)
   	            fscanf(fileHandle_p, "%d %d %d %le\n", &mesh_p->Nodes->Id[i0],
   	                   &mesh_p->Nodes->globalDegreesOfFreedom[i0], &mesh_p->Nodes->Tag[i0],
   	                   &mesh_p->Nodes->Coordinates[INDEX2(0,i0,numDim)]);
           } else if (2 == numDim) {
                    for (i0 = 0; i0 < numNodes; i0++)
   	                      fscanf(fileHandle_p, "%d %d %d %le %le\n", &mesh_p->Nodes->Id[i0],
   	                             &mesh_p->Nodes->globalDegreesOfFreedom[i0], &mesh_p->Nodes->Tag[i0],
   	                             &mesh_p->Nodes->Coordinates[INDEX2(0,i0,numDim)],
   	                             &mesh_p->Nodes->Coordinates[INDEX2(1,i0,numDim)]);
           } else if (3 == numDim) {
                    for (i0 = 0; i0 < numNodes; i0++)
   	                      fscanf(fileHandle_p, "%d %d %d %le %le %le\n", &mesh_p->Nodes->Id[i0],
   	                             &mesh_p->Nodes->globalDegreesOfFreedom[i0], &mesh_p->Nodes->Tag[i0],
   	                             &mesh_p->Nodes->Coordinates[INDEX2(0,i0,numDim)],
   	                             &mesh_p->Nodes->Coordinates[INDEX2(1,i0,numDim)],
   	                             &mesh_p->Nodes->Coordinates[INDEX2(2,i0,numDim)]);
           } /* if else else */
        }
        /* read elements */
        if (Finley_noError()) {
   
           fscanf(fileHandle_p, "%s %d\n", element_type, &numEle);
           typeID=Finley_RefElement_getTypeId(element_type);
           if (typeID==NoType) {
             sprintf(error_msg,"Finley_Mesh_read :Unidentified element type %s",element_type);
             Finley_setError(VALUE_ERROR,error_msg);
           } else {
             /* read the elements */
             mesh_p->Elements=Finley_ElementFile_alloc(typeID,mesh_p->order, mesh_p->reduced_order, mpi_info);
             if (Finley_noError()) {
                 Finley_ElementFile_allocTable(mesh_p->Elements, numEle);
                 mesh_p->Elements->minColor=0;
                 mesh_p->Elements->maxColor=numEle-1;
                 if (Finley_noError()) {
                    for (i0 = 0; i0 < numEle; i0++) {
                      fscanf(fileHandle_p, "%d %d", &mesh_p->Elements->Id[i0], &mesh_p->Elements->Tag[i0]);
                      mesh_p->Elements->Color[i0]=i0;
                      for (i1 = 0; i1 < mesh_p->Elements->ReferenceElement->Type->numNodes; i1++) {
                           fscanf(fileHandle_p, " %d",
                              &mesh_p->Elements->Nodes[INDEX2(i1, i0, mesh_p->Elements->ReferenceElement->Type->numNodes)]);
                      }	/* for i1 */
                      fscanf(fileHandle_p, "\n");
                    } /* for i0 */
                 }
             }
          }
        }
        /* get the face elements */
        if (Finley_noError()) {
             fscanf(fileHandle_p, "%s %d\n", element_type, &numEle);
             faceTypeID=Finley_RefElement_getTypeId(element_type);
             if (faceTypeID==NoType) {
               sprintf(error_msg,"Finley_Mesh_read :Unidentified element type %s for face elements",element_type);
               Finley_setError(VALUE_ERROR,error_msg);
             } else {
                mesh_p->FaceElements=Finley_ElementFile_alloc(faceTypeID,mesh_p->order, mesh_p->reduced_order, mpi_info);
                if (Finley_noError()) {
                   Finley_ElementFile_allocTable(mesh_p->FaceElements, numEle);
                   if (Finley_noError()) {
                      mesh_p->FaceElements->minColor=0;
                      mesh_p->FaceElements->maxColor=numEle-1;
                      for (i0 = 0; i0 < numEle; i0++) {
                        fscanf(fileHandle_p, "%d %d", &mesh_p->FaceElements->Id[i0], &mesh_p->FaceElements->Tag[i0]);
                        mesh_p->FaceElements->Color[i0]=i0;
                        for (i1 = 0; i1 < mesh_p->FaceElements->ReferenceElement->Type->numNodes; i1++) {
                             fscanf(fileHandle_p, " %d",
                                &mesh_p->FaceElements->Nodes[INDEX2(i1, i0, mesh_p->FaceElements->ReferenceElement->Type->numNodes)]);
                        }	/* for i1 */
                        fscanf(fileHandle_p, "\n");
                      } /* for i0 */
                   }
                }
             }
        }
        /* get the Contact face element */
        if (Finley_noError()) {
             fscanf(fileHandle_p, "%s %d\n", element_type, &numEle);
             contactTypeID=Finley_RefElement_getTypeId(element_type);
             if (contactTypeID==NoType) {
               sprintf(error_msg,"Finley_Mesh_read: Unidentified element type %s for contact elements",element_type);
               Finley_setError(VALUE_ERROR,error_msg);
             } else {
               mesh_p->ContactElements=Finley_ElementFile_alloc(contactTypeID,mesh_p->order, mesh_p->reduced_order, mpi_info);
               if (Finley_noError()) {
                   Finley_ElementFile_allocTable(mesh_p->ContactElements, numEle);
                   if (Finley_noError()) {
                      mesh_p->ContactElements->minColor=0;
                      mesh_p->ContactElements->maxColor=numEle-1;
                      for (i0 = 0; i0 < numEle; i0++) {
                        fscanf(fileHandle_p, "%d %d", &mesh_p->ContactElements->Id[i0], &mesh_p->ContactElements->Tag[i0]);
                        mesh_p->ContactElements->Color[i0]=i0;
                        for (i1 = 0; i1 < mesh_p->ContactElements->ReferenceElement->Type->numNodes; i1++) {
                            fscanf(fileHandle_p, " %d",
                               &mesh_p->ContactElements->Nodes[INDEX2(i1, i0, mesh_p->ContactElements->ReferenceElement->Type->numNodes)]);
                        }	/* for i1 */
                        fscanf(fileHandle_p, "\n");
                      } /* for i0 */
                  }
               }
             }
        }  
        /* get the nodal element */
        if (Finley_noError()) {
             fscanf(fileHandle_p, "%s %d\n", element_type, &numEle);
             pointTypeID=Finley_RefElement_getTypeId(element_type);
             if (pointTypeID==NoType) {
               sprintf(error_msg,"Finley_Mesh_read: Unidentified element type %s for points",element_type);
               Finley_setError(VALUE_ERROR,error_msg);
             }
             mesh_p->Points=Finley_ElementFile_alloc(pointTypeID,mesh_p->order, mesh_p->reduced_order, mpi_info);
             if (Finley_noError()) {
                Finley_ElementFile_allocTable(mesh_p->Points, numEle);
                if (Finley_noError()) {
                   mesh_p->Points->minColor=0;
                   mesh_p->Points->maxColor=numEle-1;
                   for (i0 = 0; i0 < numEle; i0++) {
                     fscanf(fileHandle_p, "%d %d", &mesh_p->Points->Id[i0], &mesh_p->Points->Tag[i0]);
                     mesh_p->Points->Color[i0]=i0;
                     for (i1 = 0; i1 < mesh_p->Points->ReferenceElement->Type->numNodes; i1++) {
                         fscanf(fileHandle_p, " %d",
                            &mesh_p->Points->Nodes[INDEX2(i1, i0, mesh_p->Points->ReferenceElement->Type->numNodes)]);
                     }	/* for i1 */
                     fscanf(fileHandle_p, "\n");
                   } /* for i0 */
                }
             }
        }
        /* get the name tags */
        if (Finley_noError()) {
           if (feof(fileHandle_p) == 0) {
              fscanf(fileHandle_p, "%s\n", name);
              while (feof(fileHandle_p) == 0) {
                   fscanf(fileHandle_p, "%s %d\n", name, &tag_key);
                   Finley_Mesh_addTagMap(mesh_p,name,tag_key);
              }
           }
        }
     }
     /* close file */
     fclose(fileHandle_p);
   
     /*   resolve id's : */
     /* rearrange elements: */
   
     if (Finley_noError()) Finley_Mesh_resolveNodeIds(mesh_p);
     if (Finley_noError()) Finley_Mesh_prepare(mesh_p, optimize);
   
     /* that's it */
     #ifdef Finley_TRACE
     printf("timing: reading mesh: %.4e sec\n",Finley_timer()-time0);
     #endif
  }

  /* that's it */
  if (! Finley_noError()) {
       Finley_Mesh_free(mesh_p);
  }
  Paso_MPIInfo_free( mpi_info );
  return mesh_p;
}