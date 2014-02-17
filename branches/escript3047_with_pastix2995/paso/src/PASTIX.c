
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

/* Paso: interface to the PaStiX direct library */

/**************************************************************/

/* Copyrights by ACcESS Australia 2010 */
/* Author: l.gao@uq.edu.au */

/**************************************************************/

#include "Paso.h"
#include "PASTIX.h"
#ifdef _OPENMP
#include <omp.h>
#endif

/**************************************************************/

/*  free any extra stuff possibly used by the PASTIX library */
void Paso_PASTIX_free(Paso_SystemMatrix* A) {
#ifdef PASTIX
      index_t i;
      if (A->solver!=NULL) {
          pastix_data_t *pastix_data = (pastix_data_t *)(A->solver);
          pastix_int_t n = A->mainBlock->numCols;
          pastix_int_t *perm, *invp;
          pastix_int_t *loc2glob;
          loc2glob = MEMALLOC(n, pastix_int_t);
          if (A->mpi_info->size > 1)
              for (i=0; i<n; i++) loc2glob[i]=i;
          pastix_float_t *b;
          pastix_int_t iparm[IPARM_SIZE];
          double dparm[DPARM_SIZE];
          double *in;

          perm = MEMALLOC(n, pastix_int_t);
          invp = MEMALLOC(n, pastix_int_t);
          in   = MEMALLOC(n, double);

          for (i=0;i<IPARM_SIZE;++i) iparm[i]=0;
          for (i=0;i<DPARM_SIZE;++i) dparm[i]=0.;
          for (i=0;i<n;++i) in[i]=0.;

          iparm[IPARM_START_TASK] = API_TASK_CLEAN;
          iparm[IPARM_END_TASK] = API_TASK_CLEAN;

          dpastix(&pastix_data, A->mpi_info->comm, n,
                 A->mainBlock->pattern->ptr, A->mainBlock->pattern->index,
                 A->mainBlock->val, loc2glob, perm, invp, in, 1, 
                 iparm, dparm);
          MEMFREE(perm);
          MEMFREE(invp);
          MEMFREE(in);
          MEMFREE(loc2glob);
          A->solver=NULL;
          if (iparm[IPARM_ERROR_NUMBER] != NO_ERR) Paso_setError(TYPE_ERROR,"memory release in PASTIX library failed.");
     }
#endif
}

