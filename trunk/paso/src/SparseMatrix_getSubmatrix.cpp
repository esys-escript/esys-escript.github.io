
/*****************************************************************************
*
* Copyright (c) 2003-2014 by University of Queensland
* http://www.uq.edu.au
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
* Development until 2012 by Earth Systems Science Computational Center (ESSCC)
* Development 2012-2013 by School of Earth Sciences
* Development from 2014 by Centre for Geoscience Computing (GeoComp)
*
*****************************************************************************/


/****************************************************************************/

/* Paso: SparseMatrix */

/****************************************************************************/

/* Copyrights by ACcESS Australia 2003, 2004,2005 */
/* Author: Lutz Gross, l.gross@uq.edu.au */

/****************************************************************************/

#include "Paso.h"
#include "SparseMatrix.h"
#include "PasoUtil.h"

namespace paso {

/*****************************************************************************

    Returns the submatrix of A where rows are gathered by index row_list 
    and columns are selected by non-negative values of new_col_index.
    If new_col_index[i]>-1 new_col_index[i] gives the column of i in 
    the returned submatrix.
*/


SparseMatrix* SparseMatrix_getSubmatrix(const SparseMatrix* A,int n_row_sub,
                                        int n_col_sub, const index_t* row_list,
                                        const index_t* new_col_index)
{
    SparseMatrix* out=NULL;
    index_t index_offset=(A->type & MATRIX_FORMAT_OFFSET1 ? 1:0);
    int i,k,tmp,m,subpattern_row;
    int type=A->type;
    Esys_resetError();
    if (A->type & MATRIX_FORMAT_CSC) {
        Esys_setError(TYPE_ERROR, "SparseMatrix_getSubmatrix: gathering submatrices supports CSR matrix format only.");
    } else {
        Pattern_ptr sub_pattern(A->pattern->getSubpattern(n_row_sub, n_col_sub,
                                          row_list, new_col_index));
        if (Esys_noError()) {
            /* create the return object */
            out=SparseMatrix_alloc(type,sub_pattern,A->row_block_size,A->col_block_size,TRUE);
            if (Esys_noError()) {
                #pragma omp parallel for private(i,k,m,subpattern_row,tmp) schedule(static)
                for (i=0;i<n_row_sub;++i) {
                    subpattern_row=row_list[i];
                    for (k=A->pattern->ptr[subpattern_row]-index_offset;k<A->pattern->ptr[subpattern_row+1]-index_offset;++k) {
                        tmp=new_col_index[A->pattern->index[k]-index_offset];
                        if (tmp>-1) {
                            #pragma ivdep
                            for (m=out->pattern->ptr[i]-index_offset;m<out->pattern->ptr[i+1]-index_offset;++m) {
                                if (out->pattern->index[m]==tmp+index_offset) {
                                   Paso_copyShortDouble(A->block_size,&(A->val[k*A->block_size]),&(out->val[m*A->block_size]));
                                   break;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return out;
}

SparseMatrix* SparseMatrix_getBlock(const SparseMatrix* A, int blockid)
{
    dim_t blocksize=A->row_block_size,i;
    dim_t n=A->numRows;
    index_t iptr;
    SparseMatrix* out = SparseMatrix_alloc(A->type, A->pattern, 1, 1, 0);

    if (blocksize==1) {
        if (blockid==1) {
            #pragma omp parallel for private(i,iptr) schedule(static)
            for(i=0;i<n;++i) {
                for (iptr=A->pattern->ptr[i];iptr<A->pattern->ptr[i+1]; ++iptr) {
                    out->val[iptr]=A->val[iptr];
                }
            }
        } else {
            Esys_setError(VALUE_ERROR, "SparseMatrix_getBlock: Requested and actual block sizes do not match.");
        }
    } else if (blocksize==2) {
        if (blockid==1) {
            #pragma omp parallel for private(i,iptr) schedule(static)
            for(i=0;i<n;i++) {
                for (iptr=A->pattern->ptr[i];iptr<A->pattern->ptr[i+1]; ++iptr) {
                    out->val[iptr]=A->val[4*iptr];
                }
            }
        } else if (blockid==2) {
            #pragma omp parallel for private(i,iptr) schedule(static)
            for(i=0;i<n;i++) {
                for (iptr=A->pattern->ptr[i];iptr<A->pattern->ptr[i+1]; ++iptr) {
                    out->val[iptr]=A->val[4*iptr+3];
                }
            }
        } else {
            Esys_setError(VALUE_ERROR,"SparseMatrix_getBlock: Requested and actual block sizes do not match.");
        }
    } else if (blocksize==3) {
        if (blockid==1) {
            #pragma omp parallel for private(i,iptr) schedule(static)
            for(i=0;i<n;i++) {
                for (iptr=A->pattern->ptr[i];iptr<A->pattern->ptr[i+1]; ++iptr) {
                    out->val[iptr]=A->val[9*iptr];
                }
            }
        } else if (blockid==2) {
            #pragma omp parallel for private(i,iptr) schedule(static)
            for(i=0;i<n;i++) {
                for (iptr=A->pattern->ptr[i];iptr<A->pattern->ptr[i+1]; ++iptr) {
                    out->val[iptr]=A->val[9*iptr+4];
                }
            }
        } else if (blockid==3) {
            #pragma omp parallel for private(i,iptr) schedule(static)
            for(i=0;i<n;i++) {
                for (iptr=A->pattern->ptr[i];iptr<A->pattern->ptr[i+1]; ++iptr) {
                    out->val[iptr]=A->val[9*iptr+8];
                }
            }
        } else {
            Esys_setError(VALUE_ERROR,"SparseMatrix_getBlock: Requested and actual block sizes do not match.");
        }
    }

    return out;
}

} // namespace paso

