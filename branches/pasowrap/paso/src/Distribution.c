
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

/*   Paso: distribution                                       */

/**************************************************************/

/*   Author: Lutz Gross, l.gross@uq.edu.au */

/**************************************************************/

#include "Distribution.h"
#include "PasoUtil.h"
#include "esysUtils/error.h"  /* For checkPtr */

Paso_Distribution* Paso_Distribution_alloc( Esys_MPIInfo *mpi_info, 
                                            index_t *first_component,
                                            index_t m, index_t b) 
{
  int i;
  Paso_Distribution *out=NULL;
  out = MEMALLOC( 1, Paso_Distribution );
  if (Esys_checkPtr(out)) return NULL;
  out->mpi_info = Esys_MPIInfo_getReference(mpi_info);
  out->reference_counter = 0;
  out->first_component=NULL;

  out->first_component = MEMALLOC( (mpi_info->size)+1, index_t );
  if (Esys_checkPtr(out->first_component)) {
       Paso_Distribution_free(out);
       return NULL;
  }
  for (i=0; i<(mpi_info->size)+1; ++i) out->first_component[i]=m*first_component[i]+b;
  out->reference_counter++;
  return out;
}

void Paso_Distribution_free( Paso_Distribution *in )
{
  if (in != NULL) {
    --(in->reference_counter);
    if (in->reference_counter<=0) {
      Esys_MPIInfo_free( in->mpi_info );
      MEMFREE( in->first_component );
      MEMFREE( in );
    } 
  }
}

Paso_Distribution* Paso_Distribution_getReference( Paso_Distribution *in )
{
  if ( in != NULL) 
    in->reference_counter++;
  return in;
}

index_t Paso_Distribution_getFirstComponent(Paso_Distribution *in ) {
 if (in !=NULL) {
   return in->first_component[in->mpi_info->rank];
 } else {
   return 0;
 }
}
index_t Paso_Distribution_getLastComponent(Paso_Distribution *in ){
 if (in !=NULL) {
   return in->first_component[(in->mpi_info->rank)+1];
 } else {
   return 0;
 }
}

dim_t Paso_Distribution_getGlobalNumComponents(Paso_Distribution *in ){
   return Paso_Distribution_getMaxGlobalComponents(in)-Paso_Distribution_getMinGlobalComponents(in);
}
dim_t Paso_Distribution_getMyNumComponents(Paso_Distribution *in ) {
   return Paso_Distribution_getLastComponent(in)-Paso_Distribution_getFirstComponent(in);
}

dim_t Paso_Distribution_getMinGlobalComponents(Paso_Distribution *in ){
 if (in !=NULL) {
   return in->first_component[0];
 } else {
   return 0;
 }
}
dim_t Paso_Distribution_getMaxGlobalComponents(Paso_Distribution *in ){
 if (in !=NULL) {
   return in->first_component[in->mpi_info->size];
 } else {
   return 0;
 }
}

/* Pseudo random numbers such that the values are independent from
   the distribution */

static double Paso_Distribution_random_seed=.4142135623730951;

double* Paso_Distribution_createRandomVector(Paso_Distribution *in, const dim_t block )
{
   
   index_t i;
   double *out=NULL;
   const index_t n_0 = in->first_component[in->mpi_info->rank] * block;
   const index_t n_1 = in->first_component[in->mpi_info->rank+1] * block;
   const index_t n = ( Paso_Distribution_getMaxGlobalComponents(in)-Paso_Distribution_getMinGlobalComponents(in) ) * block;
   const dim_t my_n = n_1-n_0;
   
   out=MEMALLOC(my_n , double);

   #pragma omp parallel for private(i) schedule(static)
   for (i=0; i<my_n ;++i) {
      out[i]=fmod( Paso_Distribution_random_seed*(n_0+i+1) ,1.);
   }
   
   Paso_Distribution_random_seed=fmod( Paso_Distribution_random_seed * (n+1), 1.);
   
   return out;
}

dim_t Paso_Distribution_numPositives(const double* x, const Paso_Distribution *in, const dim_t block )
{
   
   dim_t my_out, out;
   const index_t n_0 = in->first_component[in->mpi_info->rank] * block;
   const index_t n_1 = in->first_component[in->mpi_info->rank+1] * block;
   const dim_t my_n = n_1-n_0;
   

   my_out = Paso_Util_numPositives(my_n, x);
   
   #ifdef ESYS_MPI
      #pragma omp single
      {
	 MPI_Allreduce(&my_out,&out, 1, MPI_INT, MPI_SUM, in->mpi_info->comm);
      }
   #else
      out=my_out;
   #endif
   
   return out;
}
