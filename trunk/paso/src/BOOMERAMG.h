
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


/************************************************************************************/

/* Paso: interface to HYPRE, a software library of
   high performance preconditioners and solvers. We use the 
   BoomerAMG provided in this library */

/************************************************************************************/

/* Author: Lin Gao, l.gao@uq.edu.au */

/************************************************************************************/

#ifndef INC_PASO_BOOMERAMG
#define INC_PASO_BOOMERAMG

#ifdef BOOMERAMG
#include <HYPRE_krylov.h> 
#include <HYPRE.h>
#include <HYPRE_parcsr_ls.h>
#endif

typedef struct {
#ifdef BOOMERAMG
  HYPRE_IJMatrix A;
  HYPRE_ParCSRMatrix parcsr_A;
  HYPRE_IJVector b;
  HYPRE_ParVector par_b;
  HYPRE_IJVector x;
  HYPRE_ParVector par_x;
  HYPRE_Solver solver;
#else
  void* n;
#endif
} Paso_BOOMERAMG_Handler;

#endif

