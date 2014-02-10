
/*******************************************************
*
* Copyright (c) 2003-2009 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/


/**************************************************************/

/*   Finley: Mesh: ElementFile */

/*  set tags to newTag where mask>0 */

/**************************************************************/

#include "ElementFile.h"
#include "Util.h"
#include "Assemble.h"

/**************************************************************/


void Finley_ElementFile_setTags(Finley_ElementFile* self,const int newTag, escriptDataC* mask) {
    register dim_t n,q;
    dim_t numElements, numQuad;
    register __const double *mask_array;
    register bool_t check;
    Finley_resetError();
    if (self==NULL) return;
    numElements=self->numElements;
    if (Finley_Assemble_reducedIntegrationOrder(mask)) {
       numQuad=self->ReferenceElementReducedOrder->numQuadNodes;
    } else {
       numQuad=self->ReferenceElement->numQuadNodes;
    }

    if (1!=getDataPointSize(mask)) {
       Finley_setError(TYPE_ERROR,"Finley_ElementFile_setTags: number of components of mask is 1.");
    } else if (!numSamplesEqual(mask,numQuad,numElements)) {
       Finley_setError(TYPE_ERROR,"Finley_ElementFile_setTags: illegal number of samples of mask Data object");
    }

    /* now we can start */

    if (Finley_noError()) {
         if (isExpanded(mask)) {
	   void* buffer=allocSampleBuffer(mask);	   
	   #pragma omp parallel private(n,check,mask_array)
	   {
             #pragma omp for schedule(static)
             for (n=0;n<numElements;n++) {
                 mask_array=getSampleDataRO(mask,n,buffer);
                 if (mask_array[0]>0) self->Tag[n]=newTag;
             }
	   }
	   freeSampleBuffer(buffer);
         } else {
	   void* buffer=allocSampleBuffer(mask);
	   #pragma omp parallel private(q,n,check,mask_array)
	   {
             #pragma omp for schedule(static)
             for (n=0;n<numElements;n++) {
                 mask_array=getSampleDataRO(mask,n,buffer);
                 check=FALSE;
                 for (q=0;q<numQuad;q++) check=check || mask_array[q];
                 if (check) self->Tag[n]=newTag;
             }
	   }
	   freeSampleBuffer(buffer);
         }
         Finley_ElementFile_setTagsInUse(self);
    }
}
/*
* $Log$
*
*/