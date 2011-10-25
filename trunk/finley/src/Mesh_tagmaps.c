
/*******************************************************
*
* Copyright (c) 2003-2010 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/


/**************************************************************/

/*   Finley: Mesh tagmaps: provides access to the mesh tag map */

/**************************************************************/

#include "Mesh.h"

/**************************************************************/

void Finley_Mesh_addTagMap(Finley_Mesh *mesh_p,const char* name, index_t tag_key) 
{
   Finley_TagMap_insert(&(mesh_p->TagMap),name,tag_key);
}
index_t Finley_Mesh_getTag(Finley_Mesh *mesh_p,const char* name) {
   return Finley_TagMap_getTag(mesh_p->TagMap,name);
}
bool_t Finley_Mesh_isValidTagName(Finley_Mesh *mesh_p,const char* name) {
   return Finley_TagMap_isValidTagName(mesh_p->TagMap,name);
}
