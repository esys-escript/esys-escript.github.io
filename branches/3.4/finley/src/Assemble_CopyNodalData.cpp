
/*****************************************************************************
*
* Copyright (c) 2003-2013 by University of Queensland
* http://www.uq.edu.au
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
* Development until 2012 by Earth Systems Science Computational Center (ESSCC)
* Development since 2012 by School of Earth Sciences
*
*****************************************************************************/


/****************************************************************************

  Assemblage routines: copies data between different types of nodal
  representations

*****************************************************************************/

#include "Assemble.h"
#include "Util.h"

namespace finley {

void Assemble_CopyNodalData(NodeFile* nodes, escript::Data& out,
                            const escript::Data& in)
{
    Finley_resetError();
    if (!nodes)
        return;

    const int mpiSize = nodes->MPIInfo->size;
    const int numComps = out.getDataPointSize();
    const int in_data_type=in.getFunctionSpace().getTypeCode();
    const int out_data_type=out.getFunctionSpace().getTypeCode();

    // check out and in
    if (numComps != in.getDataPointSize()) {
        Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: number of components of input and output Data do not match.");
    } else if (!out.actsExpanded()) {
        Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: expanded Data object is expected for output data.");
    }

    // more sophisticated test needed for overlapping node/DOF counts
    if (in_data_type == FINLEY_NODES) {
        if (!in.numSamplesEqual(1, nodes->getNumNodes())) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: illegal number of samples of input Data object");
        }
    } else if (in_data_type == FINLEY_REDUCED_NODES) {
        if (!in.numSamplesEqual(1, nodes->getNumReducedNodes())) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: illegal number of samples of input Data object");
        }
    } else if (in_data_type == FINLEY_DEGREES_OF_FREEDOM) {
        if (!in.numSamplesEqual(1, nodes->getNumDegreesOfFreedom())) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: illegal number of samples of input Data object");
        }
        if (((out_data_type == FINLEY_NODES) || (out_data_type == FINLEY_DEGREES_OF_FREEDOM)) && !in.actsExpanded() && (mpiSize>1)) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: FINLEY_DEGREES_OF_FREEDOM to FINLEY_NODES or FINLEY_DEGREES_OF_FREEDOM requires expanded input data on more than one processor.");
        }
    } else if (in_data_type == FINLEY_REDUCED_DEGREES_OF_FREEDOM) {
        if (!in.numSamplesEqual(1, nodes->getNumReducedDegreesOfFreedom())) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: illegal number of samples of input Data object");
        }
        if ((out_data_type == FINLEY_DEGREES_OF_FREEDOM) && !in.actsExpanded() && (mpiSize>1)) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: FINLEY_REDUCED_DEGREES_OF_FREEDOM to FINLEY_DEGREES_OF_FREEDOM requires expanded input data on more than one processor.");
        }
    } else {
        Finley_setError(TYPE_ERROR, "Assemble_CopyNodalData: illegal function space type for target object");
    }

    if (out_data_type == FINLEY_NODES) {
        if (!out.numSamplesEqual(1, nodes->getNumNodes())) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: illegal number of samples of output Data object");
        }
    } else if (out_data_type == FINLEY_REDUCED_NODES) {
        if (!out.numSamplesEqual(1, nodes->getNumReducedNodes())) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: illegal number of samples of output Data object");
        }
    } else if (out_data_type == FINLEY_DEGREES_OF_FREEDOM) {
        if (!out.numSamplesEqual(1, nodes->getNumDegreesOfFreedom())) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: illegal number of samples of output Data object");
        }
    } else if (out_data_type == FINLEY_REDUCED_DEGREES_OF_FREEDOM) {
        if (!out.numSamplesEqual(1, nodes->getNumReducedDegreesOfFreedom())) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: illegal number of samples of output Data object");
        }
    } else {
        Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: illegal function space type for source object");
    }

    if (!Finley_noError())
        return;

    const size_t numComps_size = numComps*sizeof(double);
    escript::Data& _in(*const_cast<escript::Data*>(&in));

    /*********************** FINLEY_NODES ********************************/
    if (in_data_type == FINLEY_NODES) {
        out.requireWrite();
        if (out_data_type == FINLEY_NODES) {
#pragma omp parallel for
            for (int n=0; n<nodes->nodesMapping->numNodes; n++) {
                memcpy(out.getSampleDataRW(n), _in.getSampleDataRO(n), numComps_size);
            }
        } else if (out_data_type == FINLEY_REDUCED_NODES) {
#pragma omp parallel for
            for (int n=0; n<nodes->reducedNodesMapping->numTargets; n++) {
                memcpy(out.getSampleDataRW(n),
                       _in.getSampleDataRO(nodes->reducedNodesMapping->map[n]),
                       numComps_size);
            }
        } else if (out_data_type == FINLEY_DEGREES_OF_FREEDOM) {
            int nComps = Paso_Distribution_getMyNumComponents(nodes->degreesOfFreedomDistribution);
#pragma omp parallel for
            for (int n=0; n<nComps; n++) {
                memcpy(out.getSampleDataRW(n),
                       _in.getSampleDataRO(nodes->degreesOfFreedomMapping->map[n]),
                       numComps_size);
            }
        } else if (out_data_type == FINLEY_REDUCED_DEGREES_OF_FREEDOM) {
            int nComps = Paso_Distribution_getMyNumComponents(nodes->reducedDegreesOfFreedomDistribution);
#pragma omp parallel for
            for (int n=0; n<nComps; n++) {
                memcpy(out.getSampleDataRW(n),
                       _in.getSampleDataRO(nodes->reducedDegreesOfFreedomMapping->map[n]),
                       numComps_size);
            }
        }

    /*********************** FINLEY_REDUCED_NODES ***************************/
    } else if (in_data_type == FINLEY_REDUCED_NODES) {
        out.requireWrite();
        if (out_data_type == FINLEY_NODES) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: cannot copy from reduced nodes to nodes.");
        } else if (out_data_type == FINLEY_REDUCED_NODES) {
#pragma omp parallel for
            for (int n=0; n<nodes->reducedNodesMapping->numNodes; n++) {
                memcpy(out.getSampleDataRW(n), _in.getSampleDataRO(n), numComps_size);
            }
       } else if (out_data_type == FINLEY_DEGREES_OF_FREEDOM) {
            Finley_setError(TYPE_ERROR,"Assemble_CopyNodalData: cannot copy from reduced nodes to degrees of freedom.");
       } else if (out_data_type == FINLEY_REDUCED_DEGREES_OF_FREEDOM) {
            int nComps = Paso_Distribution_getMyNumComponents(nodes->reducedDegreesOfFreedomDistribution);
#pragma omp parallel for
            for (int n=0; n<nComps; n++) {
               const int k = nodes->reducedDegreesOfFreedomMapping->map[n];
               memcpy(out.getSampleDataRW(n),
                      _in.getSampleDataRO(nodes->reducedNodesMapping->target[k]),
                      numComps_size);
            }
        }

    /******************** FINLEY_DEGREES_OF_FREEDOM *********************/
    } else if (in_data_type == FINLEY_DEGREES_OF_FREEDOM) {
        out.requireWrite();
        if (out_data_type == FINLEY_NODES) {
            Paso_Coupler *coupler = Paso_Coupler_alloc(nodes->degreesOfFreedomConnector, numComps);
            if (Esys_noError()) {
                // It is not immediately clear whether coupler can be
                // trusted with constant data so I'll assume RW.
                // Also, it holds pointers so it might not be safe to use
                // on lazy data anyway?
                _in.requireWrite();
                Paso_Coupler_startCollect(coupler, _in.getSampleDataRW(0));
                const double *recv_buffer=Paso_Coupler_finishCollect(coupler);
                const int upperBound=Paso_Distribution_getMyNumComponents(nodes->degreesOfFreedomDistribution);
#pragma omp parallel for
                for (int n=0; n<nodes->numNodes; n++) {
                    const int k=nodes->degreesOfFreedomMapping->target[n];
                    if (k < upperBound) {
                        memcpy(out.getSampleDataRW(n), _in.getSampleDataRO(k),
                               numComps_size);
                    } else {
                        memcpy(out.getSampleDataRW(n),
                               &recv_buffer[(k-upperBound)*numComps],
                               numComps_size);
                    }
                }
            }
            Paso_Coupler_free(coupler);
        } else if  (out_data_type == FINLEY_REDUCED_NODES) {
            Paso_Coupler *coupler = Paso_Coupler_alloc(nodes->degreesOfFreedomConnector, numComps);
            if (Esys_noError()) {
                _in.requireWrite(); // See comment above about coupler and const
                Paso_Coupler_startCollect(coupler, _in.getSampleDataRW(0));
                const double *recv_buffer=Paso_Coupler_finishCollect(coupler);
                const int upperBound=Paso_Distribution_getMyNumComponents(nodes->degreesOfFreedomDistribution);

#pragma omp parallel for
                for (int n=0; n<nodes->reducedNodesMapping->numTargets; n++) {
                    const int l=nodes->reducedNodesMapping->map[n];
                    const int k=nodes->degreesOfFreedomMapping->target[l];
                    if (k < upperBound) {
                        memcpy(out.getSampleDataRW(n), _in.getSampleDataRO(k),
                               numComps_size);
                    } else {
                        memcpy(out.getSampleDataRW(n),
                               &recv_buffer[(k-upperBound)*numComps],
                               numComps_size);
                    }
                }
            }
            Paso_Coupler_free(coupler);
        } else if (out_data_type == FINLEY_DEGREES_OF_FREEDOM) {
            const int nComps = Paso_Distribution_getMyNumComponents(nodes->degreesOfFreedomDistribution);
#pragma omp parallel for
            for (int n=0; n<nComps; n++) {
                memcpy(out.getSampleDataRW(n), _in.getSampleDataRO(n),
                       numComps_size);
            }
        } else if (out_data_type == FINLEY_REDUCED_DEGREES_OF_FREEDOM) {
            const int nComps = Paso_Distribution_getMyNumComponents(nodes->reducedDegreesOfFreedomDistribution);
#pragma omp parallel for
            for (int n=0; n<nComps; n++) {
                const int k=nodes->reducedDegreesOfFreedomMapping->map[n];
                memcpy(out.getSampleDataRW(n),
                       _in.getSampleDataRO(nodes->degreesOfFreedomMapping->target[k]),
                       numComps_size);
            }
        }

    /**************** FINLEY_REDUCED_DEGREES_OF_FREEDOM *****************/
    } else if (in_data_type == FINLEY_REDUCED_DEGREES_OF_FREEDOM) {
        if (out_data_type == FINLEY_NODES) {
            Finley_setError(TYPE_ERROR, "Assemble_CopyNodalData: cannot copy from reduced degrees of freedom to nodes.");
        } else if (out_data_type == FINLEY_REDUCED_NODES) {
            Paso_Coupler *coupler=Paso_Coupler_alloc(nodes->reducedDegreesOfFreedomConnector,numComps);
            if (Esys_noError()) {
                const int upperBound=Paso_Distribution_getMyNumComponents(nodes->reducedDegreesOfFreedomDistribution);
                _in.requireWrite(); // See comment about coupler and const
                Paso_Coupler_startCollect(coupler, _in.getSampleDataRW(0));
                const double *recv_buffer=Paso_Coupler_finishCollect(coupler);
                out.requireWrite();
#pragma omp parallel for
                for (int n=0; n<nodes->reducedNodesMapping->numTargets; n++) {
                    const int l=nodes->reducedNodesMapping->map[n];
                    const int k=nodes->reducedDegreesOfFreedomMapping->target[l];
                    if (k < upperBound) {
                        memcpy(out.getSampleDataRW(n), _in.getSampleDataRO(k),
                               numComps_size);
                    } else {
                        memcpy(out.getSampleDataRW(n),
                               &recv_buffer[(k-upperBound)*numComps],
                               numComps_size);
                    }
                }
            }
            Paso_Coupler_free(coupler);
        } else if (out_data_type == FINLEY_REDUCED_DEGREES_OF_FREEDOM) {
            const int nComps = Paso_Distribution_getMyNumComponents(nodes->reducedDegreesOfFreedomDistribution);
            out.requireWrite();
#pragma omp parallel for
            for (int n=0; n<nComps; n++) {
                memcpy(out.getSampleDataRW(n), _in.getSampleDataRO(n), numComps_size);
            }
        } else if (out_data_type == FINLEY_DEGREES_OF_FREEDOM ) {
            Finley_setError(TYPE_ERROR, "Assemble_CopyNodalData: cannot copy from reduced degrees of freedom to degrees of freedom.");
        }
    } // in_data_type
}

} // namespace finley
