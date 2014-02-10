
/* $Id$ */

/*******************************************************
 *
 *           Copyright 2003-2007 by ACceSS MNRF
 *       Copyright 2007 by University of Queensland
 *
 *                http://esscc.uq.edu.au
 *        Primary Business: Queensland, Australia
 *  Licensed under the Open Software License version 3.0
 *     http://www.opensource.org/licenses/osl-3.0.php
 *
 *******************************************************/

/**************************************************************/

/* Paso: interface to the SGI's direct solvers                */

/**************************************************************/

/* Copyrights by ACcESS Australia 2003,2004,2005 */
/* Author: gross@access.edu.au */

/**************************************************************/

#include "Paso.h"
#include "SystemMatrix.h"
#include "SCSL.h"
#ifdef SCSL
  #include <scsl_sparse.h>
  static int TokenList[]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
  static int Token[]={0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19};
  static int TokenSym[]={FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE,FALSE};
#endif

/**************************************************************/

/*  free any extra stuff possibly used by the SCSL library */

void Paso_SCSL_direct_free(Paso_SystemMatrix* A) {
#ifdef SCSL
      if (A->solver!=NULL) {
	int token=*(int*)(A->solver);
        TokenList[token]=0;
        if (TokenSym[token]) {
            DPSLDLT_Destroy(token);
        } else {
            DPSLDU_Destroy(token);
        }
        A->solver=NULL;
     }
#endif
}
/*  call the iterative solver: */

void Paso_SCSL_direct(Paso_SystemMatrix* A,
                               double* out,
                               double* in,
                               Paso_Options* options,
                               Paso_Performance* pp) {
#ifdef SCSL
  double time0;
  int token,l=sizeof(TokenList)/sizeof(int),reordering_method,method;
  long long non_zeros;
  double ops;

  if (A->type & MATRIX_FORMAT_SYM) {
      method=PASO_CHOLEVSKY;
  } else {
      method=PASO_DIRECT;
  }
  if (A->col_block_size!=1) {
      Paso_setError(TYPE_ERROR,"Paso_SCSL_direct: linear solver can only be applied to block size 1.");
  }
  if (method==PASO_CHOLEVSKY) {
      if (! (A->type & (MATRIX_FORMAT_CSC + MATRIX_FORMAT_SYM + MATRIX_FORMAT_BLK1)) )
          Paso_setError(TYPE_ERROR,"Paso_SCSL_direct: direct solver for symmetric matrices can only be applied to symmetric CSC format with block size 1 and index offset 0.");
  } else {
      if (! (A->type & (MATRIX_FORMAT_CSC + MATRIX_FORMAT_BLK1)) )
          Paso_setError(TYPE_ERROR,"Paso_SCSL_direct: direct solver can only be applied to CSC format with block size 1 and index offset 0.");
  }
  method=Paso_Options_getSolver(options->method,PASO_PASO,options->symmetric);
  Performance_startMonitor(pp,PERFORMANCE_ALL);
  if (Paso_noError()) {

     /* if no token has been assigned a free token must be found*/
     if (A->solver==NULL) {
        /* find the next available token */
       for(token=0;token<l && TokenList[token]!=0;token++);
        if (token==l) {
            Paso_setError(TYPE_ERROR,"Paso_SCSL_direct: limit of number of matrices reached.");
        } else {
          TokenList[token] = 1;
          TokenSym[token]=(method==PASO_CHOLEVSKY);
          A->solver=&Token[token];
          /* map the reordering method onto SCSL */
          switch (options->reordering) {
                case PASO_NO_REORDERING:
                     reordering_method=0;
                     break;
                case PASO_MINIMUM_FILL_IN:
                     reordering_method=1;
                     break;
                default:
                     reordering_method=2;
                     break;
          }
          time0=Paso_timer();
          if (TokenSym[token]) {
               /* DPSLDLT_Ordering(token,reordering_method); (does not work)*/
               DPSLDLT_Preprocess(token,A->mainBlock->numRows,A->mainBlock->pattern->ptr,A->mainBlock->pattern->index,&non_zeros,&ops); 
               DPSLDLT_Factor(token,A->mainBlock->numRows,A->mainBlock->pattern->ptr,A->mainBlock->pattern->index,A->mainBlock->val);
               if (options->verbose) printf("timing SCSL: Cholevsky factorization: %.4e sec (token = %d)\n",Paso_timer()-time0,token);
          } else {
               /* DPSLDU_Ordering(token,reordering_method);(does not work)*/
               DPSLDU_Preprocess(token,A->mainBlock->numRows,A->mainBlock->pattern->ptr,A->mainBlock->pattern->index,&non_zeros,&ops); 
               DPSLDU_Factor(token,A->mainBlock->numRows,A->mainBlock->pattern->ptr,A->mainBlock->pattern->index,A->mainBlock->val);
               if (options->verbose) printf("timing SCSL: LDU factorization: %.4e sec (token = %d)\n",Paso_timer()-time0,token);
          }
       }
    }
  }
  time0=Paso_timer();
  if (Paso_noError())  {
     token=*(int*)(A->solver);
     if (TokenSym[token]) {
        DPSLDLT_Solve(token,out,in);
     } else {
        DPSLDU_Solve(token,out,in);
     }
     if (options->verbose) printf("timing SCSL: solve: %.4e sec (token = %d)\n",Paso_timer()-time0,token);
   }
   Performance_stopMonitor(pp,PERFORMANCE_ALL);
#else
    Paso_setError(SYSTEM_ERROR,"Paso_SCSL_direct:SCSL is not avialble.");
#endif
}
/*
 * $Log$
 * Revision 1.2  2005/09/15 03:44:40  jgs
 * Merge of development branch dev-02 back to main trunk on 2005-09-15
 *
 * Revision 1.1.2.2  2005/09/07 00:59:08  gross
 * some inconsistent renaming fixed to make the linking work.
 *
 * Revision 1.1.2.1  2005/09/05 06:29:49  gross
 * These files have been extracted from finley to define a stand alone libray for iterative
 * linear solvers on the ALTIX. main entry through Paso_solve. this version compiles but
 * has not been tested yet.
 *
 *
 */