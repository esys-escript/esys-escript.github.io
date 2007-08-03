/* $Id:$ */

/*
********************************************************************************
*               Copyright   2006, 2007 by ACcESS MNRF                          *
*                                                                              * 
*                 http://www.access.edu.au                                     *
*           Primary Business: Queensland, Australia                            *
*     Licensed under the Open Software License version 3.0 		       *
*        http://www.opensource.org/licenses/osl-3.0.php                        *
********************************************************************************
*/

/**************************************************************/

/* Paso: Coupler organizes the coupling with in a pattern/matrix   */
/*       across processors                                         */

/**************************************************************/
 
/* Author: gross@access.edu.au */

/**************************************************************/

#include "Coupler.h"

/**************************************************************/

/* allocates a Coupler  */


/**************************************************************/


Paso_Coupler* Paso_Coupler_alloc(Paso_SharedComponents* send,
                                 Paso_SharedComponents* recv)
{
  Paso_Coupler*out=NULL;
  Paso_resetError();
  out=MEMALLOC(1,Paso_Coupler);
  if ( send->distribution != recv->distribution ) {
     Paso_setError(SYSTEM_ERROR,"Paso_Coupler_alloc: send and recv distribution need to match.");
     return NULL;
  }
  if (!Paso_checkPtr(out)) {
      out->distribution=Paso_Distribution_getReference(send->distribution);
      out->send=Paso_SharedComponents_getReference(send);
      out->send_buffer=NULL;
      out->recv= Paso_SharedComponents_getReference(recv);
      out->recv_buffer=NULL;
      out->mpi_requests=NULL;
      out->mpi_stati=NULL;
      out->mpi_info = Paso_MPIInfo_getReference(send->mpi_info);
      out->reference_counter=1;
      
      #ifdef PASO_MPI
         out->mpi_requests=MEMALLOC(send->numNeighbors+recv->numNeighbors,MPI_Request);
         out->mpi_stati=MEMALLOC(send->numNeighbors+recv->numNeighbors,MPI_Status);
         Paso_checkPtr(out->mpi_requests);
         Paso_checkPtr(out->mpi_stati);
      #endif
  }
  if (Paso_noError()) {
     return out;
  } else {
     Paso_Coupler_free(out);
     return NULL;
  }
}

/* returns a reference to in */

Paso_Coupler* Paso_Coupler_getReference(Paso_Coupler* in) {
     if (in!=NULL) {
        ++(in->reference_counter);
     }
     return in;
}
  
/* deallocates a Coupler: */

void Paso_Coupler_free(Paso_Coupler* in) {
  if (in!=NULL) {
     in->reference_counter--;
     if (in->reference_counter<=0) {
        Paso_SharedComponents_free(in->send);
        MEMFREE(in->send_buffer);
        Paso_SharedComponents_free(in->recv);
        MEMFREE(in->recv_buffer);
        MEMFREE(in->mpi_requests);
        MEMFREE(in->mpi_stati);
        Paso_MPIInfo_free(in->mpi_info);
        MEMFREE(in);
        #ifdef Paso_TRACE
        printf("Paso_Coupler_dealloc: system matrix pattern as been deallocated.\n");
        #endif
     }
   }
}


void Paso_Coupler_allocBuffer(Paso_Coupler* coupler,dim_t block_size)
{
    Paso_MPIInfo *mpi_info = coupler->mpi_info;  
    if ( (coupler->send_buffer !=NULL) || (coupler->recv_buffer!=NULL) ) {
        Finley_setError(SYSTEM_ERROR,"Paso_Coupler_allocBuffer: coupler are still in use.");
        return;
    }
    coupler->block_size=block_size;
    if (coupler->mpi_info->size>1) {
        coupler->send_buffer=MEMALLOC(coupler->send->numSharedComponents * coupler->block_size,double);
        coupler->recv_buffer=MEMALLOC(coupler->recv->numSharedComponents * coupler->block_size,double);
        if (Paso_checkPtr(coupler->send_buffer) || Paso_checkPtr(coupler->recv_buffer) ) {
              TMPMEMFREE(coupler->send_buffer);
              TMPMEMFREE(coupler->recv_buffer);
        }
    }
    return;
}
void Paso_Coupler_freeBuffer(Paso_Coupler* coupler) 
{

  if (coupler->mpi_info->size>1) {
     MEMFREE(coupler->send_buffer);
     MEMFREE(coupler->recv_buffer);
  }
  return;
}

