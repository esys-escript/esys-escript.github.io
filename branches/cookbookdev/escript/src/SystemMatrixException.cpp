
/*******************************************************
*
* Copyright (c) 2003-2009 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/


#include "SystemMatrixException.h"

using namespace escript;

const std::string 
SystemMatrixException::exceptionNameValue("SystemMatrixException");


const std::string &
SystemMatrixException::exceptionName() const
{
  return exceptionNameValue;
}

