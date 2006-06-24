/*
 ************************************************************
 *          Copyright 2006 by ACcESS MNRF                   *
 *                                                          *
 *              http://www.access.edu.au                    *
 *       Primary Business: Queensland, Australia            *
 *  Licensed under the Open Software License version 3.0    *
 *     http://www.opensource.org/licenses/osl-3.0.php       *
 *                                                          *
 ************************************************************
*/

/**************************************************************/

/*   Finley: generates rectangular meshes  */

/*   Generates numElements[0] mesh with second order elements (Line3) in the interval */
/*   [0,Length[0]]. order is the desired accuracy of the integration scheme. */

/**************************************************************/

/*  Author: gross@access.edu.au */
/*  Version: $Id$ */

/**************************************************************/

#include "RectangularMesh.h"

/**************************************************************/

Finley_Mesh* Finley_RectangularMesh_Line3(dim_t* numElements,double* Length,bool_t* periodic,index_t order,bool_t useElementsOnFace) {
  dim_t N0,NE0,i0,NDOF0,NFaceElements,NUMNODES;
  index_t k,node0;
  Finley_Mesh* out;
  char name[50];
  double time0=Finley_timer();
  NE0=MAX(1,numElements[0]);
  N0=2*NE0+1;
  if (!periodic[0]) {
      NDOF0=N0;
      NFaceElements=2;
  } else {
      NDOF0=N0-1;
      NFaceElements=0;
  }
  
  /*  allocate mesh: */
  
  sprintf(name,"Rectangular mesh with %d nodes",N0);
  /* TEMPFIX */
#ifndef PASO_MPI
  out=Finley_Mesh_alloc(name,1,order);
  if (! Finley_noError()) return NULL;

  out->Elements=Finley_ElementFile_alloc(Line3,out->order);
  if (useElementsOnFace) {
    out->FaceElements=Finley_ElementFile_alloc(Line3Face,out->order);
    out->ContactElements=Finley_ElementFile_alloc(Line3Face_Contact,out->order);
  } else {
    out->FaceElements=Finley_ElementFile_alloc(Point1,out->order);
    out->ContactElements=Finley_ElementFile_alloc(Point1_Contact,out->order);
  }
  out->Points=Finley_ElementFile_alloc(Point1,out->order);
#else
  /* TODO */
  PASO_MPI_TODO;
  out = NULL;
#endif
  if (! Finley_noError()) {
       Finley_Mesh_dealloc(out);
       return NULL;
  }
  
  /*  allocate tables: */
 #ifndef PASO_MPI
  Finley_NodeFile_allocTable(out->Nodes,N0);
#else
  /* TODO */
#endif
  Finley_ElementFile_allocTable(out->Elements,NE0);
  Finley_ElementFile_allocTable(out->FaceElements,NFaceElements);
  if (! Finley_noError()) {
      Finley_Mesh_dealloc(out);
      return NULL;
  }
  
  /*  set nodes: */
  
  #pragma omp parallel for private(i0,k) 
  for (i0=0;i0<N0;i0++) {
     k=i0;
     out->Nodes->Coordinates[INDEX2(0,k,1)]=DBLE(i0)/DBLE(N0-1)*Length[0];
     out->Nodes->Id[k]=k;
     out->Nodes->Tag[k]=0;
     out->Nodes->degreeOfFreedom[k]=(i0%NDOF0);
  }
  if (!periodic[0]) {
     out->Nodes->Tag[0]=1;
     out->Nodes->Tag[N0-1]=2;
  }
  
  /*   set the elements: */
  
  #pragma omp parallel for private(i0,k,node0) 
  for (i0=0;i0<NE0;i0++) {
    k=i0;
    node0=2*i0;

    out->Elements->Id[k]=k;
    out->Elements->Tag[k]=0;
    out->Elements->Color[k]=COLOR_MOD(i0);

    out->Elements->Nodes[INDEX2(0,k,3)]=node0;
    out->Elements->Nodes[INDEX2(1,k,3)]=node0+2;
    out->Elements->Nodes[INDEX2(2,k,3)]=node0+1;
  }
  out->Elements->minColor=0;
  out->Elements->maxColor=COLOR_MOD(0);
  
  /*   face elements: */
  if (useElementsOnFace) {
     NUMNODES=3;
  } else {
     NUMNODES=1;
  }
  
  if (!periodic[0]) {
     out->FaceElements->Id[0]=NE0;
     out->FaceElements->Tag[0]=1;
     out->FaceElements->Color[0]=0;
     if (useElementsOnFace) {
       out->FaceElements->Nodes[INDEX2(0,0,NUMNODES)]=0;
       out->FaceElements->Nodes[INDEX2(1,0,NUMNODES)]=2;
       out->FaceElements->Nodes[INDEX2(2,0,NUMNODES)]=1;
     } else {
       out->FaceElements->Nodes[INDEX2(0,0,NUMNODES)]=0;
     }

     out->FaceElements->Id[1]=NE0+1;
     out->FaceElements->Tag[1]=2;
     out->FaceElements->Color[1]=1;
     if (useElementsOnFace) {
        out->FaceElements->Nodes[INDEX2(0,1,NUMNODES)]=N0-1;
        out->FaceElements->Nodes[INDEX2(1,1,NUMNODES)]=N0-3;
        out->FaceElements->Nodes[INDEX2(2,1,NUMNODES)]=N0-2;
     } else {
        out->FaceElements->Nodes[INDEX2(0,1,NUMNODES)]=N0-1;
     }
  }
  out->FaceElements->minColor=0;
  out->FaceElements->maxColor=1;

  /*  face elements done: */
  
  /*   condense the nodes: */
  
  Finley_Mesh_resolveNodeIds(out);

  /* prepare mesh for further calculations:*/

  Finley_Mesh_prepare(out) ;

  #ifdef Finley_TRACE
  printf("timing: mesh generation: %.4e sec\n",Finley_timer()-time0);
  #endif

  if (! Finley_noError()) {
      Finley_Mesh_dealloc(out);
      return NULL;
  }
  return out;
}

/*
* Revision 1.3  2005/09/01 03:31:36  jgs
* Merge of development branch dev-02 back to main trunk on 2005-09-01
*
* Revision 1.2.2.2  2005/09/07 06:26:19  gross
* the solver from finley are put into the standalone package paso now
*
* Revision 1.2.2.1  2005/08/24 02:02:18  gross
* timing output switched off. solver output can be swiched through getSolution(verbose=True) now.
*
* Revision 1.2  2005/07/08 04:07:53  jgs
* Merge of development branch back to main trunk on 2005-07-08
*
* Revision 1.1.1.1.2.1  2005/06/29 02:34:52  gross
* some changes towards 64 integers in finley
*
* Revision 1.1.1.1  2004/10/26 06:53:57  jgs
* initial import of project esys2
*
* Revision 1.1.1.1  2004/06/24 04:00:40  johng
* Initial version of eys using boost-python.
*
*
*/

