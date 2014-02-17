
/*******************************************************
*
* Copyright (c) 2003-2012 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/


/**************************************************************/

/* Paso: AMG preconditioner  (local version)                  */

/**************************************************************/

/* Author: artak@uq.edu.au, l.gross@uq.edu.au l.gao@uq.edu.au */

/**************************************************************/

#define SHOW_TIMING FALSE
#define USE_TRANSPOSE TRUE
#define SMALL_PANEL TRUE

#include "Paso.h"
#include "Preconditioner.h"
#include "Options.h"
#include "PasoUtil.h"
#include "UMFPACK.h"
#include "MKL.h"

/**************************************************************/

/* free all memory used by AMG                                */

void Paso_Preconditioner_LocalAMG_free(Paso_Preconditioner_LocalAMG * in) {
     if (in!=NULL) {
	Paso_Preconditioner_LocalSmoother_free(in->Smoother);
	Paso_SparseMatrix_free(in->P);
	Paso_SparseMatrix_free(in->R);
	Paso_SparseMatrix_free(in->A_C);
	Paso_Preconditioner_LocalAMG_free(in->AMG_C);
	MEMFREE(in->r);
	MEMFREE(in->x_C);
	MEMFREE(in->b_C);

	
	MEMFREE(in);
     }
}

index_t Paso_Preconditioner_LocalAMG_getMaxLevel(const Paso_Preconditioner_LocalAMG * in) {
   if (in->AMG_C == NULL) {
      return in->level; 
   } else {
      return Paso_Preconditioner_LocalAMG_getMaxLevel(in->AMG_C);
   }
}

double Paso_Preconditioner_LocalAMG_getCoarseLevelSparsity(const Paso_Preconditioner_LocalAMG * in) {
      if (in->AMG_C == NULL) {
	 if (in->A_C == NULL) {
	    return 1.;
	 } else {
	    return Paso_SparseMatrix_getSparsity(in->A_C);
	 }
      } else {
	    return Paso_Preconditioner_LocalAMG_getCoarseLevelSparsity(in->AMG_C);
      }
}

dim_t Paso_Preconditioner_LocalAMG_getNumCoarseUnknwons(const Paso_Preconditioner_LocalAMG * in) {
   if (in->AMG_C == NULL) {
      if (in->A_C == NULL) {
	 return 0;
      } else {
	 return Paso_SparseMatrix_getTotalNumRows(in->A_C);
      }
   } else {
 	 return Paso_Preconditioner_LocalAMG_getNumCoarseUnknwons(in->AMG_C);
   }
}