/*  call the solver: */
void Paso_PASTIX(Paso_SystemMatrix* A,
                          double* out,
                          double* in,
                          Paso_Options* options,
                          Paso_Performance* pp) {
#ifdef PASTIX 
     double time0;
     index_t i, m;
     dim_t node_num, offset;
     pastix_data_t  *pastix_data = NULL;
     pastix_int_t   n=A->mainBlock->numCols;
     pastix_int_t   *perm=NULL;
     pastix_int_t   *invp=NULL;
     pastix_int_t   iparm[IPARM_SIZE];
     pastix_int_t   *loc2glob=NULL;  /* Local to global column correspondance */
     pastix_int_t   *loc2glob2=NULL; /* Local to global column correspondance */
     pastix_int_t   *ptr=NULL;    /* Starting index of each column */
     pastix_int_t   *index=NULL;  /* Row of each element of the matrix */
     pastix_float_t *val=NULL;    /* Value of each element of the matrix */
     pastix_int_t   *ptr2=NULL;
     pastix_int_t   *index2=NULL;
     pastix_float_t *val2=NULL;
     double         *out_saved=NULL;      /* right-hand-side */
     double         *out2=NULL;
     double         dparm[DPARM_SIZE];

printf("CHP 0\n");

     if (! (A->type & (MATRIX_FORMAT_CSC + MATRIX_FORMAT_OFFSET1 + MATRIX_FORMAT_BLK1)) ) {
        Paso_setError(TYPE_ERROR,"Paso_PASTIX: PASTIX requires CSC format with index offset 1 and block size 1.");
        return;
     }
     options->converged=FALSE;
     Performance_startMonitor(pp,PERFORMANCE_ALL);

     loc2glob = MEMALLOC(n,pastix_int_t);
     perm = MEMALLOC(n, pastix_int_t);
     invp = MEMALLOC(n, pastix_int_t);

     offset = A->col_distribution->first_component[A->mpi_info->rank]+1;
     #pragma omp parallel for schedule(static) private(i)
     for (i=0; i<n; i++) loc2glob[i]=i+offset;
     #pragma omp parallel for schedule(static) private(i)
     for (i=0;i<IPARM_SIZE;++i) iparm[i]=0;
     #pragma omp parallel for schedule(static) private(i)
     for (i=0;i<DPARM_SIZE;++i) dparm[i]=0.;

     /* Set arrays "ptr", "index" and "val" of matrix */
     Paso_SystemMatrix_mergeMainAndCouple(A, &ptr, &index, &val);

     /*    Check Matrix format                  
      *    Matrix needs :
      *    - to be in fortran numbering (with offset 1)
      *    - to have only the lower triangular part in symmetric case
      *    - to have a graph with a symmetric structure in unsymmetric case
      */
     pastix_checkMatrix(A->mpi_info->comm, API_VERBOSE_YES,
                     ((A->type & MATRIX_FORMAT_SYM) ? API_SYM_YES:API_SYM_NO), 
                     API_YES, n, &ptr, &index, &val, &loc2glob, 1);

     /* copy the right-hand-side into the solution */
     out_saved = MEMALLOC(n, double);
     memcpy(out_saved, in, n*sizeof(double));

     /* initialize parameters to default values */
     iparm[IPARM_MODIFY_PARAMETER] = API_NO;
     dpastix(&pastix_data, A->mpi_info->comm, n,
             ptr, index, val, loc2glob, perm, invp, out_saved, 1, 
             iparm, dparm);

     /* set some iparm values (customized parameters)*/
     iparm[IPARM_VERBOSE] = API_VERBOSE_YES;
     iparm[IPARM_ITERMAX] = 2; /* maximum number of refinements */
     iparm[IPARM_MATRIX_VERIFICATION] = API_NO;
/*     iparm[IPARM_RHSD_CHECK] = API_NO; */
     iparm[IPARM_START_TASK]          = API_TASK_ORDERING;
     iparm[IPARM_END_TASK]            = API_TASK_BLEND;
#ifdef _OPENMP
     /* For thread binding on savanna, do we need to adjust the thread
        binding to suit the structure of savanna ice node??? 
        TO BE DONE */
/*   iparm[IPARM_BINDTHRD] = API_BIND_TAB
     pastix_setBind() */
     iparm[IPARM_THREAD_NBR] = omp_get_max_threads();
#else
     iparm[IPARM_THREAD_NBR] = 1;
#endif
     iparm[IPARM_RHS_MAKING] = API_RHS_B;
     if (A->type & MATRIX_FORMAT_SYM){
         iparm[IPARM_SYM] = API_SYM_YES;
         iparm[IPARM_FACTORIZATION] = API_FACT_LDLT;
     } else {
         iparm[IPARM_SYM] = API_SYM_NO;
         iparm[IPARM_FACTORIZATION] = API_FACT_LU;
     }

     /* start solving */
     time0=Paso_timer();
     dpastix (&pastix_data, A->mpi_info->comm, n,
              ptr, index, val, loc2glob, perm, invp, out_saved, 1, 
              iparm, dparm);

     node_num = pastix_getLocalNodeNbr(&pastix_data);
     loc2glob2 = MEMALLOC(node_num, pastix_int_t);

     pastix_getLocalNodeLst(&pastix_data, loc2glob2);

     if (EXIT_SUCCESS != cscd_redispatch(n, ptr, index, val, out_saved, 
                                         loc2glob, node_num, &ptr2, 
                                         &index2, &val2, &out2, loc2glob2, 
                                         A->mpi_info->comm)){
         Paso_setError(TYPE_ERROR,"Paso_PASTIX: CSCD redistribute fail.");
         return;
     }

     /* free part of memory allocation */
     MEMFREE(perm);
     MEMFREE(invp);
     MEMFREE(ptr);
     MEMFREE(index);
     MEMFREE(val);
     MEMFREE(out_saved);

     iparm[IPARM_START_TASK]          = API_TASK_NUMFACT;
     iparm[IPARM_END_TASK]            = API_TASK_CLEAN;

     dpastix(&pastix_data, A->mpi_info->comm, node_num,
             ptr2, index2, val2, loc2glob2, perm, invp, 
             out2, 1, iparm, dparm);

     /* copy the right-hand-side back into the solution */
     redispatch_rhs(node_num, out2, loc2glob2, n, out, loc2glob, 
                    A->mpi_info->size, A->mpi_info->rank, 
                    A->mpi_info->comm);

     options->time=Paso_timer()-time0;
     options->set_up_time=0;

     if (iparm[IPARM_ERROR_NUMBER] != NO_ERROR) {
         if (options->verbose) printf("PASTIX: solve failed.\n");
         Paso_setError(VALUE_ERROR,"pastix library failed.");
         Paso_PASTIX_free(A);
     } else {
         if (options->verbose) printf("PASTIX: solve completed.\n");
//         A->solver=NULL;
         options->converged=TRUE;
         options->residual_norm=0;
         options->num_iter=1;
         options->num_level=0;
         options->num_inner_iter=0;
         MEMFREE(loc2glob);
         MEMFREE(loc2glob2);
         MEMFREE(ptr2);
         MEMFREE(index2);
         MEMFREE(val2);
         MEMFREE(out2);
     }
     Performance_stopMonitor(pp,PERFORMANCE_ALL);
#else
     Paso_setError(SYSTEM_ERROR,"Paso_PASTIX: PASTIX is not avialble.");
#endif
}

/*
 * $Log$
 *
 */