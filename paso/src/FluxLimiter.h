
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

#ifndef __PASO_FLUXLIMITER_H__
#define __PASO_FLUXLIMITER_H__

#include "Transport.h"

namespace paso {


PASO_DLL_API
struct FCT_FluxLimiter
{
    FCT_FluxLimiter(const_TransportProblem_ptr tp);
    ~FCT_FluxLimiter();

    inline dim_t getTotalNumRows() const
    {
        return antidiffusive_fluxes->getTotalNumRows();
    }

    inline SystemMatrixPattern_ptr getFluxPattern() const
    {
        return antidiffusive_fluxes->pattern;
    }

    void setU_tilde(const double* Mu_tilde);
    void addLimitedFluxes_Start();
    void addLimitedFluxes_Complete(double* b);

    SystemMatrix_ptr antidiffusive_fluxes;
    esysUtils::JMPI mpi_info;
    double dt;
    double* u_tilde;
    double* MQ;  // (M_C* Q_min, M_C* Q_max)
    double* R;   // (R-, R+)
    //Coupler_ptr MQ_coupler;
    Coupler_ptr R_coupler;
    Coupler_ptr u_tilde_coupler;
    double* borrowed_lumped_mass_matrix; // borrowed reference
};

} // namespace paso

#endif // __PASO_FLUXLIMITER_H__