/*****************************************************************

   Constructs AMG
   
******************************************************************/
Paso_Preconditioner_LocalAMG* Paso_Preconditioner_LocalAMG_alloc(Paso_SparseMatrix *A_p,dim_t level,Paso_Options* options) {

  Paso_Preconditioner_LocalAMG* out=NULL;
  bool_t verbose=options->verbose;
  
  Paso_SparseMatrix *Atemp=NULL, *A_C=NULL;
  const dim_t n=A_p->numRows;
  const dim_t n_block=A_p->row_block_size;
  index_t* F_marker=NULL, *counter=NULL, *mask_C=NULL, *rows_in_F=NULL, *S=NULL, *degree_S=NULL;
  dim_t n_F=0, n_C=0, i;
  double time0=0;
  const double theta = options->coarsening_threshold;
  const double tau = options->diagonal_dominance_threshold;
  const double sparsity=Paso_SparseMatrix_getSparsity(A_p);
  const dim_t total_n=Paso_SparseMatrix_getTotalNumRows(A_p);
  
  /*
  is the input matrix A suitable for coarsening
  
  */
  if ( (sparsity >= options->min_coarse_sparsity) || 
     (total_n <= options->min_coarse_matrix_size) || 
     (level > options->level_max) ) {
     
     if (verbose) { 
	/* 
	print stopping condition:
	- 'SPAR' = min_coarse_matrix_sparsity exceeded
	- 'SIZE' = min_coarse_matrix_size exceeded
	- 'LEVEL' = level_max exceeded
	*/
	printf("Paso_Preconditioner: AMG: termination of coarsening by "); 
	
	if (sparsity >= options->min_coarse_sparsity)
	   printf("SPAR");
	
	if (total_n <= options->min_coarse_matrix_size)
	   printf("SIZE");
	
	if (level > options->level_max)
	   printf("LEVEL");
	
	printf("\n");
	
	printf("Paso_Preconditioner: AMG level %d (limit = %d) stopped. Sparsity = %e (limit = %e), unknowns = %d (limit = %d)\n", 
	       level,  options->level_max, sparsity, options->min_coarse_sparsity, total_n, options->min_coarse_matrix_size);  
	       
     } 

     return NULL;
  } 
     /* Start Coarsening : */

     F_marker=TMPMEMALLOC(n,index_t);
     counter=TMPMEMALLOC(n,index_t);
     degree_S=TMPMEMALLOC(n, dim_t);
     S=TMPMEMALLOC(A_p->pattern->len, index_t);
     if ( !( Esys_checkPtr(F_marker) || Esys_checkPtr(counter) || Esys_checkPtr(degree_S) || Esys_checkPtr(S) ) ) {
	 /* 
	      set splitting of unknowns:
    	 */
	 time0=Esys_timer();
	 if (n_block>1) {
	       Paso_Preconditioner_LocalAMG_setStrongConnections_Block(A_p, degree_S, S, theta,tau);
	 } else {
	       Paso_Preconditioner_LocalAMG_setStrongConnections(A_p, degree_S, S, theta,tau);
	 }

	 Paso_Preconditioner_LocalAMG_RungeStuebenSearch(n, A_p->pattern->ptr, degree_S, S, F_marker, options->usePanel);

         /* in BoomerAMG if interpolation is used FF connectivity is required: */
         if (options->interpolation_method == PASO_CLASSIC_INTERPOLATION_WITH_FF_COUPLING) 
                             Paso_Preconditioner_LocalAMG_enforceFFConnectivity(n, A_p->pattern->ptr, degree_S, S, F_marker);  
	 options->coarsening_selection_time=Esys_timer()-time0 + MAX(0, options->coarsening_selection_time);
	 
	 if (Esys_noError() ) {
	    #pragma omp parallel for private(i) schedule(static)
	    for (i = 0; i < n; ++i) F_marker[i]=(F_marker[i] ==  PASO_AMG_IN_F);
	 
	    /*
	       count number of unknowns to be eliminated:
	    */
	    n_F=Paso_Util_cumsum_maskedTrue(n,counter, F_marker);
	    n_C=n-n_F;
	    if (verbose) printf("Paso_Preconditioner: AMG level %d: %d unknowns are flagged for elimination. %d left.\n",level,n_F,n-n_F);
	 
	    if ( n_F == 0 ) {  /* This is a nasty case. A direct solver should be used, return NULL */
	       out = NULL;
	    } else {
	       out=MEMALLOC(1,Paso_Preconditioner_LocalAMG);
	       if (! Esys_checkPtr(out)) {
		  out->level = level;
		  out->A_C = NULL; 
		  out->P = NULL;  
		  out->R = NULL; 	       
		  out->post_sweeps = options->post_sweeps;
		  out->pre_sweeps  = options->pre_sweeps;
		  out->r = NULL;
		  out->x_C = NULL;
		  out->b_C = NULL;
		  out->AMG_C = NULL;
		  out->Smoother=NULL;
	       }
	       mask_C=TMPMEMALLOC(n,index_t);
	       rows_in_F=TMPMEMALLOC(n_F,index_t);
	       Esys_checkPtr(mask_C);
	       Esys_checkPtr(rows_in_F);
	       if ( Esys_noError() ) {

		  out->Smoother = Paso_Preconditioner_LocalSmoother_alloc(A_p, (options->smoother == PASO_JACOBI), verbose);
	  
		  if (n_C != 0) {
			   /* if nothing has been removed we have a diagonal
                            * dominant matrix and we just run a few steps of
                            * the smoother */ 
   
			/* allocate helpers :*/
			out->x_C=MEMALLOC(n_block*n_C,double);
			out->b_C=MEMALLOC(n_block*n_C,double);
			out->r=MEMALLOC(n_block*n,double);
		     
			Esys_checkPtr(out->r);
			Esys_checkPtr(out->x_C);
			Esys_checkPtr(out->b_C);
		     
			if ( Esys_noError() ) {
			   /* creates index for F */
			   #pragma omp parallel private(i)
			   {
			      #pragma omp for schedule(static)
			      for (i = 0; i < n; ++i) {
				 if  (F_marker[i]) rows_in_F[counter[i]]=i;
			      }
			   }
			   /*  create mask of C nodes with value >-1 gives new id */
			   i=Paso_Util_cumsum_maskedFalse(n,counter, F_marker);

			   #pragma omp parallel for private(i) schedule(static)
			   for (i = 0; i < n; ++i) {
			      if  (F_marker[i]) {
				 mask_C[i]=-1;
			      } else {
				 mask_C[i]=counter[i];;
			      }
			   }
			   /*
			      get Prolongation :	 
			   */					
			   time0=Esys_timer();
			   out->P=Paso_Preconditioner_LocalAMG_getProlongation(A_p,A_p->pattern->ptr, degree_S,S,n_C,mask_C, options->interpolation_method);
			   if (SHOW_TIMING) printf("timing: level %d: getProlongation: %e\n",level, Esys_timer()-time0);
			}
			/*      
			   construct Restriction operator as transposed of Prolongation operator: 
			*/
			if ( Esys_noError()) {
			   time0=Esys_timer();
			   out->R=Paso_SparseMatrix_getTranspose(out->P);
			   if (SHOW_TIMING) printf("timing: level %d: Paso_SparseMatrix_getTranspose: %e\n",level,Esys_timer()-time0);
			}		
			/* 
			construct coarse level matrix:
			*/
			if ( Esys_noError()) {
			   time0=Esys_timer();
			   if (USE_TRANSPOSE)
			     Atemp=Paso_SparseMatrix_MatrixMatrixTranspose(A_p,out->P,out->R);
			   else
			     Atemp=Paso_SparseMatrix_MatrixMatrix(A_p,out->P);
			   A_C=Paso_SparseMatrix_MatrixMatrix(out->R,Atemp);
			   Paso_SparseMatrix_free(Atemp);
			   if (SHOW_TIMING) printf("timing: level %d : construct coarse matrix: %e\n",level,Esys_timer()-time0);			
			}

			
			/*
			   construct coarser level:
			   
			*/
			if ( Esys_noError()) {
			   out->AMG_C=Paso_Preconditioner_LocalAMG_alloc(A_C,level+1,options);
			}
			if ( Esys_noError()) {
			   if ( out->AMG_C == NULL ) { 
			      out->reordering = options->reordering;
			      out->refinements = options->coarse_matrix_refinements;
			      /* no coarse level matrix has been constructed. Use direct solver */
			      #ifdef MKL
				    out->A_C=Paso_SparseMatrix_unroll(MATRIX_FORMAT_BLK1 + MATRIX_FORMAT_OFFSET1, A_C);
				    Paso_SparseMatrix_free(A_C);
				    out->A_C->solver_package = PASO_MKL;
				    if (verbose) printf("Paso_Preconditioner: AMG: use MKL direct solver on the coarsest level (number of unknowns = %d).\n",n_C*n_block); 
			      #else
				    #ifdef UMFPACK
				       out->A_C=Paso_SparseMatrix_unroll(MATRIX_FORMAT_BLK1 + MATRIX_FORMAT_CSC, A_C); 
				       Paso_SparseMatrix_free(A_C);
				       out->A_C->solver_package = PASO_UMFPACK;
				       if (verbose) printf("Paso_Preconditioner: AMG: use UMFPACK direct solver on the coarsest level (number of unknowns = %d).\n",n_C*n_block); 
				    #else
				       out->A_C=A_C;
				       out->A_C->solver_p=Paso_Preconditioner_LocalSmoother_alloc(out->A_C, (options->smoother == PASO_JACOBI), verbose);
				       out->A_C->solver_package = PASO_SMOOTHER;
				       if (verbose) printf("Paso_Preconditioner: AMG: use smoother on the coarsest level (number of unknowns = %d).\n",n_C*n_block);
				    #endif
			      #endif
			   } else {
			      /* finally we set some helpers for the solver step */
			      out->A_C=A_C;
			   }
			}		  
		  }
	       }
	       TMPMEMFREE(mask_C);
	       TMPMEMFREE(rows_in_F);
	    }
	 }
  }
  TMPMEMFREE(counter);
  TMPMEMFREE(F_marker);
  TMPMEMFREE(degree_S);
  TMPMEMFREE(S);

  if (Esys_noError()) {
     return out;
  } else  {
     Paso_Preconditioner_LocalAMG_free(out);
     return NULL;
  }
}