void Paso_Coupler_startCollect(Paso_Coupler* coupler, double* in)
{
  Paso_MPIInfo *mpi_info = coupler->mpi_info;  
  dim_t block_size=coupler->block_size;
  size_t block_size_size=block_size*sizeof(double);
  dim_t i,j;
  if ( mpi_info->size>1) {
     /* start reveiving input */
     #pragma omp master 
     {
        for (i=0; i< coupler->recv->numNeighbors; ++i) {
            #ifdef PASO_MPI
            MPI_Irecv(&(coupler->recv_buffer[coupler->recv->offsetInShared[i] *  block_size]),
                      (coupler->recv->offsetInShared[i+1]- coupler->recv->offsetInShared[i])*block_size,
                      MPI_DOUBLE,
                      coupler->recv->neighbor[i], 
                      mpi_info->msg_tag_counter+coupler->recv->neighbor[i],
                      mpi_info->comm,
                      &(coupler->mpi_requests[i]));
            #endif

        }
     }
     /* collect values into buffer */
     #pragma parallel omp for private(i)
     for (i=0; i < coupler->send->numSharedComponents;++i) {
        memcpy(&(coupler->send_buffer[(block_size)*i]),&(in[ block_size * coupler->send->shared[i]]), block_size_size);
     }
     /* send buffer out */
     #pragma omp master 
     {
        for (i=0; i< coupler->send->numNeighbors; ++i) {
             #ifdef PASO_MPI
             MPI_Issend(&(coupler->send_buffer[coupler->send->offsetInShared[i] *  block_size]),
                        (coupler->send->offsetInShared[i+1]- coupler->send->offsetInShared[i])*block_size,
                        MPI_DOUBLE,
                        coupler->send->neighbor[i], 
                        mpi_info->msg_tag_counter+mpi_info->rank,
                        mpi_info->comm,
                        &(coupler->mpi_requests[i+ coupler->recv->numNeighbors]));
             #endif 
        }
     }
     mpi_info->msg_tag_counter+mpi_info->size;
  }
}

double* Paso_Coupler_finishCollect(Paso_Coupler* coupler)
{
  Paso_MPIInfo *mpi_info = coupler->mpi_info;  
  if ( mpi_info->size>1) {
     /* wait for receive */
     #pragma omp master 
     {
        #ifdef PASO_MPI
        MPI_Waitall(coupler->recv->numNeighbors+coupler->send->numNeighbors,
                    coupler->mpi_requests,
                    coupler->mpi_stati);
        #endif
     }
  }
  return coupler->recv_buffer;
}

Paso_Coupler* Paso_Coupler_unroll(Paso_Coupler* in, index_t block_size) {
     Paso_SharedComponents *new_send_shcomp=NULL, *new_recv_shcomp=NULL;
     Paso_Coupler *out=NULL;
     Paso_Distribution*new_distribution;
     new_distribution=Paso_Distribution_alloc(in->mpi_info,
                                              in->distribution->first_component,
                                              block_size,0);
     if (Paso_noError()) {
        new_send_shcomp=Paso_SharedComponents_alloc(in->send->numComponents,in->send->globalComponent,block_size,0,new_distribution);
        new_recv_shcomp=Paso_SharedComponents_alloc(in->recv->numComponents,in->recv->globalComponent,block_size,0,new_distribution);
        if (Paso_noError()) out=Paso_Coupler_alloc(new_send_shcomp,new_recv_shcomp);
     }
     Paso_Distribution_free(new_distribution);
     Paso_SharedComponents_free(new_send_shcomp);
     Paso_SharedComponents_free(new_recv_shcomp);
     if (Paso_noError()) {
          return out;
     } else {
          Paso_Coupler_free(out);
          return NULL;
     } 

}

