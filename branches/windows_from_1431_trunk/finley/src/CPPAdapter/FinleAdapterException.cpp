
/* $Id: FinleyAdapterException.cpp 1312 2007-09-24 06:18:44Z ksteube $ */

/*******************************************************
 *
 *           Copyright 2003-2007 by ACceSS MNRF
 *       Copyright 2007 by University of Queensland
 *
 *                http://esscc.uq.edu.au
 *        Primary Business: Queensland, Australia
 *  Licensed under the Open Software License version 3.0
 *     http://www.opensource.org/licenses/osl-3.0.php
 *
 *******************************************************/

#include "FinleyAdapterException.h"


using namespace finley;


const std::string 
FinleyAdapterException::exceptionNameValue("FinleyAdapterException");


const std::string &
FinleyAdapterException::exceptionName() const
{
  return exceptionNameValue;
}

