
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


/****************************************************************************

  Finley: ElementFile

  This routine tries to reduce the number of colours used to colour elements
  in the Finley_ElementFile 'in'.

*****************************************************************************/

#include "ElementFile.h"
#include "Util.h"

#include <vector>

void Finley_ElementFile_createColoring(Finley_ElementFile* in, dim_t numNodes,
                                       index_t* degreeOfFreedom)
{
    if (!in || in->numElements < 1)
        return;

    const int NN = in->numNodes;
    const int min_id=Finley_Util_getMinInt(1, numNodes, degreeOfFreedom);
    const int max_id=Finley_Util_getMaxInt(1, numNodes, degreeOfFreedom);
    const int len=max_id-min_id+1;

    // reset color vector
#pragma omp parallel for
    for (int e=0; e<in->numElements; e++)
        in->Color[e]=-1;

    int numUncoloredElements=in->numElements;
    in->minColor=0;
    in->maxColor=in->minColor-1;
    while (numUncoloredElements>0) {
        // initialize the mask marking nodes used by a color
        std::vector<int> maskDOF(len, -1);
        numUncoloredElements=0;

        // TODO: OMP
        for (int e=0; e<in->numElements; e++) {
            if (in->Color[e] < 0) {
                // find out if element e is independent from the elements
                // already coloured:
                bool independent = true; 
                for (int i=0; i<NN; i++) {
#ifdef BOUNDS_CHECK
if (in->Nodes[INDEX2(i,e,NN)] < 0 || in->Nodes[INDEX2(i,e,NN)] >= numNodes) {
    printf("BOUNDS_CHECK %s %d i=%d e=%d NN=%d min_id=%d in->Nodes[INDEX2...]=%d\n", __FILE__, __LINE__, i, e, NN, min_id, in->Nodes[INDEX2(i,e,NN)]);
    exit(1);
}
if ((degreeOfFreedom[in->Nodes[INDEX2(i,e,NN)]]-min_id) >= len || (degreeOfFreedom[in->Nodes[INDEX2(i,e,NN)]]-min_id) < 0) {
    printf("BOUNDS_CHECK %s %d i=%d e=%d NN=%d min_id=%d dof=%d\n", __FILE__, __LINE__, i, e, NN, min_id, degreeOfFreedom[in->Nodes[INDEX2(i,e,NN)]]-min_id);
    exit(1);
}
#endif
                    if (maskDOF[degreeOfFreedom[in->Nodes[INDEX2(i,e,NN)]]-min_id]>0) {
                        independent=false;
                        break;
                    }
                }
                // if e is independent a new color is assigned and the nodes
                // are marked as being used
                if (independent) {
                    for (int i=0; i<NN; i++)
                        maskDOF[degreeOfFreedom[in->Nodes[INDEX2(i,e,NN)]]-min_id] = 1;
                    in->Color[e]=in->maxColor+1;
                } else {
                    numUncoloredElements++;
                }
            } // if no colour yet
        } // for all elements
        in->maxColor++;
    } // end of while loop
}
