
/*******************************************************
*
* Copyright (c) 2003-2008 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/


/**********************************************************************/

/* Paso: Pattern: Paso_Pattern_coupling 

   searches for a maximal independent set MIS in the matrix pattern 
   vertices in the maximal independent set are marked in mis_marker
   nodes to be considered are marked by -1 on the input in mis_marker

*/
/**********************************************************************/

/* Copyrights by ACcESS Australia 2003,2004,2005              */
/* Author: artak@uq.edu.au                                */

/**************************************************************/

#include "PasoUtil.h"
#include "Pattern_coupling.h"


/***************************************************************/
 
#define IS_AVAILABLE -1
#define IS_IN_SET -3
#define IS_REMOVED -4

void Paso_Pattern_coup(Paso_SparseMatrix* A, index_t* mis_marker, double threshold) {

  index_t index_offset=(A->pattern->type & PATTERN_FORMAT_OFFSET1 ? 1:0);
  dim_t i,j;
  /*double threshold=0.05;*/
  index_t iptr,*index,*where_p,diagptr;
  bool_t fail;
  dim_t n=A->numRows;
  /*double sum;*/
  if (A->pattern->type & PATTERN_FORMAT_SYM) {
    Paso_setError(TYPE_ERROR,"Paso_Pattern_mis: symmetric matrix pattern is not supported yet");
    return;
  }
   
     /* is there any vertex available ?*/
     if (Paso_Util_isAny(n,mis_marker,IS_AVAILABLE)) {

            #pragma omp parallel for private(i,iptr,index,where_p,diagptr,j) schedule(static) 
            for (i=0;i<n;++i) {
              if (mis_marker[i]==IS_AVAILABLE) {
                 diagptr=A->pattern->ptr[i];
                 index=&(A->pattern->index[diagptr]);
                 where_p=(index_t*)bsearch(&i,
                                        index,
                                        A->pattern->ptr[i + 1]-A->pattern->ptr[i],
                                        sizeof(index_t),
                                        Paso_comparIndex);
                if (where_p==NULL) {
                    Paso_setError(VALUE_ERROR, "Paso_Solver_getAMG: main diagonal element missing.");
                } else {
                    diagptr+=(index_t)(where_p-index);
                }
                 for (iptr=A->pattern->ptr[i]-index_offset;iptr<A->pattern->ptr[i+1]-index_offset; ++iptr) {
                     j=A->pattern->index[iptr]-index_offset;
                     if (j!=i && ABS(A->val[iptr])>=threshold*ABS(A->val[diagptr])) {
                        mis_marker[j]=IS_REMOVED;
                       }
                 }
                }
            }
            
            #pragma omp parallel for private(i,iptr) schedule(static)
            for (i=0;i<n;++i)
                if(mis_marker[i]==IS_AVAILABLE)
                           mis_marker[i]=IS_IN_SET;
             
              #pragma omp parallel for private(i,iptr,index,where_p,diagptr) schedule(static)
              for (i=0;i<n;i++) {
               if (mis_marker[i]==IS_REMOVED) {
                 fail=FALSE;
                 diagptr=A->pattern->ptr[i];
                 index=&(A->pattern->index[diagptr]);
                 where_p=(index_t*)bsearch(&i,
                                        index,
                                        A->pattern->ptr[i + 1]-A->pattern->ptr[i],
                                        sizeof(index_t),
                                        Paso_comparIndex);
                if (where_p==NULL) {
                    Paso_setError(VALUE_ERROR, "Paso_Solver_getAMG: main diagonal element missing.");
                } else {
                    diagptr+=(index_t)(where_p-index);
                }
                 for (iptr=A->pattern->ptr[i]-index_offset;iptr<A->pattern->ptr[i+1]-index_offset; ++iptr) {
                     j=A->pattern->index[iptr]-index_offset;
                     if (mis_marker[j]==IS_IN_SET && (A->val[iptr]/A->val[diagptr])<-threshold){
                         fail=TRUE;
                         #ifndef _OPENMP  
                         break;
                         #endif
                     }
                 }
                 if(!fail) {
                    mis_marker[i]=IS_IN_SET;
                 }
               }
              }
              
        }
     /* swap to TRUE/FALSE in mis_marker */
     #pragma omp parallel for private(i) schedule(static)
     for (i=0;i<n;i++) mis_marker[i]=(mis_marker[i]==IS_IN_SET);
}

