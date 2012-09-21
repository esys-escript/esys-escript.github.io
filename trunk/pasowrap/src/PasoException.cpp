
/*****************************************************************************
*
* Copyright (c) 2003-2012 by University of Queensland
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


#include "PasoException.h"
extern "C"
{
#include <esysUtils/error.h>
}

namespace paso
{

const std::string 
PasoException::exceptionNameValue("PasoException");

PASOWRAP_DLL_API
const std::string &
PasoException::exceptionName() const
{
  return exceptionNameValue;
}

PASOWRAP_DLL_API
void checkPasoError() 
{
  if (Esys_noError()) {
    return;
  } else {
    //
    // reset the error code to no error otherwise the next call to
    // this function may resurrect a previous error
    Esys_resetError();
    throw PasoException(Esys_getErrorMessage());
  }
}

}