void Paso_Preconditioner_LocalAMG_solve(Paso_SparseMatrix* A, Paso_Preconditioner_LocalAMG * amg, double * x, double * b) {
     const dim_t n = A->numRows * A->row_block_size;
     double time0=0;
     const dim_t post_sweeps=amg->post_sweeps;
     const dim_t pre_sweeps=amg->pre_sweeps;

     /* presmoothing */
     time0=Esys_timer();
     Paso_Preconditioner_LocalSmoother_solve(A, amg->Smoother, x, b, pre_sweeps, FALSE); 
     time0=Esys_timer()-time0;
     if (SHOW_TIMING) printf("timing: level %d: Presmoothing: %e\n",amg->level, time0); 
     /* end of presmoothing */
	
     time0=Esys_timer();
     Paso_Copy(n, amg->r, b);                            /*  r <- b */
     Paso_SparseMatrix_MatrixVector_CSR_OFFSET0(-1.,A,x,1.,amg->r); /*r=r-Ax*/
     Paso_SparseMatrix_MatrixVector_CSR_OFFSET0_DIAG(1.,amg->R,amg->r,0.,amg->b_C);  /* b_c = R*r  */
     time0=Esys_timer()-time0;
     /* coarse level solve */
     if ( amg->AMG_C == NULL) {
	    time0=Esys_timer();
	    /*  A_C is the coarsest level */
	    switch (amg->A_C->solver_package) {
	       case (PASO_MKL):
		  Paso_MKL(amg->A_C, amg->x_C,amg->b_C, amg->reordering, amg->refinements, SHOW_TIMING);
		  break;
	       case (PASO_UMFPACK):
		  Paso_UMFPACK(amg->A_C, amg->x_C,amg->b_C, amg->refinements, SHOW_TIMING);
		  break;
	       case (PASO_SMOOTHER):
		  Paso_Preconditioner_LocalSmoother_solve(amg->A_C, amg->A_C->solver_p,amg->x_C,amg->b_C,pre_sweeps+post_sweeps, FALSE);
		  break;
	    }
	    if (SHOW_TIMING) printf("timing: level %d: DIRECT SOLVER: %e\n",amg->level,Esys_timer()-time0);
     } else {
	    Paso_Preconditioner_LocalAMG_solve(amg->A_C, amg->AMG_C,amg->x_C,amg->b_C); /* x_C=AMG(b_C)     */
     }  
     time0=time0+Esys_timer();
     Paso_SparseMatrix_MatrixVector_CSR_OFFSET0_DIAG(1.,amg->P,amg->x_C,1.,x); /* x = x + P*x_c */    
	
     /*postsmoothing*/
    
     /*solve Ax=b with initial guess x */
     time0=Esys_timer();
     Paso_Preconditioner_LocalSmoother_solve(A, amg->Smoother, x, b, post_sweeps, TRUE); 
     time0=Esys_timer()-time0;
     if (SHOW_TIMING) printf("timing: level %d: Postsmoothing: %e\n",amg->level,time0);
     /*end of postsmoothing*/
     return;
}

