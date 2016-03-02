
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


/****************************************************************************

  Assemblage routines: prepares the assemble parameter set

*****************************************************************************/

#include "Assemble.h"
#include <paso/SystemMatrix.h>

namespace finley {

AssembleParameters::AssembleParameters(const NodeFile* nodes,
                                       const ElementFile* ef,
                                       escript::AbstractSystemMatrix* sm,
                                       escript::Data& rhs,
                                       bool reducedOrder)
    : elements(ef),
      S(sm),
      F(rhs)
{
    int numSub, numQuadSub;
    
    paso::SystemMatrix* pasoMat = (sm ? dynamic_cast<paso::SystemMatrix*>(sm) : NULL);

    if (!rhs.isEmpty() && !rhs.actsExpanded()) {
        throw escript::ValueError("AssembleParameters: Right hand side is not expanded.");
    }
    // check the dimensions of S and rhs
    if (pasoMat!=NULL && !rhs.isEmpty()) {
        const index_t numRows = pasoMat->row_distribution->getMyNumComponents()*pasoMat->row_block_size;
        if (!rhs.numSamplesEqual(1, numRows/pasoMat->logical_row_block_size)) {
            throw escript::ValueError("AssembleParameters: number of rows of matrix and length of right hand side don't match.");
        }
    }

    // get the number of equations and components
    if (sm==NULL) {
        if (rhs.isEmpty()) {
            this->numEqu = this->numComp = 1;
        } else {
            this->numEqu = this->numComp = rhs.getDataPointSize();
        }
    } else {
        if (!rhs.isEmpty() && rhs.getDataPointSize() != sm->getRowBlockSize()) {
            throw escript::ValueError("AssembleParameters: matrix row block size and number of components of right hand side don't match.");
            return;
        }
        this->numEqu = sm->getRowBlockSize();
        this->numComp = sm->getColumnBlockSize();
    }
    this->col_DOF = nodes->borrowTargetDegreesOfFreedom();
    this->row_DOF = nodes->borrowTargetDegreesOfFreedom();

    // get information for the labeling of the degrees of freedom from
    // the matrix
    if (pasoMat) {
        // Make sure # rows in matrix == num DOF for one of:
        // full or reduced (use numLocalDOF for MPI)
        const index_t numRows = pasoMat->row_distribution->getMyNumComponents()*pasoMat->row_block_size;
        const index_t numCols = pasoMat->col_distribution->getMyNumComponents()*pasoMat->col_block_size;
        if (numRows == this->numEqu*nodes->getNumDegreesOfFreedom()) {
            this->row_DOF_UpperBound = nodes->getNumDegreesOfFreedom();
            this->row_DOF = nodes->borrowTargetDegreesOfFreedom();
            this->row_jac = ef->borrowJacobians(nodes, false, reducedOrder);
        } else if (numRows == this->numEqu*nodes->getNumReducedDegreesOfFreedom()) {
            this->row_DOF_UpperBound = nodes->getNumReducedDegreesOfFreedom();
            this->row_DOF = nodes->borrowTargetReducedDegreesOfFreedom();
            this->row_jac = ef->borrowJacobians(nodes, true, reducedOrder);
        } else {
            throw escript::ValueError("AssembleParameters: number of rows in matrix does not match the number of degrees of freedom in mesh");
        }
        // Make sure # cols in matrix == num DOF for one of:
        // full or reduced (use numLocalDOF for MPI)
        if (numCols == this->numComp*nodes->getNumDegreesOfFreedom()) {
            this->col_DOF_UpperBound = nodes->getNumDegreesOfFreedom();
            this->col_DOF = nodes->borrowTargetDegreesOfFreedom();
            this->col_jac = ef->borrowJacobians(nodes, false, reducedOrder);
        } else if (numCols == this->numComp*nodes->getNumReducedDegreesOfFreedom()) {
            this->col_DOF_UpperBound = nodes->getNumReducedDegreesOfFreedom();
            this->col_DOF = nodes->borrowTargetReducedDegreesOfFreedom();
            this->col_jac = ef->borrowJacobians(nodes, true, reducedOrder);
        } else {
            throw escript::ValueError("AssembleParameters: number of columns in matrix does not match the number of degrees of freedom in mesh");
        }
    } else if (sm) {
        // FIXME:
        this->row_DOF_UpperBound = nodes->getNumDegreesOfFreedom();
        this->row_DOF = nodes->borrowTargetDegreesOfFreedom();
        this->row_jac = ef->borrowJacobians(nodes, false, reducedOrder);
        this->col_DOF_UpperBound = nodes->getNumDegreesOfFreedom();
        this->col_DOF = nodes->borrowTargetDegreesOfFreedom();
        this->col_jac = ef->borrowJacobians(nodes, false, reducedOrder);
    }

    // get the information from right hand side
    if (!rhs.isEmpty()) {
        if (rhs.numSamplesEqual(1, nodes->getNumDegreesOfFreedom())) {
            this->row_DOF_UpperBound = nodes->getNumDegreesOfFreedom();
            this->row_DOF = nodes->borrowTargetDegreesOfFreedom();
            this->row_jac = ef->borrowJacobians(nodes, false, reducedOrder);
        } else if (rhs.numSamplesEqual(1, nodes->getNumReducedDegreesOfFreedom())) {
            this->row_DOF_UpperBound = nodes->getNumReducedDegreesOfFreedom();
            this->row_DOF = nodes->borrowTargetReducedDegreesOfFreedom();
            this->row_jac = ef->borrowJacobians(nodes, true, reducedOrder);
        } else {
            throw escript::ValueError("AssembleParameters: length of RHS vector does not match the number of degrees of freedom in mesh");
        }
        if (sm==NULL) {
            this->col_DOF_UpperBound = this->row_DOF_UpperBound;
            this->col_DOF = this->row_DOF;
            this->col_jac = this->row_jac;
        }
    }

    numSub = std::min(this->row_jac->numSub, this->col_jac->numSub);
    numQuadSub = this->row_jac->numQuadTotal/numSub;
    if (this->row_jac->numSides != this->col_jac->numSides) {
        throw escript::ValueError("AssembleParameters: number of sides for row and column shape functions must match.");
    }
    if (this->row_jac->numDim != this->col_jac->numDim) {
        throw escript::ValueError("AssembleParameters: spatial dimension for row and column shape function must match.");
    }
    if (ef->numNodes < this->row_jac->numShapesTotal) {
        throw escript::ValueError("AssembleParameters: too many nodes are expected by row.");
    }
    if (ef->numNodes < this->col_jac->numShapesTotal) {
        throw escript::ValueError("AssembleParameters: too many nodes are expected by col.");
    }
    if (this->row_jac->numElements != ef->numElements) {
        throw escript::ValueError("AssembleParameters: number of elements for row is wrong.");
    }
    if (this->col_jac->numElements != ef->numElements) {
        throw escript::ValueError("AssembleParameters: number of elements for column is wrong.");
    }
    if (this->row_jac->numQuadTotal != this->col_jac->numQuadTotal) {
        throw escript::ValueError("AssembleParameters: number of quadrature points for row and column shape functions must match.");
    }
    // to consider different basis function for rows and columns this will
    // require some work:
    if (numQuadSub*numSub != this->row_jac->numQuadTotal) {
        throw escript::ValueError("AssembleParameters: number of quadrature points for row is not correct.");
    }
    if (numQuadSub != this->row_jac->BasisFunctions->numQuadNodes) {
        throw escript::ValueError("AssembleParameters: Incorrect number of quadrature points for row.");
    }
    if (numQuadSub != this->col_jac->BasisFunctions->numQuadNodes) {
        throw escript::ValueError("AssembleParameters: Incorrect number of quadrature points for column.");
    }

    this->numQuadSub = numQuadSub;
    this->numSub = numSub;
    this->numQuadTotal = this->row_jac->numQuadTotal;
    this->NN = elements->numNodes;
    this->numElements = elements->numElements;
    this->numDim = this->row_jac->numDim;
    this->col_node = this->col_jac->node_selection;
    this->row_node = this->row_jac->node_selection;
    this->numSides = this->row_jac->numSides;
    this->row_numShapesTotal = this->row_jac->numShapesTotal;
    this->row_numShapes = this->row_jac->BasisFunctions->Type->numShapes;
    this->col_numShapesTotal = this->col_jac->numShapesTotal;
    this->col_numShapes = this->col_jac->BasisFunctions->Type->numShapes;
}

} // namespace finley

