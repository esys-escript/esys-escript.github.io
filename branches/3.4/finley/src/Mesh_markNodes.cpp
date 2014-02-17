
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

/*   Finley: Mesh */

/*   mark the used nodes with offset */

/************************************************************************************/

#include "Mesh.h"

/************************************************************************************/

void Finley_Mesh_markNodes(index_t* mask,index_t offset,Finley_Mesh* in,bool_t useLinear) {
    in->Elements->markNodes(mask, offset, useLinear);
    in->FaceElements->markNodes(mask, offset, useLinear);
    in->ContactElements->markNodes(mask, offset, useLinear);
    in->Points->markNodes(mask, offset, useLinear);
}

void Finley_Mesh_markDOFsConnectedToRange(index_t* mask, index_t offset, index_t marker, 
                                          index_t firstDOF,index_t lastDOF,Finley_Mesh* in, bool_t useLinear)
{
   index_t *dofIndex;
   if (useLinear) {
       dofIndex=in->Nodes->globalReducedDOFIndex;
   } else {
       dofIndex=in->Nodes->globalDegreesOfFreedom;
   }
   in->Elements->markDOFsConnectedToRange(mask,offset,marker,firstDOF,lastDOF,dofIndex,useLinear);
   in->FaceElements->markDOFsConnectedToRange(mask,offset,marker,firstDOF,lastDOF,dofIndex,useLinear);
   in->ContactElements->markDOFsConnectedToRange(mask,offset,marker,firstDOF,lastDOF,dofIndex,useLinear);
   in->Points->markDOFsConnectedToRange(mask,offset,marker,firstDOF,lastDOF,dofIndex,useLinear);
}