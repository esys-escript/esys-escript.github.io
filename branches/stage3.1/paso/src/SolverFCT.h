
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


#ifndef INC_SOLVERFCT
#define INC_SOLVERFCT

#define DT_FACTOR_MAX 1000.

#include "SystemMatrix.h"
#include "Options.h"
#include "performance.h"

typedef struct Paso_FCTransportProblem {

    double theta;
    double dt_max;
    bool_t valid_matrices;
    double dt_factor; /* = MIN(1/(1-theta),DT_FACTOR_MAX) */

    Paso_SystemMatrix * transport_matrix;
    Paso_SystemMatrix * mass_matrix;

    double constraint_factor;
    double* constraint_weights;

    double* u;
    Paso_Coupler* u_coupler;

    index_t *main_iptr;
    Paso_SystemMatrix * iteration_matrix;
    double* main_diagonal_low_order_transport_matrix;
    double* lumped_mass_matrix;

    Paso_MPIInfo *mpi_info;
    dim_t reference_counter;

} Paso_FCTransportProblem;



PASO_DLL_API
Paso_FCTransportProblem* Paso_FCTransportProblem_getReference(Paso_FCTransportProblem* in);

PASO_DLL_API
Paso_FCTransportProblem* Paso_FCTransportProblem_alloc(double theta, Paso_SystemMatrixPattern *pattern, int block_size);

PASO_DLL_API
dim_t Paso_FCTransportProblem_getBlockSize(const Paso_FCTransportProblem* in);

PASO_DLL_API
double Paso_FCTransportProblem_getSafeTimeStepSize(Paso_FCTransportProblem* in);

PASO_DLL_API
void Paso_FCTransportProblem_setLowOrderOperator(Paso_FCTransportProblem * fc);

PASO_DLL_API
Paso_SystemMatrix* Paso_FCTransportProblem_borrowTransportMatrix(Paso_FCTransportProblem* in);

PASO_DLL_API
Paso_SystemMatrix* Paso_FCTransportProblem_borrowMassMatrix(Paso_FCTransportProblem* in);

PASO_DLL_API
double* Paso_FCTransportProblem_borrowLumpedMassMatrix(Paso_FCTransportProblem* in);

PASO_DLL_API
dim_t Paso_FCTransportProblem_getTotalNumRows(Paso_FCTransportProblem* in);

PASO_DLL_API
void Paso_FCTransportProblem_free(Paso_FCTransportProblem* in);

PASO_DLL_API
void Paso_FCTransportProblem_reset(Paso_FCTransportProblem* in);

PASO_DLL_API
void Paso_SolverFCT_solve(Paso_FCTransportProblem* fctp, double* u, double dt, double* source, Paso_Options* options);

PASO_DLL_API
void Paso_FCTransportProblem_checkinSolution(Paso_FCTransportProblem* in, double* u);

PASO_DLL_API
void Paso_FCTransportProblem_applyPreAntiDiffusionCorrection(Paso_SystemMatrix *f,const Paso_Coupler* u_coupler);

PASO_DLL_API
void Paso_SolverFCT_setQs(const Paso_Coupler* u_coupler,double* QN, double* QP, const Paso_SystemMatrix *L);

PASO_DLL_API
void Paso_FCTransportProblem_setAntiDiffusionFlux(const double dt, const Paso_FCTransportProblem * fc, Paso_SystemMatrix *flux_matrix, const Paso_Coupler* u_coupler);

PASO_DLL_API
void Paso_FCTransportProblem_setRs(const Paso_SystemMatrix *f,const double* lumped_mass_matrix,const Paso_Coupler* QN,const Paso_Coupler* QP,double* RN,double* RP);

PASO_DLL_API
void Paso_FCTransportProblem_addCorrectedFluxes(double* f,const Paso_SystemMatrix *flux_matrix,const Paso_Coupler* RN,const Paso_Coupler* RP);


PASO_DLL_API
void Paso_SolverFCT_setMuPaLuPbQ(double* out, const double* M, const Paso_Coupler* u_coupler, const double a, const Paso_SystemMatrix *L, const double b, const double* Q);

PASO_DLL_API
Paso_Connector* Paso_FCTransportProblem_borrowConnector(const Paso_FCTransportProblem* in);

PASO_DLL_API
void Paso_FCT_setUp(Paso_FCTransportProblem* fctp, const double dt, const double *sourceN, const double *sourceP, double* b, double* uTilde,
                     Paso_Coupler* uTilde_coupler, double *QN, Paso_Coupler* QN_coupler, double *QP, Paso_Coupler* QP_coupler,
                     Paso_Options* options, Paso_Performance* pp);

PASO_DLL_API
index_t Paso_FCTransportProblem_getTypeId(const index_t solver,const index_t preconditioner, const index_t package,const  bool_t symmetry, Paso_MPIInfo *mpi_info);


PASO_DLL_API
void Paso_FCTransportProblem_insertConstraint(Paso_FCTransportProblem* fctp,  const double* r,  double* source);


PASO_DLL_API
void Paso_FCTransportProblem_setUpConstraint(Paso_FCTransportProblem* fctp,  const double* q, const double factor);

#endif /* #ifndef INC_SOLVERFCT */