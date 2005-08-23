/* $Id$ */

/**************************************************************/

/* Finley: SystemMatrix                                           */

/*  returns a borrowed reference to the matrix normaliztion vector */

/*  if the vector is in valid a new vector is calculate as the inverse */
/*  of the sum of the absolute value in each row/column                */

/**************************************************************/

/* Copyrights by ACcESS Australia 2005 */
/* Author: gross@access.edu.au */

/**************************************************************/

#include "Finley.h"
#include "System.h"

double* Finley_SystemMatrix_borrowNormalization(Finley_SystemMatrix* A) {
   dim_t ir,irow,ic,icb,icol,irb;
   index_t iptr,icol_failed,irow_failed;
   double fac;
   if (!A->normalizer_is_valid) {
      switch(A->type) {
        case CSR:
          irow_failed=-1;
          #pragma omp parallel for private(ir,irow,fac,iptr,icb) schedule(static)
          for (ir=0;ir< A->pattern->n_ptr;ir++) {
	    for (irb=0;irb< A->row_block_size;irb++) {
	      irow=irb+A->row_block_size*ir;
              fac=0.;
	      for (iptr=A->pattern->ptr[ir]-PTR_OFFSET;iptr<A->pattern->ptr[ir+1]-PTR_OFFSET; iptr++) {
	          for (icb=0;icb< A->col_block_size;icb++) 
                    fac+=ABS(A->val[iptr*A->block_size+irb+A->row_block_size*icb]);
              }
              if (fac>0) {
                 A->normalizer[irow]=1./fac;
              } else {
                 A->normalizer[irow]=1.;
                 irow_failed=irow;
              }
            }
          }
          if (irow_failed>=0) {
             Finley_ErrorCode=ZERO_DIVISION_ERROR;
             sprintf(Finley_ErrorMsg,"Row %d contains zero entries only.",irow_failed);
          }
          break;
        case CSC:
          icol_failed=-1;
          #pragma omp parallel for private(ic,icb,icol,fac,iptr,irb) schedule(static)
          for (ic=0;ic< A->pattern->n_ptr;ic++) {
    	     for (icb=0;icb< A->col_block_size;icb++) {
	       icol=icb+A->col_block_size*ic;
               fac=0.;
	       for (iptr=A->pattern->ptr[ic]-PTR_OFFSET;iptr<A->pattern->ptr[ic+1]-PTR_OFFSET; iptr++) {
	          for (irb=0;irb< A->row_block_size;irb++) 
                     fac+=ABS(A->val[iptr*A->block_size+irb+A->row_block_size*icb]);
               }
               if (fac>0) {
                  A->normalizer[icol]=1./fac;
               } else {
                  A->normalizer[icol]=1.;
                  icol_failed=icol;
               }
             }
           }
           if (icol_failed>=0) {
              Finley_ErrorCode=ZERO_DIVISION_ERROR;
              sprintf(Finley_ErrorMsg,"Column %d contains zero entries only.",icol_failed);
           }
           break;
      default:
        Finley_ErrorCode=TYPE_ERROR;
        sprintf(Finley_ErrorMsg,"Unknown matrix type.");
      } /* switch A->type */
      A->normalizer_is_valid=TRUE;
   }
   return A->normalizer;
}
/*
 * $Log$
 * Revision 1.2  2005/08/23 01:24:30  jgs
 * Merge of development branch dev-02 back to main trunk on 2005-08-23
 *
 * Revision 1.1.2.1  2005/08/19 07:37:23  gross
 * missing System_borrowNormalization.c
 *
 *
 */
