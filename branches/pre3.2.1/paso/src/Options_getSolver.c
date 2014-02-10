
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

/* Paso: returns the package to be used                   */

/**************************************************************/

/* Copyrights by ACcESS Australia 2004,2005 */
/* Author: Lutz Gross, l.gross@uq.edu.au */

/**************************************************************/

#include "Paso.h"
#include "Options.h"

/**************************************************************/

index_t Paso_Options_getSolver(index_t solver,index_t package, bool_t symmetry, Esys_MPIInfo *mpi_info) {
  index_t out=PASO_DEFAULT;
  /* PASO */
  if (package==PASO_PASO) {
     switch (solver) {
        case PASO_BICGSTAB:
            out=PASO_BICGSTAB;
            break;
        case PASO_PCG:
            out=PASO_PCG;
            break;
        case PASO_PRES20:
            out=PASO_PRES20;
            break;
        case PASO_GMRES:
            out=PASO_GMRES;
            break;
        case PASO_NONLINEAR_GMRES:
            out=PASO_NONLINEAR_GMRES;
            break;
        case PASO_TFQMR:
            out=PASO_TFQMR;
            break;
        case PASO_MINRES:
            out=PASO_MINRES;
            break;
        default:
            if (symmetry) {
               out=PASO_PCG;
            } else {
               out=PASO_BICGSTAB;
            }
            break;
     }
  /* MKL */
  } else if (package==PASO_MKL) {
    switch (solver) {
      case PASO_CHOLEVSKY:
        out=PASO_CHOLEVSKY;
        break;
      case PASO_DIRECT:
        out=PASO_DIRECT;
        break;
      default:
        if (symmetry) {
          out=PASO_CHOLEVSKY;
        } else {
          out=PASO_DIRECT;
        }
        break;
    }
  /* TRILINOS */
  } else if (package==PASO_TRILINOS) {
     switch (solver) {
        case PASO_BICGSTAB:
            out=PASO_BICGSTAB;
            break;
        case PASO_PCG:
            out=PASO_PCG;
            break;
        case PASO_PRES20:
            out=PASO_PRES20;
            break;
        case PASO_GMRES:
            out=PASO_GMRES;
            break;
        case PASO_TFQMR:
            out=PASO_TFQMR;
            break;
        case PASO_MINRES:
            out=PASO_MINRES;
            break;
        default:
            if (symmetry) {
               out=PASO_PCG;
            } else {
               out=PASO_BICGSTAB;
            }
            break;
     }
  } else if (package==PASO_UMFPACK) {
      out=PASO_DIRECT;
  } else {
      Esys_setError(VALUE_ERROR,"Unidentified package.");
  }
  return out;
}