/* theta = threshold for strong connections */
/* tau = threshold for diagonal dominance */

/*S_i={j \in N_i; i strongly coupled to j}

in the sense that |A_{ij}| >= theta * max_k |A_{ik}| 
*/

void Paso_Preconditioner_LocalAMG_setStrongConnections(Paso_SparseMatrix* A, 
					  dim_t *degree_S, index_t *S,
					  const double theta, const double tau)
{
   const dim_t n=A->numRows;
   index_t iptr, i;


      #pragma omp parallel for private(i,iptr) schedule(static)
      for (i=0;i<n;++i) {        
	 register double max_offdiagonal = 0.;
	 register double sum_row=0;
	 register double main_row=0;
	 #pragma ivdep
	 for (iptr=A->pattern->ptr[i];iptr<A->pattern->ptr[i+1]; ++iptr) {
	    register index_t j=A->pattern->index[iptr];
	    register double fnorm=ABS(A->val[iptr]);
	    
	    if( j != i) {
	       max_offdiagonal = MAX(max_offdiagonal,fnorm);
	       sum_row+=fnorm;
	    } else {
	       main_row=fnorm;
	    }
	 }
	 {
	    const double threshold = theta*max_offdiagonal;
	    register dim_t kdeg=0;
	    if (tau*main_row < sum_row) { /* no diagonal dominance */
	       #pragma ivdep
	       for (iptr=A->pattern->ptr[i];iptr<A->pattern->ptr[i+1]; ++iptr) {
	          register index_t j=A->pattern->index[iptr];
	          if(ABS(A->val[iptr])>threshold && i!=j) {
		     S[A->pattern->ptr[i]+kdeg] = j;
		     kdeg++;
	          }
	       }
            }
	    degree_S[i]=kdeg;
         }
      }

}

