
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


#include "NodeMapping.h"
#include "Util.h"
#include "esysUtils/mem.h"

Finley_NodeMapping* Finley_NodeMapping_alloc(dim_t numNodes, index_t* target, index_t unused)
{
  dim_t i;
  index_t min_target, numTargets, max_target;
  Finley_NodeMapping* out=NULL;
  /*  allocate the return value */
  min_target=Finley_Util_getFlaggedMinInt(1,numNodes,target,unused);
  if (min_target<0) {
     Finley_setError(VALUE_ERROR,"Finley_NodeMapping_alloc: target has negative entry.");
     return NULL;
  }
  /* now we assume min_target=0! */
  max_target=Finley_Util_getFlaggedMaxInt(1,numNodes,target,unused);
  numTargets= min_target<=max_target ? max_target+1 :0;
  out=new Finley_NodeMapping;
  if (!Finley_checkPtr(out)) {
     out->reference_counter=1;
     out->unused=unused;
     out->numNodes=numNodes;
     out->numTargets=numTargets;
     out->map=new index_t[numTargets];
     out->target=new index_t[numNodes];
     if (! (Finley_checkPtr(out->target) || Finley_checkPtr(out->map) ) ) {
        #pragma omp parallel
        {
           #pragma omp for private(i)
           for (i=0; i<numTargets; ++i)out-> map[i]=-1;
           #pragma omp for private(i)
           for (i=0;i<numNodes;++i) {
             out->target[i]=target[i];
             if (target[i] != unused) out->map[out->target[i]]=i;
           }
           #pragma omp for private(i)
           for (i=0; i<numTargets; ++i) {
               if (out->map[i]==-1) {
                  Finley_setError(VALUE_ERROR,"Finley_NodeMapping_alloc: target does not define a continuous labeling.");
               }
           }
        }
     }
     if (!Finley_noError()) {
         Finley_NodeMapping_free(out) ;
     }
          
  }      
  return out;
}

void Finley_NodeMapping_free(Finley_NodeMapping* in) {
  if (in != NULL) {
      in->reference_counter--;
      if (in->reference_counter<=0) {
         delete[] in->target;
         delete[] in->map; 
         delete in;  
     }
  }
}
Finley_NodeMapping* Finley_NodeMapping_getReference(Finley_NodeMapping *in) 
{
  if (in != NULL) 
    in->reference_counter++;
  return in;
}
