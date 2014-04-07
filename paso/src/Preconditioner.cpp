
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

/* Paso: preconditioner  set up                               */

/****************************************************************************/

/* Author: Lutz Gross, l.gross@uq.edu.au */

/****************************************************************************/

#include "Paso.h"
#include "SystemMatrix.h"
#include "PasoUtil.h"
#include "Preconditioner.h"


/*  free space */
void Paso_Preconditioner_free(Paso_Preconditioner* in)
{
    if (in!=NULL) {
      Paso_Preconditioner_Smoother_free(in->jacobi);
      Paso_Preconditioner_Smoother_free(in->gs);
      Paso_Preconditioner_AMG_Root_free(in->amg);
      /*********************************/
      Paso_Solver_ILU_free(in->ilu);
      Paso_Solver_RILU_free(in->rilu);
      /*********************************/
      
      delete in;
    }
}

Paso_Preconditioner* Paso_Preconditioner_alloc(paso::SystemMatrix_ptr A,
                                               Paso_Options* options)
{
    Paso_Preconditioner* prec = new Paso_Preconditioner;
    prec->type=UNKNOWN;
    prec->jacobi=NULL;
    prec->gs=NULL;
    prec->amg=NULL;
    
    /*********************************/ 
    prec->rilu=NULL;
    prec->ilu=NULL;
    /*********************************/
    
    if (options->verbose && options->use_local_preconditioner) printf("Paso: Apply preconditioner locally only.\n");

    switch (options->preconditioner) {
       default:
       case PASO_JACOBI:
          if (options->verbose) {
                            if (options->sweeps >0 ) {
                              printf("Paso_Preconditioner: Jacobi(%d) preconditioner is used.\n",options->sweeps);
                            } else {
                              printf("Paso_Preconditioner: Jacobi preconditioner is used.\n");
                            }
          }
          prec->jacobi=Paso_Preconditioner_Smoother_alloc(A, TRUE, options->use_local_preconditioner, options->verbose);
          prec->type=PASO_JACOBI;
          prec->sweeps=options->sweeps;
          break;
       case PASO_GS:
          if (options->verbose)  {
            if (options->sweeps >0 ) {
              printf("Paso_Preconditioner: Gauss-Seidel(%d) preconditioner is used.\n",options->sweeps);
            } else {
               printf("Paso_Preconditioner: Gauss-Seidel preconditioner is used.\n");
            }
          }
          prec->gs=Paso_Preconditioner_Smoother_alloc(A, FALSE, options->use_local_preconditioner, options->verbose);
          prec->type=PASO_GS;
          prec->sweeps=options->sweeps;
          break;
       case PASO_BOOMERAMG:
       case PASO_AMLI:
       case PASO_AMG:
          prec->amg=Paso_Preconditioner_AMG_Root_alloc(A, options);
          prec->type=PASO_AMG;
          break;

       /*********************************************************************/   
       case PASO_ILU0:
          if (options->verbose) printf("Paso_Preconditioner: ILU preconditioner is used.\n");
          prec->ilu=Paso_Solver_getILU(A->mainBlock,options->verbose);
          prec->type=PASO_ILU0;
          Esys_MPIInfo_noError(A->mpi_info);
          break;
       case PASO_RILU:
          if (options->verbose) printf("Paso_Preconditioner: RILU preconditioner is used.\n");
          prec->rilu=Paso_Solver_getRILU(A->mainBlock,options->verbose);
          Esys_MPIInfo_noError(A->mpi_info);
          prec->type=PASO_RILU;
          break;
       case PASO_NO_PRECONDITIONER:
          if (options->verbose) printf("Paso_Preconditioner: no preconditioner is applied.\n");
          prec->type=PASO_NO_PRECONDITIONER;
          break;
    }
    if (! Esys_noError() ){
         Paso_Preconditioner_free(prec);
        return NULL;
    } else {
        return prec;
    }
}

/* Applies the preconditioner. */
/* Has to be called within a parallel region. */
/* Barrier synchronization is performed before the evaluation to make sure that the input vector is available */
void Paso_Preconditioner_solve(Paso_Preconditioner* prec,
                               paso::SystemMatrix_ptr A, double* x, double* b)
{
    dim_t n=0;

    switch (prec->type) {
        default:
        case PASO_JACOBI:
           Paso_Preconditioner_Smoother_solve(A, prec->jacobi,x,b,prec->sweeps, FALSE);
           break;   
        case PASO_GS:
           Paso_Preconditioner_Smoother_solve(A, prec->gs,x,b,prec->sweeps, FALSE);
           break;
        case PASO_AMG:
           Paso_Preconditioner_AMG_Root_solve(A, prec->amg ,x,b);
           break;
           
        /*=========================================================*/   
        case PASO_ILU0:
           Paso_Solver_solveILU(A->mainBlock, prec->ilu,x,b);
           break;
        case PASO_RILU:
           Paso_Solver_solveRILU(prec->rilu,x,b);
           break;
        case PASO_NO_PRECONDITIONER:
            n = MIN(A->getTotalNumCols(), A->getTotalNumRows());
            Paso_Copy(n,x,b);
            break;

    }
}