/*
 *
 * Return a strength of connection mask using the classical 
 * strength of connection measure by Ruge and Stuben.
 *
 * Specifically, an off-diagonal entry A[i.j] is a strong 
 * connection if:
 *  
 *      -A[i,j] >= theta * max( -A[i,k] )   where k != i
 * 
 * Otherwise, the connection is weak.
 *  
 */  
void Paso_Pattern_RS(Paso_SparseMatrix* A, index_t* mis_marker, double theta) 
{
  index_t index_offset=(A->pattern->type & PATTERN_FORMAT_OFFSET1 ? 1:0);
  dim_t i;
  index_t iptr;
  double threshold,min_offdiagonal;
  dim_t n=A->numRows;
  if (A->pattern->type & PATTERN_FORMAT_SYM) {
    Paso_setError(TYPE_ERROR,"Paso_Pattern_RS: symmetric matrix pattern is not supported yet");
    return;
  }

/* is there any vertex available ?*/
     if (Paso_Util_isAny(n,mis_marker,IS_AVAILABLE)) {

     #pragma omp parallel for private(i,iptr,min_offdiagonal,threshold) schedule(static) 
      for (i=0;i<n;++i) {
        min_offdiagonal = A->val[A->pattern->ptr[i]-index_offset];
        for (iptr=A->pattern->ptr[i]-index_offset;iptr<A->pattern->ptr[i+1]-index_offset; ++iptr) {
            if(A->pattern->index[iptr-index_offset] != i){
                min_offdiagonal = MIN(min_offdiagonal,A->val[iptr-index_offset]);
            }
        }

        threshold = theta*min_offdiagonal;
        mis_marker[i]=IS_IN_SET;
        #pragma omp parallel for private(iptr) schedule(static) 
        for (iptr=A->pattern->ptr[i]-index_offset;iptr<A->pattern->ptr[i+1]-index_offset; ++iptr) {
            if(A->val[iptr-index_offset] < threshold){
                    mis_marker[i]=IS_REMOVED;
                    #ifndef _OPENMP    
                     break;
                    #endif
            }
        }
      }
    }
     /* swap to TRUE/FALSE in mis_marker */
     #pragma omp parallel for private(i) schedule(static)
     for (i=0;i<n;i++) mis_marker[i]=(mis_marker[i]==IS_IN_SET);
}




void Paso_Pattern_Aggregiation(Paso_SparseMatrix* A, index_t* mis_marker, double theta) 
{
  index_t index_offset=(A->pattern->type & PATTERN_FORMAT_OFFSET1 ? 1:0);
  dim_t i,j;
  index_t iptr;
  double diag,eps_Aii,val;
  dim_t n=A->numRows;
  double* diags=MEMALLOC(n,double);
  
  if (A->pattern->type & PATTERN_FORMAT_SYM) {
    Paso_setError(TYPE_ERROR,"Paso_Pattern_RS: symmetric matrix pattern is not supported yet");
    return;
  }
    
   if (Paso_Util_isAny(n,mis_marker,IS_AVAILABLE)) {
    #pragma omp parallel for private(i,iptr,diag) schedule(static) 
      for (i=0;i<n;++i) {
        diag = 0;
        for (iptr=A->pattern->ptr[i]-index_offset;iptr<A->pattern->ptr[i+1]-index_offset; ++iptr) {
            if(A->pattern->index[iptr-index_offset] != i){
                diag+=A->val[iptr-index_offset];
            }
        }
        diags[i]=ABS(diag);
      }
    
    #pragma omp parallel for private(i,iptr,diag,j,val,eps_Aii) schedule(static) 
      for (i=0;i<n;++i) {
        eps_Aii = theta*theta*diags[i];
        mis_marker[i]=IS_REMOVED;

        for (iptr=A->pattern->ptr[i]-index_offset;iptr<A->pattern->ptr[i+1]-index_offset; ++iptr) {
            j=A->pattern->index[iptr-index_offset];
            val=A->val[iptr-index_offset];
            if(j!= i && val*val>=eps_Aii * diags[j]){
                mis_marker[i]=IS_IN_SET;
            }
        }
      }
   }
    /* swap to TRUE/FALSE in mis_marker */
     #pragma omp parallel for private(i) schedule(static)
     for (i=0;i<n;i++) mis_marker[i]=(mis_marker[i]==IS_IN_SET);
     
     MEMFREE(diags);
}


#undef IS_AVAILABLE 
#undef IS_IN_SET 
#undef IS_REMOVED
