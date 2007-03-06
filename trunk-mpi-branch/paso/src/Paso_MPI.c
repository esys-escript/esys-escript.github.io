#include <stdlib.h>
#include <stdio.h>


#include "Paso_MPI.h"


/* allocate memory for an mpi_comm, and find the communicator details */
Paso_MPIInfo* Paso_MPIInfo_alloc( MPI_Comm comm )
{
  int error;
  Paso_MPIInfo *out=NULL;

  out = MEMALLOC( 1, Paso_MPIInfo );
  
  out->reference_counter = 0;
  #ifdef PASO_MPI
     error = MPI_Comm_rank( comm, &out->rank )==MPI_SUCCESS && MPI_Comm_size( comm, &out->size )==MPI_SUCCESS;
     if( !error ) {
       Paso_setError( PASO_MPI_ERROR, "Paso_MPIInfo_alloc : error finding comm rank/size" );
     }
  
     out->comm = comm;
  #else
     out->rank=0;
     out->size=1;
     out->comm 0;
  #endif
  out->reference_counter++;

  return out;
}

/* free memory for an mpi_comm */
void Paso_MPIInfo_dealloc( Paso_MPIInfo *in )
{
  if( in && !(--in->reference_counter) )
    MEMFREE( in );
}

Paso_MPIInfo *Paso_MPIInfo_getReference( Paso_MPIInfo* in )
{
  if (in!=NULL) 
    ++(in->reference_counter);
  
  return in;
}


/* checks that there is no error accross all processes in a communicator */
/* NOTE : does not make guarentee consistency of error string on each process */
bool_t Paso_MPI_noError( Paso_MPIInfo *mpi_info )
{
  int errorGlobal=0;
  int errorLocal = (int)Paso_noError();
  #ifdef PASO_MPI
     MPI_Allreduce( &errorLocal, &errorGlobal, 1, MPI_INT, MPI_LAND, mpi_info->comm  );

           // take care of the case where the error was on another processor
           if( errorLocal && !errorGlobal )
                   Paso_setError( PASO_MPI_ERROR, "Paso_MPI_noError() : there was an error on another MPI process" );
  #else
     errorGlobal=errorLocal;
  #endif
  return (bool_t) errorGlobal;
}


/**************************************************
                 WRAPPERS 
**************************************************/

int Paso_MPI_initialized( void )
{
  int error=0, initialised=0;

  #ifdef PASO_MPI
     error = MPI_Initialized( &initialised );
     if( error!=MPI_SUCCESS )
         Paso_setError( PASO_MPI_ERROR, "mpi_initialised : MPI error" );
     return initialised;
  #else
     return TRUE;
  #endif
}
