/* $Id$ */

/**************************************************************/

/* Finley: SystemMatrix */

/**************************************************************/

/* Copyrights by ACcESS Australia 2003, 2004,2005 */
/* Author: gross@access.edu.au */

/**************************************************************/

#include "Finley.h"
#include "System.h"
#include "Util.h"
#include "SystemPattern.h"


/**************************************************************

    returns the submatrix of A where rows are gathered by index row_list 
    and columns are selected by non-negative values of new_col_index.
    if new_col_index[i]>-1 new_col_index[i] gives the column of i in 
    the returned submatrix 

*/


Finley_SystemMatrix* Finley_SystemMatrix_getSubmatrix(Finley_SystemMatrix* A,int n_row_sub,index_t* row_list,index_t* new_col_index){
      Finley_SystemMatrixPattern* sub_pattern=NULL;
      Finley_SystemMatrix* out=NULL;
      Finley_ErrorCode=NO_ERROR;
      int i,k,tmp,m,subpattern_row;
      int type=A->type;
      if (type!=CSR) {
          Finley_ErrorCode=TYPE_ERROR;
          sprintf(Finley_ErrorMsg,"gathering submatrices supports CSR matrix format only.");
      } else {
         sub_pattern=Finley_SystemMatrixPattern_getSubpattern(A->pattern,n_row_sub,row_list,new_col_index);
         if (Finley_ErrorCode==NO_ERROR) {
            /* create the return object */
            out=Finley_SystemMatrix_alloc(type,sub_pattern,A->row_block_size,A->col_block_size);
            if (Finley_ErrorCode==NO_ERROR) {
                 #pragma omp parallel for private(i,k,m,subpattern_row,tmp) schedule(static)
                 for (i=0;i<n_row_sub;++i) {
                     subpattern_row=row_list[i];
                     for (k=A->pattern->ptr[subpattern_row]-PTR_OFFSET;k<A->pattern->ptr[subpattern_row+1]-PTR_OFFSET;++k) {
                        tmp=new_col_index[A->pattern->index[k]-INDEX_OFFSET];
                        if (tmp>-1) {
                           for (m=out->pattern->ptr[i]-PTR_OFFSET;m<out->pattern->ptr[i+1]-PTR_OFFSET;++m) {
                               if (out->pattern->index[m]==tmp+INDEX_OFFSET) {
                                   Finley_copyDouble(A->block_size,&(A->val[k*A->block_size]),&(out->val[m*A->block_size]));
                                   break;
                               }
                           }
                        }
                     }
                 }
            }
         }
         Finley_SystemMatrixPattern_dealloc(sub_pattern);
      }
      return out;
}
/*
 * $Log$
 * Revision 1.5  2005/09/01 03:31:36  jgs
 * Merge of development branch dev-02 back to main trunk on 2005-09-01
 *
 * Revision 1.4.2.1  2005/08/29 22:34:18  gross
 * memory leak in ILU fixed.
 *
 * Revision 1.4  2005/07/08 04:07:58  jgs
 * Merge of development branch back to main trunk on 2005-07-08
 *
 * Revision 1.1.2.3  2005/06/29 02:34:57  gross
 * some changes towards 64 integers in finley
 *
 * Revision 1.1.2.2  2005/03/02 23:35:06  gross
 * reimplementation of the ILU in Finley. block size>1 still needs some testing
 *
 * Revision 1.1.2.1  2005/02/18 02:27:31  gross
 * two function that will be used for a reimplementation of the ILU preconditioner
 *
 *
 */
