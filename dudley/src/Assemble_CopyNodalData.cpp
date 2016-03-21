
/*****************************************************************************
*
* Copyright (c) 2003-2016 by The University of Queensland
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

#include "Assemble.h"
#include "Util.h"

namespace dudley {

void Assemble_CopyNodalData(const NodeFile* nodes, escript::Data& out,
                            const escript::Data& in)
{
    if (!nodes)
        return;

    const int mpiSize = nodes->MPIInfo->size;
    const int numComps = out.getDataPointSize();
    const int in_data_type = in.getFunctionSpace().getTypeCode();
    const int out_data_type = out.getFunctionSpace().getTypeCode();

    // check out and in
    if (numComps != in.getDataPointSize()) {
        throw DudleyException("Assemble_CopyNodalData: number of components of input and output Data do not match.");
    } else if (!out.actsExpanded()) {
        throw DudleyException("Assemble_CopyNodalData: expanded Data object is expected for output data.");
    }

    // more sophisticated test needed for overlapping node/DOF counts
    if (in_data_type == DUDLEY_NODES) {
        if (!in.numSamplesEqual(1, nodes->getNumNodes())) {
            throw DudleyException("Assemble_CopyNodalData: illegal number of samples of input Data object");
        }
    } else if (in_data_type == DUDLEY_DEGREES_OF_FREEDOM) {
        if (!in.numSamplesEqual(1, nodes->getNumDegreesOfFreedom())) {
            throw DudleyException("Assemble_CopyNodalData: illegal number of samples of input Data object");
        }
        if ((((out_data_type == DUDLEY_NODES) || (out_data_type == DUDLEY_DEGREES_OF_FREEDOM)) && !in.actsExpanded() && (mpiSize > 1))) {

            throw DudleyException("Assemble_CopyNodalData: DUDLEY_DEGREES_OF_FREEDOM to DUDLEY_NODES or DUDLEY_DEGREES_OF_FREEDOM requires expanded input data on more than one processor.");
        }
    } else {
        throw DudleyException("Assemble_CopyNodalData: illegal function space type for target object");
    }

    dim_t numOut = 0;
    switch (out_data_type) {
        case DUDLEY_NODES:
            numOut = nodes->getNumNodes();
            break;

        case DUDLEY_DEGREES_OF_FREEDOM:
            numOut = nodes->getNumDegreesOfFreedom();
            break;

        default:
            throw escript::ValueError("Assemble_CopyNodalData: illegal function space type for source object");
    }

    if (!out.numSamplesEqual(1, numOut)) {
        throw escript::ValueError("Assemble_CopyNodalData: illegal number of samples of output Data object");
    }

    const size_t numComps_size = numComps * sizeof(double);

    /**************************** DUDLEY_NODES ******************************/
    if (in_data_type == DUDLEY_NODES) {
        out.requireWrite();
        if (out_data_type == DUDLEY_NODES) {
#pragma omp parallel for
            for (index_t n = 0; n < numOut; n++) {
                memcpy(out.getSampleDataRW(n), in.getSampleDataRO(n), numComps_size);
            }
        } else if (out_data_type == DUDLEY_DEGREES_OF_FREEDOM) {
            const index_t* map = nodes->borrowDegreesOfFreedomTarget();
#pragma omp parallel for
            for (index_t n = 0; n < numOut; n++) {
                memcpy(out.getSampleDataRW(n), in.getSampleDataRO(map[n]),
                       numComps_size);
            }
        }
    /********************** DUDLEY_DEGREES_OF_FREEDOM ***********************/
    } else if (in_data_type == DUDLEY_DEGREES_OF_FREEDOM) {
        out.requireWrite();
        if (out_data_type == DUDLEY_NODES) {
            paso::Coupler_ptr coupler(new paso::Coupler(nodes->degreesOfFreedomConnector, numComps));
            // safe provided coupler->copyAll is called before the pointer
            // in "in" is invalidated
            const_cast<escript::Data*>(&in)->resolve();
            coupler->startCollect(in.getDataRO());  
            const double* recv_buffer = coupler->finishCollect();
            const index_t upperBound = nodes->getNumDegreesOfFreedom();
            const index_t* target = nodes->borrowTargetDegreesOfFreedom();
#pragma omp parallel for
            for (index_t n = 0; n < numOut; n++) {
                const index_t k = target[n];
                if (k < upperBound) {
                    memcpy(out.getSampleDataRW(n), in.getSampleDataRO(k),
                           numComps_size);
                } else {
                    memcpy(out.getSampleDataRW(n),
                           &recv_buffer[(k - upperBound) * numComps],
                           numComps_size);
                }
            }
        } else if (out_data_type == DUDLEY_DEGREES_OF_FREEDOM) {
#pragma omp parallel for
            for (index_t n = 0; n < numOut; n++) {
                memcpy(out.getSampleDataRW(n), in.getSampleDataRO(n),
                       numComps_size);
            }
        }
    } // in_data_type
}

} // namespace dudley

