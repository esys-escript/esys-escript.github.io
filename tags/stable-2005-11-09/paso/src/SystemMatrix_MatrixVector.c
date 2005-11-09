/* $Id$ */

/**************************************************************/

/* Paso: matrix vector product with sparse matrix           */

/**************************************************************/

/* Copyrights by ACcESS Australia 2003,2004,2005 */
/* Author: gross@access.edu.au */

/**************************************************************/

#include "Paso.h"
#include "SystemMatrix.h"

/**************************************************************************/

/*  raw scaled vector update operation: out = alpha * A * in + beta * out */

/* has to be called within a parallel region                              */
/* barrier synconization is performed to make sure that the input vector available */

void  Paso_SystemMatrix_MatrixVector(double alpha,
    Paso_SystemMatrix* A,
    double* in,
    double beta,
    double* out) {

  register index_t ir,icol,iptr,icb,irb,irow,ic;
  register double reg,reg1,reg2,reg3;
  #pragma omp barrier

  if (ABS(beta)>0.) {
    #pragma omp for private(irow) schedule(static)
    for (irow=0;irow < A->num_rows * A->row_block_size;irow++) 
      out[irow] *= beta;
  } else {
    #pragma omp for private(irow) schedule(static)
    for (irow=0;irow < A->num_rows * A->row_block_size;irow++) 
      out[irow] = 0;
  }
      
  /*  do the operation: */
  if (ABS(alpha)>0) {
    if (A ->col_block_size==1 && A->row_block_size ==1) {
      switch(A->type) {
      case CSR:
        #pragma omp for private(irow,iptr,reg) schedule(static)
	for (irow=0;irow< A->pattern->n_ptr;++irow) {
          reg=0.;
	  for (iptr=(A->pattern->ptr[irow])-PTR_OFFSET;iptr<(A->pattern->ptr[irow+1])-PTR_OFFSET; ++iptr) {
	      reg += A->val[iptr] * in[A->pattern->index[iptr]-INDEX_OFFSET];
	  }
	  out[irow] += alpha * reg;
	}
	break;
      case CSC:
        /* TODO: parallelize (good luck!) */
        #pragma omp single
	for (icol=0;icol< A->pattern->n_ptr;++icol) {
	  for (iptr=A->pattern->ptr[icol]-PTR_OFFSET;iptr<A->pattern->ptr[icol+1]-PTR_OFFSET; ++iptr) {
	    out[A->pattern->index[iptr]-INDEX_OFFSET]+= alpha * A->val[iptr] * in[icol];
	  }
	}
	break;
      default:
	Paso_setError(TYPE_ERROR,"Unknown matrix type in MVM.");
      } /* switch A->type */
    } else if (A ->col_block_size==2 && A->row_block_size ==2) {
      switch(A->type) {
      case CSR:
        #pragma omp for private(ir,iptr,irb,icb,irow,icol,reg1,reg2) schedule(static)
	for (ir=0;ir< A->pattern->n_ptr;ir++) {
          reg1=0.;
          reg2=0.;
	  for (iptr=A->pattern->ptr[ir]-PTR_OFFSET;iptr<A->pattern->ptr[ir+1]-PTR_OFFSET; iptr++) {
	       ic=2*(A->pattern->index[iptr]-INDEX_OFFSET);
	       reg1 += A->val[iptr*4  ]*in[ic] + A->val[iptr*4+2]*in[1+ic];
	       reg2 += A->val[iptr*4+1]*in[ic] + A->val[iptr*4+3]*in[1+ic];
	  }
	  out[  2*ir] += alpha * reg1;
	  out[1+2*ir] += alpha * reg2;
	}
	break;
      case CSC:
        /* TODO: parallelize */
        #pragma omp single
	for (ic=0;ic< A->pattern->n_ptr;ic++) {
	  for (iptr=A->pattern->ptr[ic]-PTR_OFFSET;iptr<A->pattern->ptr[ic+1]-PTR_OFFSET; iptr++) {
	       ic=2*(A->pattern->index[iptr]-INDEX_OFFSET);
	       out[  2*ir] += alpha * ( A->val[iptr*4  ]*in[ic] + A->val[iptr*4+2]*in[1+ic] );
	       out[1+2*ir] += alpha * ( A->val[iptr*4+1]*in[ic] + A->val[iptr*4+3]*in[1+ic] );
	  }
	}
      default:
	Paso_setError(TYPE_ERROR,"Unknown matrix type in MVM.");
      } /* switch A->type */
    } else if (A ->col_block_size==3 && A->row_block_size ==3) {
      switch(A->type) {
      case CSR:
        #pragma omp for private(ir,iptr,irb,icb,irow,icol,reg1,reg2,reg3) schedule(static)
	for (ir=0;ir< A->pattern->n_ptr;ir++) {
          reg1=0.;
          reg2=0.;
          reg3=0.;
	  for (iptr=A->pattern->ptr[ir]-PTR_OFFSET;iptr<A->pattern->ptr[ir+1]-PTR_OFFSET; iptr++) {
	       ic=3*(A->pattern->index[iptr]-INDEX_OFFSET);
	       reg1 += A->val[iptr*9  ]*in[ic] + A->val[iptr*9+3]*in[1+ic] + A->val[iptr*9+6]*in[2+ic];
	       reg2 += A->val[iptr*9+1]*in[ic] + A->val[iptr*9+4]*in[1+ic] + A->val[iptr*9+7]*in[2+ic];
	       reg3 += A->val[iptr*9+2]*in[ic] + A->val[iptr*9+5]*in[1+ic] + A->val[iptr*9+8]*in[2+ic];
	  }
	  out[  3*ir] += alpha * reg1;
	  out[1+3*ir] += alpha * reg2;
	  out[2+3*ir] += alpha * reg3;
	}
	break;
      case CSC:
        /* TODO: parallelize */
        #pragma omp single
	for (ic=0;ic< A->pattern->n_ptr;ic++) {
	  for (iptr=A->pattern->ptr[ic]-PTR_OFFSET;iptr<A->pattern->ptr[ic+1]-PTR_OFFSET; iptr++) {
	      ir=3*(A->pattern->index[iptr]-INDEX_OFFSET);
              out[  3*ir] += alpha * ( A->val[iptr*9  ]*in[ic] + A->val[iptr*9+3]*in[1+ic] + A->val[iptr*9+6]*in[2+ic] );
	      out[1+3*ir] += alpha * ( A->val[iptr*9+1]*in[ic] + A->val[iptr*9+4]*in[1+ic] + A->val[iptr*9+7]*in[2+ic] );
	      out[2+3*ir] += alpha * ( A->val[iptr*9+2]*in[ic] + A->val[iptr*9+5]*in[1+ic] + A->val[iptr*9+8]*in[2+ic] );
	  }
	}
      default:
	Paso_setError(TYPE_ERROR,"Unknown matrix type in MVM.");
      } /* switch A->type */
    } else {
      switch(A->type) {
      case CSR:
        #pragma omp for private(ir,iptr,irb,icb,irow,icol,reg) schedule(static)
	for (ir=0;ir< A->pattern->n_ptr;ir++) {
	  for (iptr=A->pattern->ptr[ir]-PTR_OFFSET;iptr<A->pattern->ptr[ir+1]-PTR_OFFSET; iptr++) {
	    for (irb=0;irb< A->row_block_size;irb++) {
	      irow=irb+A->row_block_size*ir;
              reg=0.;
	      for (icb=0;icb< A->col_block_size;icb++) {
		icol=icb+A->col_block_size*(A->pattern->index[iptr]-INDEX_OFFSET);
		reg += A->val[iptr*A->block_size+irb+A->row_block_size*icb] * in[icol];
	      }
	      out[irow] += alpha * reg;
	    }
	  }
	}
	break;
      case CSC:
        /* TODO: parallelize */
        #pragma omp single
	for (ic=0;ic< A->pattern->n_ptr;ic++) {
	  for (iptr=A->pattern->ptr[ic]-PTR_OFFSET;iptr<A->pattern->ptr[ic+1]-PTR_OFFSET; iptr++) {
	    for (irb=0;irb< A->row_block_size;irb++) {
	      irow=irb+A->row_block_size*(A->pattern->index[iptr]-INDEX_OFFSET);
	      for (icb=0;icb< A->col_block_size;icb++) {
		icol=icb+A->col_block_size*ic;
		out[irow] += alpha * A->val[iptr*A->block_size+irb+A->row_block_size*icb] * in[icol];
	      }
	    }
	  }
	}
      default:
	Paso_setError(TYPE_ERROR,"Unknown matrix type in MVM.");
      } /* switch A->type */
    }
  }
  return;
}

/*
 * $Log$
 * Revision 1.2  2005/09/15 03:44:39  jgs
 * Merge of development branch dev-02 back to main trunk on 2005-09-15
 *
 * Revision 1.1.2.1  2005/09/05 06:29:47  gross
 * These files have been extracted from finley to define a stand alone libray for iterative
 * linear solvers on the ALTIX. main entry through Paso_solve. this version compiles but
 * has not been tested yet.
 *
 *
 */
