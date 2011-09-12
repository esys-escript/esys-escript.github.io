
/*******************************************************
*
* Copyright (c) 2003-2011 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/


/**************************************************************/

/* Paso: SystemMatrix: interface to intel MKL sparse solver */

/**************************************************************/

/* Copyrights by ACcESS Australia 2006 */
/* Author: Lutz Gross, l.gross@uq.edu.au */

/**************************************************************/

#ifndef INC_PASO_MKL
#define INC_PASO_MKL

#include "SparseMatrix.h"
#include "performance.h"

# if defined(_WIN32) || defined(_WIN64)
#define PARDISO pardiso
#else
#define PARDISO pardiso_
#endif

#ifdef MKL
#include "mkl_pardiso.h"
#endif


#define MKL_ERROR_NO 0
#define MKL_MTYPE_SYM -2
#define MKL_MTYPE_UNSYM 11

#define MKL_REORDERING_MINIMUM_DEGREE 0
#define MKL_REORDERING_NESTED_DISSECTION 2
#define MKL_PHASE_SYMBOLIC_FACTORIZATION 11
#define MKL_PHASE_FACTORIZATION 22
#define MKL_PHASE_SOLVE 33
#define MKL_PHASE_RELEASE_MEMORY -1

/* extern int PARDISO
#         (void *, int *, int *, int *, int *, int *,
#         double *, int *, int *, int *, int *, int *,
#         int *, double *, double *, int *);
*/


void Paso_MKL_free(Paso_SparseMatrix* A);
void Paso_MKL(Paso_SparseMatrix* A, double* out, double* in, index_t reordering, dim_t numRefinements, bool_t verbose);
#endif
