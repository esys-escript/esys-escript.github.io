/**************************************************************/

/*   Finley: Mesh */

/**************************************************************/

/*   Copyrights by ACcESS Australia 2003,04 */
/*   Author: gross@access.edu.au */
/*   Version: $Id$ */

/**************************************************************/

#include "Finley.h"
#include "Mesh.h"

/**************************************************************/

/*   allocates a Mesh with name name for elements of type id using an integration order. If order is negative, */
/*   the most appropriate order is selected indepently. */

extern Finley_RefElementInfo Finley_RefElement_InfoList[];

Finley_Mesh* Finley_Mesh_alloc(char* name,int numDim, int order) {
  Finley_Mesh *out;
  
  /*  allocate the return value */
  
  out=MEMALLOC(1,Finley_Mesh);
  if (Finley_checkPtr(out)) return NULL;
  out->Name=NULL;  
  out->Nodes=NULL; 
  out->Elements=NULL;   
  out->FaceElements=NULL; 
  out->Points=NULL;      
  out->ContactElements=NULL;      
  out->reference_counter=0;

  out->FullFullPattern=NULL;
  out->FullReducedPattern=NULL;
  out->ReducedFullPattern=NULL;
  out->ReducedReducedPattern=NULL;
  
  /*   copy name: */
  
  out->Name=MEMALLOC(strlen(name)+1,char);
  if (Finley_checkPtr(out->Name)) {
      Finley_Mesh_dealloc(out);
      return NULL;
  }
  strcpy(out->Name,name);
  
  /*   allocate node table: */
  
  out->Nodes=Finley_NodeFile_alloc(numDim);
  if (Finley_ErrorCode!=NO_ERROR) {
      Finley_Mesh_dealloc(out);
      return NULL;
  }
  out->order=order;
  out->Elements=NULL;
  out->FaceElements=NULL;
  out->Points=NULL;
  out->ContactElements=NULL;
  out->reference_counter++;
  return out;
}

/* returns a reference to Finley_Mesh in */

Finley_Mesh* Finley_Mesh_reference(Finley_Mesh* in) {
     if (in!=NULL) ++(in->reference_counter);
     return in;
}

/*   deallocates a mesh: */

void Finley_Mesh_dealloc(Finley_Mesh* in) {
  if (in!=NULL) {
     in->reference_counter--;
     if (in->reference_counter<1) {
       #ifdef Finley_TRACE
       if (in->Name!=NULL) {
           printf("Finley_Mesh_dealloc: mesh %s is deallocated.\n",in->Name);
       } else {
           printf("Finley_Mesh_dealloc\n");
       }
       #endif
       MEMFREE(in->Name);
       Finley_NodeFile_dealloc(in->Nodes);
       Finley_ElementFile_dealloc(in->Elements);   
       Finley_ElementFile_dealloc(in->FaceElements);
       Finley_ElementFile_dealloc(in->ContactElements);
       Finley_ElementFile_dealloc(in->Points);
       Finley_SystemMatrixPattern_dealloc(in->FullFullPattern);
       Finley_SystemMatrixPattern_dealloc(in->FullReducedPattern);
       Finley_SystemMatrixPattern_dealloc(in->ReducedFullPattern);
       Finley_SystemMatrixPattern_dealloc(in->ReducedReducedPattern);
       MEMFREE(in);      
     }
  }
}

/**************************************************************/

/*  returns the spatial dimension of the mesh: */

int Finley_Mesh_getDim(Finley_Mesh *in) {
  return in->Nodes->numDim;
}

/**************************************************************/

/*  returns the number of nodes in the mesh: */

int Finley_Mesh_getNumNodes(Finley_Mesh *in) {
  return in->Nodes->numNodes;
}
/**************************************************************/

/*  returns the number of degrees of freedom in the mesh: */

int Finley_Mesh_getNumDegreesOfFreedom(Finley_Mesh *in) {
  return in->Nodes->numDegreesOfFreedom;
}
/**************************************************************/

/*  returns the number of degrees of freedom in the mesh: */

int Finley_Mesh_getReducedNumDegreesOfFreedom(Finley_Mesh *in) {
  return in->Nodes->reducedNumDegreesOfFreedom;
}
/* 
* $Log$
* Revision 1.2  2004/12/14 05:39:30  jgs
* *** empty log message ***
*
* Revision 1.1.1.1.2.2  2004/11/24 01:37:13  gross
* some changes dealing with the integer overflow in memory allocation. Finley solves 4M unknowns now
*
* Revision 1.1.1.1.2.1  2004/11/12 06:58:18  gross
* a lot of changes to get the linearPDE class running: most important change is that there is no matrix format exposed to the user anymore. the format is chosen by the Domain according to the solver and symmetry
*
* Revision 1.1.1.1  2004/10/26 06:53:57  jgs
* initial import of project esys2
*
* Revision 1.1.1.1  2004/06/24 04:00:40  johng
* Initial version of eys using boost-python.
*
*
*/
