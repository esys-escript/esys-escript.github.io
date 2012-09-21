
/*****************************************************************************
*
* Copyright (c) 2003-2012 by University of Queensland
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

/* Paso: SharedComponents organizes the coupling within a     */
/*       pattern/matrix across processors                     */

/************************************************************************************/
 
/* Author: Lutz Gross, l.gross@uq.edu.au                      */

/************************************************************************************/

#include "SharedComponents.h"
#include "esysUtils/error.h"

/************************************************************************************/

/* allocates SharedComponents  */

/************************************************************************************/

Paso_SharedComponents* Paso_SharedComponents_alloc(dim_t local_length,
                                                   dim_t numNeighbors,
                                                   Esys_MPI_rank* neighbor,
                                                   index_t* shared,
                                                   index_t* offsetInShared,
                                                   index_t m, index_t b,
                                                   Esys_MPIInfo *mpi_info)
{
  dim_t i,j;
  register index_t itmp;
  Paso_SharedComponents* out=NULL;
  Esys_resetError();
  out=MEMALLOC(1,Paso_SharedComponents);
  if (!Esys_checkPtr(out)) {
      out->local_length=local_length*m;
      out->mpi_info = Esys_MPIInfo_getReference(mpi_info);
      out->numNeighbors=numNeighbors;
      out->neighbor=MEMALLOC(out->numNeighbors,Esys_MPI_rank);
      if (offsetInShared == NULL) {
          out->numSharedComponents=0;
      } else {
          out->numSharedComponents=offsetInShared[numNeighbors]*m;
      }
      out->shared=MEMALLOC(out->numSharedComponents,index_t);
      out->offsetInShared=MEMALLOC(out->numNeighbors+1,index_t);
      out->reference_counter=1;
      if (! (Esys_checkPtr(out->neighbor) ||
             Esys_checkPtr(out->shared) || 
             Esys_checkPtr(out->offsetInShared) ) ) {


         if ((out->numNeighbors>0) && (offsetInShared!=NULL) ) {
            #pragma omp parallel
            {
               #pragma omp for private(i)
               for (i=0;i<out->numNeighbors;++i){
                   out->neighbor[i]=neighbor[i];
                   out->offsetInShared[i]=offsetInShared[i]*m;
               }
               out->offsetInShared[out->numNeighbors]=offsetInShared[numNeighbors]*m;
               #pragma omp for private(i,j,itmp)
               for (i=0;i<offsetInShared[numNeighbors];++i){
                   itmp=m*shared[i]+b;
                   for (j=0;j<m;++j) out->shared[m*i+j]=itmp+j;
               }
            }
         } else {
            out->offsetInShared[out->numNeighbors]=0;
         }
      }

  }
  if (Esys_noError()) {
     return out;
  } else {
     Paso_SharedComponents_free(out);
     return NULL;
  }
}

/* returns a reference to in */

Paso_SharedComponents* Paso_SharedComponents_getReference(Paso_SharedComponents* in) {
     if (in!=NULL) {
        ++(in->reference_counter);
     }
     return in;
}
  
/* deallocates SharedComponents */

void Paso_SharedComponents_free(Paso_SharedComponents* in) {
  if (in!=NULL) {
     in->reference_counter--;
     if (in->reference_counter<=0) {
        MEMFREE(in->neighbor);
        MEMFREE(in->shared);
        MEMFREE(in->offsetInShared);
        Esys_MPIInfo_free(in->mpi_info);
        MEMFREE(in);
        #ifdef Paso_TRACE
        printf("Paso_SharedComponents_dealloc: system matrix pattern has been deallocated.\n");
        #endif
     }
   }
}

