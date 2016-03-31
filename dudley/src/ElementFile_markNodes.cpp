
/*****************************************************************************
*
* Copyright (c) 2003-2016 by The University of Queensland
* http://www.uq.edu.au
*
* Primary Business: Queensland, Australia
* Licensed under the Apache License, version 2.0
* http://www.apache.org/licenses/LICENSE-2.0
*
* Development until 2012 by Earth Systems Science Computational Center (ESSCC)
* Development 2012-2013 by School of Earth Sciences
* Development from 2014 by Centre for Geoscience Computing (GeoComp)
*
*****************************************************************************/

/****************************************************************************/

/*   Dudley: ElementFile */

/*   mark the used nodes with offset: */

/****************************************************************************/

#include "ElementFile.h"

namespace dudley {

void Dudley_ElementFile_markNodes(index_t* mask, index_t offset, dim_t numNodes, Dudley_ElementFile* in, bool useLinear)
{
    dim_t i, NN, e;
    if (in != NULL)
    {
        NN = in->numNodes;
#pragma omp parallel for private(e,i) schedule(static)
        for (e = 0; e < in->numElements; e++)
        {
            for (i = 0; i < NN; i++)
            {
                mask[in->Nodes[INDEX2(i, e, NN)] - offset] = 1;
            }
        }
    }
}

void Dudley_ElementFile_markDOFsConnectedToRange(index_t * mask, index_t offset, index_t marker, index_t firstDOF,
                                                 index_t lastDOF, index_t * dofIndex, Dudley_ElementFile * in,
                                                 bool useLinear)
{
    dim_t i, NN, e, j;
    index_t color;
    index_t k;

    if (in != NULL)
    {
        NN = in->numNodes;
        for (color = in->minColor; color <= in->maxColor; color++)
        {
#pragma omp parallel for private(e,i,j,k) schedule(static)
            for (e = 0; e < in->numElements; e++)
            {
                if (in->Color[e] == color)
                {
                    for (i = 0; i < NN; i++)
                    {
                        k = dofIndex[in->Nodes[INDEX2(i, e, NN)]];
                        if ((firstDOF <= k) && (k < lastDOF))
                        {
                            for (j = 0; j < NN; j++)
                                mask[dofIndex[in->Nodes[INDEX2(j, e, NN)]] - offset] = marker;
                            break;
                        }
                    }
                }
            }
        }
    }
}

} // namespace dudley

