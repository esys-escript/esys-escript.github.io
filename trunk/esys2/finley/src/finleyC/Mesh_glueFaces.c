/**************************************************************/

/*   Finley: Mesh */

/* removes matching face elements from self */

/**************************************************************/

/*   Copyrights by ACcESS Australia 2003/04 */
/*   Author: gross@access.edu.au */
/*   Version: $Id$ */

/**************************************************************/

#include "Common.h"
#include "Finley.h"
#include "Mesh.h"

/**************************************************************/


void Finley_Mesh_glueFaces(Finley_Mesh* self,double safety_factor,double tolerance) { 
   Finley_NodeFile *newNodeFile=NULL;
   Finley_ElementFile *newFaceElementsFile=NULL;
   dim_t numPairs,e,i,n;
   index_t face_node, *elem1=NULL,*elem0=NULL,*elem_mask=NULL,*new_node_label=NULL,*new_node_list=NULL,*new_node_mask=NULL,*matching_nodes_in_elem1=NULL;

   if (self->FaceElements==NULL) return;

   if (self->FaceElements->ReferenceElement->Type->numNodesOnFace<=0) {
     Finley_ErrorCode=TYPE_ERROR;
     sprintf(Finley_ErrorMsg,"glueing faces cannot be applied to face elements pf type %s",self->FaceElements->ReferenceElement->Type->Name);
     return;
   }

   dim_t NNFace=self->FaceElements->ReferenceElement->Type->numNodesOnFace;
   dim_t NN=self->FaceElements->ReferenceElement->Type->numNodes;
   dim_t numDim=self->Nodes->numDim;
   /* allocate work arrays */
   elem1=TMPMEMALLOC(self->FaceElements->numElements,index_t);
   elem0=TMPMEMALLOC(self->FaceElements->numElements,index_t);
   elem_mask=TMPMEMALLOC(self->FaceElements->numElements,index_t);
   matching_nodes_in_elem1=TMPMEMALLOC(self->FaceElements->numElements*NN,index_t);
   new_node_label=TMPMEMALLOC(self->Nodes->numNodes,index_t);
   new_node_list=TMPMEMALLOC(self->Nodes->numNodes,index_t);
   new_node_mask=TMPMEMALLOC(self->Nodes->numNodes,index_t);
   if (!(Finley_checkPtr(elem1) || Finley_checkPtr(elem0) || Finley_checkPtr(elem_mask) || Finley_checkPtr(new_node_label) || Finley_checkPtr(new_node_list) || Finley_checkPtr(new_node_mask) || Finley_checkPtr(matching_nodes_in_elem1)) ) {
      /* find the matching face elements */
      Finley_Mesh_findMatchingFaces(self->Nodes,self->FaceElements,safety_factor,tolerance,&numPairs,elem0,elem1,matching_nodes_in_elem1);
      if (Finley_ErrorCode==NO_ERROR) {
         for(e=0;e<self->FaceElements->numElements;e++) elem_mask[e]=0;
         for(n=0;n<self->Nodes->numNodes;n++) new_node_label[n]=n;
         /* remove mark imatching face elements to be removed */
         for(e=0;e<numPairs;e++) {
             elem_mask[elem0[e]]=1;
             elem_mask[elem1[e]]=1;
             for (i=0;i<NNFace;i++) {
                face_node=self->FaceElements->ReferenceElement->Type->faceNode[i];
                new_node_label[matching_nodes_in_elem1[INDEX2(face_node,e,NN)]]=self->FaceElements->Nodes[INDEX2(face_node,elem0[e],NN)];
             }
         }
         /* create an index of face elements */
         dim_t new_numFaceElements=0;
         for(e=0;e<self->FaceElements->numElements;e++) {
             if (elem_mask[e]<1) {
               elem_mask[new_numFaceElements]=e;
               new_numFaceElements++;
             }
         }
         /* get the new number of nodes */
         dim_t newNumNodes=0;
         for (n=0;n<self->Nodes->numNodes;n++) new_node_mask[n]=-1;
         for (n=0;n<self->Nodes->numNodes;n++) new_node_mask[new_node_label[n]]=1;
         for (n=0;n<self->Nodes->numNodes;n++) {
               if (new_node_mask[n]>0) {
                   new_node_mask[n]=newNumNodes;
                   new_node_list[newNumNodes]=n;
                   newNumNodes++;
               }
         }
         for (n=0;n<self->Nodes->numNodes;n++) new_node_label[n]=new_node_mask[new_node_label[n]];
         /* allocate new node and element files */
         newNodeFile=Finley_NodeFile_alloc(numDim); 
         if (Finley_ErrorCode==NO_ERROR) {
             Finley_NodeFile_allocTable(newNodeFile,newNumNodes);
             if (Finley_ErrorCode==NO_ERROR) {
                newFaceElementsFile=Finley_ElementFile_alloc(self->FaceElements->ReferenceElement->Type->TypeId,self->FaceElements->order);
                if (Finley_ErrorCode==NO_ERROR) {
                   Finley_ElementFile_allocTable(newFaceElementsFile,new_numFaceElements);
                 }
              }
         }
         if (Finley_ErrorCode==NO_ERROR) {
            /* get the new nodes :*/
            Finley_NodeFile_gather(new_node_list,self->Nodes,newNodeFile);
            /* they are the new nodes*/
            Finley_NodeFile_dealloc(self->Nodes);
            self->Nodes=newNodeFile;
            /* get the face elements which are still in use:*/
            Finley_ElementFile_gather(elem_mask,self->FaceElements,newFaceElementsFile);
            /* they are the new face elements */
            Finley_ElementFile_dealloc(self->FaceElements);
            self->FaceElements=newFaceElementsFile;
            
            /* assign new node ids to elements */
            Finley_Mesh_relableElementNodes(new_node_label,0,self);
         } else {
            Finley_NodeFile_dealloc(newNodeFile);
            Finley_ElementFile_dealloc(newFaceElementsFile);
         }
      }
   } 
   TMPMEMFREE(elem1);
   TMPMEMFREE(elem0);
   TMPMEMFREE(elem_mask);
   TMPMEMFREE(new_node_label);
   TMPMEMFREE(new_node_list);
   TMPMEMFREE(new_node_mask);
   TMPMEMFREE(matching_nodes_in_elem1);
}

/*
* $Log$
* Revision 1.5  2005/07/08 04:07:52  jgs
* Merge of development branch back to main trunk on 2005-07-08
*
* Revision 1.4  2004/12/15 07:08:33  jgs
* *** empty log message ***
* Revision 1.1.1.1.2.2  2005/06/29 02:34:51  gross
* some changes towards 64 integers in finley
*
* Revision 1.1.1.1.2.1  2004/11/24 01:37:14  gross
* some changes dealing with the integer overflow in memory allocation. Finley solves 4M unknowns now
*
*
*
*/