/* theta = threshold for strong connections */
/* tau = threshold for diagonal dominance */ 
/*S_i={j \in N_i; i strongly coupled to j}

in the sense that |A_{ij}|_F >= theta * max_k |A_{ik}|_F 
*/
void Paso_Preconditioner_LocalAMG_setStrongConnections_Block(Paso_SparseMatrix* A, 
							dim_t *degree_S, index_t *S,
							const double theta, const double tau)

{
   const dim_t n_block=A->row_block_size;
   const dim_t n=A->numRows;
   index_t iptr, i, bi;
   
   
      #pragma omp parallel private(i, iptr,  bi)
      {
	 dim_t max_deg=0; /* this is local on each thread */
	 double* rtmp=NULL;

	 #pragma omp for schedule(static)
	 for (i=0;i<n;++i) max_deg=MAX(max_deg, A->pattern->ptr[i+1]-A->pattern->ptr[i]);
      
	 rtmp=TMPMEMALLOC(max_deg, double);
      
	 #pragma omp for schedule(static)
	 for (i=0;i<n;++i) {
	 
	    register double max_offdiagonal = 0.;
	    register double sum_row=0;
	    register double main_row=0;

	    for (iptr=A->pattern->ptr[i];iptr<A->pattern->ptr[i+1]; ++iptr) {
	       register index_t j=A->pattern->index[iptr];
	       register double fnorm=0;
	       #pragma ivdep
	       for(bi=0;bi<n_block*n_block;++bi) {
	           register double rtmp2 = A->val[iptr*n_block*n_block+bi];
                   fnorm+=rtmp2*rtmp2;
               }
	       fnorm=sqrt(fnorm);

	       rtmp[iptr-A->pattern->ptr[i]]=fnorm;
	       if( j != i) {
		  max_offdiagonal = MAX(max_offdiagonal,fnorm);
		  sum_row+=fnorm;
	       } else {
		  main_row=fnorm;
	       }
	    }
            {
	       const double threshold = theta*max_offdiagonal;
	       register dim_t kdeg=0;
	       if (tau*main_row < sum_row) { /* no diagonal dominance */
	          #pragma ivdep
	          for (iptr=A->pattern->ptr[i];iptr<A->pattern->ptr[i+1]; ++iptr) {
		     register index_t j=A->pattern->index[iptr];
		     if(rtmp[iptr-A->pattern->ptr[i]] > threshold && i!=j) {
		        S[A->pattern->ptr[i]+kdeg] = j;
		        kdeg++;
		     }
	          }
	       }
	       degree_S[i]=kdeg;
            }
	 }      
	 TMPMEMFREE(rtmp);
      } /* end of parallel region */
 
}   

