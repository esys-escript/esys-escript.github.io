/* $Id$ */

#ifndef INC_PASO_UTIL
#define INC_PASO_UTIL

#ifdef MSVC
#ifdef PASO_EXPORTS
#define PASO_DLL __declspec(dllexport)
#else
#define PASO_DLL __declspec(dllimport)
#endif
#else
#define PASO_DLL
#endif

/**************************************************************/

/*   Some utility routines: */

/**************************************************************/

/*   Copyrights by ACcESS Australia, 2003,2004,2005 */
/*   author: gross@access.edu.au */

/**************************************************************/

#include "Common.h"

#ifdef __cplusplus
extern "C" {
#endif

/**************************************************************/

PASO_DLL index_t Paso_Util_cumsum(dim_t,index_t*);
PASO_DLL void Paso_copyDouble(dim_t n,double* source, double* target);
PASO_DLL bool_t Paso_Util_isAny(dim_t N,index_t* array,index_t value);

#ifdef __cplusplus
}
#endif /* __cplusplus */



#endif /* #ifndef INC_PASO_UTIL */

/*
 * $Log$
 * Revision 1.2  2005/09/15 03:44:39  jgs
 * Merge of development branch dev-02 back to main trunk on 2005-09-15
 *
 * Revision 1.1.2.1  2005/09/05 06:29:48  gross
 * These files have been extracted from finley to define a stand alone libray for iterative
 * linear solvers on the ALTIX. main entry through Paso_solve. this version compiles but
 * has not been tested yet.
 *
 *
 */