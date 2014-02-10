
/*******************************************************
*
* Copyright (c) 2003-2012 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/

/**************************************************************/
/*                                                                                            */
/*   Dudley: ElementFile                                                                      */
/*                                                                                            */
/*   returns the maximum and minimum node reference number of nodes describing the elements:; */
/*                                                                                            */
/*                                                                                            */
/**************************************************************/

#include "ElementFile.h"
#include "Util.h"

/**************************************************************/

void Dudley_ElementFile_setNodeRange(index_t * min_id, index_t * max_id, Dudley_ElementFile * in)
{
    if (in != NULL)
    {
	*min_id = Dudley_Util_getMinInt(in->numNodes, in->numElements, in->Nodes);
	*max_id = Dudley_Util_getMaxInt(in->numNodes, in->numElements, in->Nodes);
    }
    else
    {
	*min_id = INDEX_T_MAX;
	*max_id = -INDEX_T_MAX;
    }
}