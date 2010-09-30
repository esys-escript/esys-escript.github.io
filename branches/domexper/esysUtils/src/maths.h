
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


#ifndef INC_ESYS_MATHS
#define INC_ESYS_MATHS

/**************************************************************/

/*    Pull in a maths library and define ISNAN      */


/* some system values */
/* FIXME: This is not satisfactory.                                */
/* _ECC, __INTEL_COMPILER, and other                               */
/* intel compiler pre-defines need to be handled                   */
/* (__ICL, __ICC come to mind)                                     */
#if defined(_WIN32) && defined(__INTEL_COMPILER)
#include <mathimf.h>
#else
#include <math.h>
#endif

/*#ifndef NAN
   #define NAN (0.0/0.0)
#endif
*/
/*#define IS_NAN(__VAL__)  ( (__VAL__) == NAN )*/  /* this does not work */
/* #define IS_NAN(__VAL__)  ( ! ( ( (__VAL__) >= 0. ) ||  ( (__VAL__) <= 0. ) ) )  this does not work */

#ifdef isnan
  #define IS_NAN(__VAL__) (isnan(__VAL__))
#elif defined _isnan
  #define IS_NAN(__VAL__) (_isnan(__VAL__))
#else
/* If we do not have isnan then we can't reliably check for NaN - return false */
  #define IS_NAN(__VAL__) (0)
#endif

#define INDEX_T_MAX INT_MAX
#define INDEX_T_MIN -INT_MAX
#define EPSILON DBL_EPSILON
#define LARGE_POSITIVE_FLOAT DBL_MAX
#define SMALL_NEGATIVE_FLOAT -DBL_MAX

#endif 