/* the Runge Stueben coarsening algorithm: */
void Paso_Preconditioner_LocalAMG_RungeStuebenSearch(const dim_t n, const index_t* offset_S,
						const dim_t* degree_S, const index_t* S, 
						index_t*split_marker, const bool_t usePanel)
{
   
   index_t *lambda=NULL, *ST=NULL, *notInPanel=NULL, *panel=NULL, lambda_max, lambda_k;
   dim_t i,k, p, q, *degree_ST=NULL, len_panel, len_panel_new;
   register index_t j, itmp;
   
   if (n<=0) return; /* make sure that the return of Paso_Util_arg_max is not pointing to nirvana */
   
   lambda=TMPMEMALLOC(n, index_t); Esys_checkPtr(lambda);
   degree_ST=TMPMEMALLOC(n, dim_t); Esys_checkPtr(degree_ST);
   ST=TMPMEMALLOC(offset_S[n], index_t);  Esys_checkPtr(ST);
   if (usePanel) {
      if (!SMALL_PANEL) {
	 notInPanel=TMPMEMALLOC(n, bool_t); Esys_checkPtr(notInPanel);
      }
      panel=TMPMEMALLOC(n, index_t); Esys_checkPtr(panel);
   }
   
   
   
   if (Esys_noError() ) {
      /* initialize split_marker: */
      /* Those unknowns which are not influenced go into F, the rest is available for F or C */
      #pragma omp parallel for private(i) schedule(static)
      for (i=0;i<n;++i) {
	 degree_ST[i]=0;
	 if (degree_S[i]>0) {
	    lambda[i]=0;
	    split_marker[i]=PASO_AMG_UNDECIDED;
	 } else {
	    split_marker[i]=PASO_AMG_IN_F;
	    lambda[i]=-1;
	 } 
      }
      /* create transpose :*/
      for (i=0;i<n;++i) {
	    for (p=0; p<degree_S[i]; ++p) {
	       j=S[offset_S[i]+p];
	       ST[offset_S[j]+degree_ST[j]]=i;
	       degree_ST[j]++;
	    }
      }

      /* lambda[i] = |undecided k in ST[i]| + 2 * |F-unknown in ST[i]| */
      #pragma omp parallel for private(i, j, p, itmp) schedule(static)
      for (i=0;i<n;++i) {
	 if (split_marker[i]==PASO_AMG_UNDECIDED) {
	    itmp=lambda[i];
	    for (p=0; p<degree_ST[i]; ++p) {
	       j=ST[offset_S[i]+p];
	       if (split_marker[j]==PASO_AMG_UNDECIDED) {
		  itmp++;
	       } else {  /* at this point there are no C points */
		  itmp+=2;
	       }
	    }
	    lambda[i]=itmp;
	 }
      }
      if (usePanel && !SMALL_PANEL) {
	 #pragma omp parallel for private(i) schedule(static)
	 for (i=0;i<n;++i) notInPanel[i]=TRUE;
      }
      /* start search :*/
      i=Paso_Util_arg_max(n,lambda); 
      while (lambda[i]>-1) { /* is there any undecided unknown? */
         if (SMALL_PANEL) {
            do {
               len_panel=0;
               /* the unknown i is moved to C */
               split_marker[i]=PASO_AMG_IN_C;
               lambda[i]=-1;  /* lambda from unavailable unknowns is set to -1 */

               /* all undecided unknowns strongly coupled to i are moved to F */
               for (p=0; p<degree_ST[i]; ++p) {
                  j=ST[offset_S[i]+p];

                  if (split_marker[j]==PASO_AMG_UNDECIDED) {

                     split_marker[j]=PASO_AMG_IN_F;
                     lambda[j]=-1;
                     for (q=0; q<degree_S[j]; ++q) {
                        k=S[offset_S[j]+q];
                        if (split_marker[k]==PASO_AMG_UNDECIDED) {
                           lambda[k]++;
                           panel[len_panel]=k;
                           len_panel++;

                        } 
                     }

                  }
               }
               for (p=0; p<degree_S[i]; ++p) {
                  j=S[offset_S[i]+p];
                  if (split_marker[j]==PASO_AMG_UNDECIDED) {
                     lambda[j]--;
                     panel[len_panel]=j;
                     len_panel++;
                  }
               }

               lambda_max=-1;
               for (q=0; q<len_panel; q++) {
                  k = panel[q];
                  j = lambda[k];
                  if (lambda_max < j) {
                    lambda_max = j;
                    i = k;
                  }
               } 
            } while (len_panel>0);
	 } else if (usePanel) {
	    len_panel=0;
	    do {
	       /* the unknown i is moved to C */
	       split_marker[i]=PASO_AMG_IN_C;
	       lambda[i]=-1;  /* lambda from unavailable unknowns is set to -1 */
	       
	       /* all undecided unknowns strongly coupled to i are moved to F */
	       for (p=0; p<degree_ST[i]; ++p) {
		  j=ST[offset_S[i]+p];
		  
		  if (split_marker[j]==PASO_AMG_UNDECIDED) {
		     
		     split_marker[j]=PASO_AMG_IN_F;
		     lambda[j]=-1;
		     
		     for (q=0; q<degree_S[j]; ++q) {
			k=S[offset_S[j]+q];
			if (split_marker[k]==PASO_AMG_UNDECIDED) {
			   lambda[k]++;
			   if (notInPanel[k]) { 
			      notInPanel[k]=FALSE; 
			      panel[len_panel]=k;
			      len_panel++; 
			   }

			}	 /* the unknown i is moved to C */
			split_marker[i]=PASO_AMG_IN_C;
			lambda[i]=-1;  /* lambda from unavailable unknowns is set to -1 */
		     }
		     
		  }
	       }
	       for (p=0; p<degree_S[i]; ++p) {
		  j=S[offset_S[i]+p];
		  if (split_marker[j]==PASO_AMG_UNDECIDED) {
		     lambda[j]--;
		     if (notInPanel[j]) { 
			notInPanel[j]=FALSE; 
			panel[len_panel]=j;
			len_panel++; 
		     }
		  }
	       }

	       /* consolidate panel */
	       /* remove lambda[q]=-1 */
	       lambda_max=-1;
	       i=-1;
	       len_panel_new=0;
	       for (q=0; q<len_panel; q++) {
		     k=panel[q];
		     lambda_k=lambda[k];
		     if (split_marker[k]==PASO_AMG_UNDECIDED) {
			panel[len_panel_new]=k;
			len_panel_new++;

			if (lambda_max == lambda_k) {
			   if (k<i) i=k;
			} else if (lambda_max < lambda_k) {
			   lambda_max =lambda_k;
			   i=k;
			}
		     }
	       }
	       len_panel=len_panel_new;
	    } while (len_panel>0);    
	 } else {
	    /* the unknown i is moved to C */
	    split_marker[i]=PASO_AMG_IN_C;
	    lambda[i]=-1;  /* lambda from unavailable unknowns is set to -1 */
	    
	    /* all undecided unknowns strongly coupled to i are moved to F */
	    for (p=0; p<degree_ST[i]; ++p) {
	       j=ST[offset_S[i]+p];
	       if (split_marker[j]==PASO_AMG_UNDECIDED) {
	    
		  split_marker[j]=PASO_AMG_IN_F;
		  lambda[j]=-1;
	    
		  for (q=0; q<degree_S[j]; ++q) {
		     k=S[offset_S[j]+q];
		     if (split_marker[k]==PASO_AMG_UNDECIDED) lambda[k]++;
		  }

	       }
	    }
	    for (p=0; p<degree_S[i]; ++p) {
	       j=S[offset_S[i]+p];
	       if(split_marker[j]==PASO_AMG_UNDECIDED) lambda[j]--;
	    }
	    
	 }
	 i=Paso_Util_arg_max(n,lambda);
      }
          
   }
   TMPMEMFREE(lambda);
   TMPMEMFREE(ST);
   TMPMEMFREE(degree_ST);
   if (usePanel) {
     TMPMEMFREE(panel);
     if (!SMALL_PANEL) TMPMEMFREE(notInPanel);
   }
}

