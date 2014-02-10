
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


#include "TransportProblemException.h"


using namespace escript;


const std::string 
TransportProblemException::exceptionNameValue("TransportProblemException");


const std::string &
TransportProblemException::exceptionName() const
{
  return exceptionNameValue;
}

