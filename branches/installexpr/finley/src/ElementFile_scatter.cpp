
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


/************************************************************************************
*                                                                                            
*   Finley: ElementFile                                                                      
*                                                                                            
*   scatter the ElementFile in into the ElementFile out using index[0:out->numElements-1].  
*   index has to be between 0 and in->numElements-1.                                         
*   a conservative assumption on the coloring is made                                         
*                                                                                            
************************************************************************************/

#include "ElementFile.h"

/************************************************************************************/

void Finley_ElementFile_scatter(index_t* index, Finley_ElementFile* in, Finley_ElementFile* out) {
   index_t k;
   dim_t e,j;
   if (in!=NULL) {
     dim_t NN_in=in->numNodes;
     dim_t NN_out=out->numNodes;
     #pragma omp parallel for private(e,k,j) schedule(static)
     for (e=0;e<in->numElements;e++) {
        k=index[e];
        out->Owner[k]=in->Owner[e];
        out->Id[k]=in->Id[e];
        out->Tag[k]=in->Tag[e];
        out->Color[k]=in->Color[e]+out->maxColor+1;
        for(j=0;j<MIN(NN_out,NN_in);j++) out->Nodes[INDEX2(j,k,NN_out)]=in->Nodes[INDEX2(j,e,NN_in)];
     }
     out->minColor=MIN(out->minColor,in->minColor+out->maxColor+1);
     out->maxColor=MAX(out->maxColor,in->maxColor+out->maxColor+1);
   }
}