/* ensures that two F nodes are connected via a C node :*/
void Paso_Preconditioner_LocalAMG_enforceFFConnectivity(const dim_t n, const index_t* offset_S,
						const dim_t* degree_S, const index_t* S, 
						index_t*split_marker)
{
      dim_t i, p, q;

      /* now we make sure that two (strongly) connected F nodes are (strongly) connected via a C node. */
      for (i=0;i<n;++i) {
            if ( (split_marker[i]==PASO_AMG_IN_F) && (degree_S[i]>0) ) {
	       for (p=0; p<degree_S[i]; ++p) {
                  register index_t j=S[offset_S[i]+p];
                  if ( (split_marker[j]==PASO_AMG_IN_F)  && (degree_S[j]>0) )  {
                      /* i and j are now two F nodes which are strongly connected */
                      /* is there a C node they share ? */
                      register index_t sharing=-1;
	              for (q=0; q<degree_S[i]; ++q) {
                         index_t k=S[offset_S[i]+q];
                         if (split_marker[k]==PASO_AMG_IN_C) {
                            register index_t* where_k=(index_t*)bsearch(&k, &(S[offset_S[j]]), degree_S[j], sizeof(index_t), Paso_comparIndex);
                            if (where_k != NULL) {
                               sharing=k;
                               break;
                            }
                         }
                      }
                      if (sharing<0) {
                           if (i<j) {
                              split_marker[j]=PASO_AMG_IN_C; 
                           } else {
                              split_marker[i]=PASO_AMG_IN_C; 
                              break;  /* no point to look any further as i is now a C node */
                           }
                      }
                  }
               }
            }
       }
}
