
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


#ifndef INC_FINLEY
#define INC_FINLEY

/************************************************************************************/

/*    Finley finite element solver */

/************************************************************************************/

#include "esysUtils/Esys_MPI.h"
#include "esysUtils/error.h"

/************************************************************************************/
/*#define Finley_TRACE */
#define FINLEY_UNKNOWN -1
#define FINLEY_DEGREES_OF_FREEDOM 1
#define FINLEY_NODES 3
#define FINLEY_ELEMENTS 4
#define FINLEY_FACE_ELEMENTS 5
#define FINLEY_POINTS 6
#define FINLEY_CONTACT_ELEMENTS_1 7
#define FINLEY_CONTACT_ELEMENTS_2 8
#define FINLEY_REDUCED_DEGREES_OF_FREEDOM 2
#define FINLEY_REDUCED_NODES 14
#define FINLEY_REDUCED_ELEMENTS 10
#define FINLEY_REDUCED_FACE_ELEMENTS 11
#define FINLEY_REDUCED_CONTACT_ELEMENTS_1 12
#define FINLEY_REDUCED_CONTACT_ELEMENTS_2 13

/* status stuff */
typedef int Finley_Status_t;
#define Finley_increaseStatus(self) ((self)->status)++
#define FINLEY_INITIAL_STATUS 0

/* error codes */


typedef Esys_ErrorCodeType Finley_ErrorCodeType;

/* interfaces */

double Finley_timer(void);
bool_t Finley_checkPtr(void*);
void Finley_resetError(void);
void Finley_setError(Finley_ErrorCodeType err,__const char* msg);
bool_t Finley_noError(void);
Finley_ErrorCodeType Finley_getErrorType(void);
char* Finley_getErrorMessage(void);
void Finley_convertPasoError(void);
bool_t Finley_MPI_noError( Esys_MPIInfo *mpi_info );

#endif /* #ifndef INC_FINLEY */

