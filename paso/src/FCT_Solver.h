
/*****************************************************************************
*
* Copyright (c) 2003-2017 by The University of Queensland
* http://www.uq.edu.au
*
* Primary Business: Queensland, Australia
* Licensed under the Apache License, version 2.0
* http://www.apache.org/licenses/LICENSE-2.0
*
* Development until 2012 by Earth Systems Science Computational Center (ESSCC)
* Development 2012-2013 by School of Earth Sciences
* Development from 2014 by Centre for Geoscience Computing (GeoComp)
*
*****************************************************************************/

#ifndef __PASO_FCTSOLVER_H__
#define __PASO_FCTSOLVER_H__

#include "Transport.h"
#include "FluxLimiter.h"
#include "Solver.h"

namespace paso {

template <class T>  
PASO_DLL_API
struct FCT_Solver
{
    FCT_Solver(const_TransportProblem_ptr<T> tp, Options* options);

    ~FCT_Solver();

    SolverResult update(double* u, double* u_old, Options* options, Performance* pp);

    SolverResult updateNL(double* u, double* u_old, Options* options, Performance* pp);

    SolverResult updateLCN(double* u, double* u_old, Options* options, Performance* pp);

    void initialize(double dt, Options* options, Performance* pp);

    static double getSafeTimeStepSize(const_TransportProblem_ptr<T> tp);

    static void setLowOrderOperator(TransportProblem_ptr<T> tp);

    void setAntiDiffusionFlux_linearCN(SystemMatrix_ptr<T> flux_matrix);

    void setAntiDiffusionFlux_BE(SystemMatrix_ptr<T> flux_matrix);

    void setAntiDiffusionFlux_CN(SystemMatrix_ptr<T> flux_matrix);

    void setMuPaLu(double* out, const_Coupler_ptr<T> coupler, double a);

    inline double getTheta()
    {
        return method == PASO_BACKWARD_EULER ? 1. : 0.5;
    }

    const_TransportProblem_ptr<T> transportproblem;
    escript::JMPI mpi_info;
    FCT_FluxLimiter<T>* flux_limiter;
    index_t method;
    double omega;
    double dt;
    double* b;
    double* z;
    double* du;
    Coupler_ptr<T> u_coupler;
    Coupler_ptr<T> u_old_coupler; /* last time step */
};


} // namespace paso

#endif // __PASO_FCTSOLVER_H__

