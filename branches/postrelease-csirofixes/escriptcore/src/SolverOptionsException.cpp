
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

#include "SolverOptionsException.h"

namespace escript {

const std::string SolverOptionsException::exceptionNameValue("SolverOptionsException");

const std::string& SolverOptionsException::exceptionName() const {
    return exceptionNameValue;
}

}

