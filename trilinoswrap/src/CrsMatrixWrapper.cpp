
/*****************************************************************************
*
* Copyright (c) 2016 by The University of Queensland
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

#include "CrsMatrixWrapper.h" 
#include "Amesos2Wrapper.h" 
#include "BelosWrapper.h" 
#include "PreconditionerFactory.h" 
#include "TrilinosAdapterException.h" 

#include <escript/SolverOptions.h>

#include <Kokkos_DefaultNode.hpp>
#include <MatrixMarket_Tpetra.hpp>
#include <Tpetra_DefaultPlatform.hpp>
#include <Tpetra_Vector.hpp>

using Teuchos::RCP;
using Teuchos::rcp;
using Teuchos::rcpFromRef;

namespace esys_trilinos {

template<typename ST>
CrsMatrixWrapper<ST>::CrsMatrixWrapper(const_TrilinosGraph_ptr graph) :
    mat(graph)
{
    mat.fillComplete();
    std::cout << "Matrix has " << mat.getGlobalNumEntries()
              << " entries." << std::endl;
}

template<typename ST>
void CrsMatrixWrapper<ST>::fillComplete(bool localOnly)
{
    RCP<Teuchos::ParameterList> params = Teuchos::parameterList();
    params->set("No Nonlocal Changes", localOnly);
    mat.fillComplete(params);
}

template<typename ST>
void CrsMatrixWrapper<ST>::add(const std::vector<LO>& rowIdx,
                               const std::vector<ST>& array)
{
    // NOTE: the reason this method takes a reference to the matrix and
    // we do the following with the row map is to avoid messing with shared
    // pointer use counters given that this method may be called from
    // parallel sections!
    const MapType& rowMap = *mat.getRowMap();
    const size_t emSize = rowIdx.size();
    const LO myLast = rowMap.getMaxLocalIndex();
    std::vector<LO> cols(emSize);
    std::vector<ST> vals(emSize);
    for (size_t i = 0; i < emSize; i++) {
        const LO row = rowIdx[i];
        if (row <= myLast) {
            for (int j = 0; j < emSize; j++) {
                const LO col = rowIdx[j];
                cols[j] = col;
                const size_t srcIdx = j * emSize + i;
                vals[j] = array[srcIdx];
            }
            mat.sumIntoLocalValues(row, cols, vals);
        }
    }
}

template<typename ST>
void CrsMatrixWrapper<ST>::ypAx(const Teuchos::ArrayView<ST>& y,
                                const Teuchos::ArrayView<const ST>& x) const
{
    RCP<VectorType<ST> > X = rcp(new VectorType<ST>(
                                             mat.getRowMap(), x, x.size(), 1));
    RCP<VectorType<ST> > Y = rcp(new VectorType<ST>(
                                             mat.getRowMap(), y, y.size(), 1));

    const ST alpha = Teuchos::ScalarTraits<ST>::one();
    const ST beta = Teuchos::ScalarTraits<ST>::one();

    // Y = beta*Y + alpha*A*X
    mat.apply(*X, *Y, Teuchos::NO_TRANS, alpha, beta);
    Y->get1dCopy(y, y.size());
}

template<typename ST>
void CrsMatrixWrapper<ST>::solve(const Teuchos::ArrayView<ST>& x,
                                 const Teuchos::ArrayView<const ST>& b,
                                 escript::SolverBuddy& sb) const
{
    typedef VectorType<ST> Vector;

    RCP<Vector> X = rcp(new Vector(mat.getDomainMap(), 1));
    RCP<Vector> B = rcp(new Vector(mat.getRangeMap(), b, b.size(), 1));
    RCP<const Matrix> A = rcpFromRef(mat);

    if (sb.getSolverMethod() == escript::SO_METHOD_DIRECT) {
        RCP<DirectSolverType<Matrix,Vector> > solver =
                                createDirectSolver<Matrix,Vector>(sb, A, X, B);
        if (sb.isVerbose()) {
            std::cout << solver->description() << std::endl;
            std::cout << "Performing symbolic factorization..." << std::flush;
        }
        solver->symbolicFactorization();
        if (sb.isVerbose()) {
            std::cout << "done\nPerforming numeric factorization..." << std::flush;
        }
        solver->numericFactorization();
        if (sb.isVerbose()) {
            std::cout << "done\nSolving system..." << std::flush;
        }
        solver->solve();
        if (sb.isVerbose()) {
            std::cout << "done" << std::endl;
            RCP<Teuchos::FancyOStream> fos(Teuchos::fancyOStream(Teuchos::rcpFromRef(std::cout)));
            solver->printTiming(*fos, Teuchos::VERB_HIGH);
        }

    } else { // iterative solver
        RCP<SolverType<ST> > solver = createSolver<ST>(sb);
        RCP<OpType<ST> > prec = createPreconditioner<ST>(A, sb);
        RCP<ProblemType<ST> > problem = rcp(new ProblemType<ST>(A, X, B));

        if (!prec.is_null()) {
            // Trilinos BiCGStab does not currently support left preconditioners
            if (sb.getSolverMethod() == escript::SO_METHOD_BICGSTAB)
                problem->setRightPrec(prec);
            else
                problem->setLeftPrec(prec);
        }
        problem->setProblem();
        solver->setProblem(problem);
        Belos::ReturnType result = solver->solve();
        if (sb.isVerbose()) {
            const int numIters = solver->getNumIters();
            if (result == Belos::Converged) {
                std::cout << "The solver took " << numIters
                   << " iteration(s) to reach a relative residual tolerance of "
                   << sb.getTolerance() << "." << std::endl;
            } else {
                std::cout << "The solver took " << numIters
                   << " iteration(s), but did not reach a relative residual "
                   "tolerance of " << sb.getTolerance() << "." << std::endl;
            }
        }
    }
    X->get1dCopy(x, x.size());
}

template<typename ST>
void CrsMatrixWrapper<ST>::nullifyRowsAndCols(
                                  const Teuchos::ArrayView<const ST>& rowMask,
                                  const Teuchos::ArrayView<const ST>& colView,
                                  ST mdv)
{
    RCP<VectorType<ST> > lclCol = rcp(new VectorType<ST>(mat.getRowMap(),
                                                 colView, colView.size(), 1));
    RCP<VectorType<ST> > gblCol = rcp(new VectorType<ST>(mat.getColMap(), 1));

    const ImportType importer(mat.getRowMap(), mat.getColMap());
    gblCol->doImport(*lclCol, importer, Tpetra::INSERT);
    Teuchos::ArrayRCP<const ST> colMask(gblCol->getData(0));
    const ST zero = Teuchos::ScalarTraits<ST>::zero();

    resumeFill();
// Can't use OpenMP here as replaceLocalValues() is not thread-safe.
//#pragma omp parallel for
    for (LO lclrow = 0; lclrow < mat.getNodeNumRows(); lclrow++) {
        Teuchos::ArrayView<const LO> indices;
        Teuchos::ArrayView<const ST> values;
        std::vector<GO> cols;
        std::vector<ST> vals;
        mat.getLocalRowView(lclrow, indices, values);
        GO row = mat.getRowMap()->getGlobalElement(lclrow);
        for (size_t c = 0; c < indices.size(); c++) {
            const LO lclcol = indices[c];
            const GO col = mat.getColMap()->getGlobalElement(lclcol);
            if (rowMask[lclrow] != zero || colMask[lclcol] != zero) {
                cols.push_back(lclcol);
                vals.push_back(row==col ? (ST)mdv : zero);
            }
        }
        if (cols.size() > 0)
            mat.replaceLocalValues(lclrow, cols, vals);
    }
    fillComplete(true);
}

template<typename ST>
void CrsMatrixWrapper<ST>::saveMM(const std::string& filename) const
{
    Tpetra::MatrixMarket::Writer<Matrix>::writeSparseFile(filename, rcpFromRef(mat));
}

template<typename ST>
void CrsMatrixWrapper<ST>::resetValues()
{
    resumeFill();
    mat.setAllToScalar(static_cast<const ST>(0.));
    fillComplete(true);
}


// instantiate the supported variants
template class CrsMatrixWrapper<real_t>;
template class CrsMatrixWrapper<cplx_t>;

}  // end of namespace

