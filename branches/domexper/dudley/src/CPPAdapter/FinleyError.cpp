
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


#ifdef PASO_MPI
#include <mpi.h>
#endif
#include "FinleyError.h"
#include <iostream>

namespace dudley {

  void setFinleyError(Finley_ErrorCodeType errorCode, 
		      const std::string& errMess) 
  {
    Finley_setError(errorCode,(__const char*)(errMess.c_str()));
  }

  void checkFinleyError() 
  {
    if (Finley_noError()) {
      return;
    } else {
      //
      // reset the error code to no error otherwise the next call to
      // this function may resurrect a previous error
      Finley_resetError();
      throw FinleyAdapterException(Finley_getErrorMessage());
    }
  }
  void checkPasoError() 
  {
    if (Paso_noError()) {
      return;
    } else {
      //
      // reset the error code to no error otherwise the next call to
      // this function may resurrect a previous error
      Paso_resetError();
      throw FinleyAdapterException(Paso_getErrorMessage());
    }
  }

}  // end of namespace
