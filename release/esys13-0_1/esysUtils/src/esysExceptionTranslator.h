/* 
 ************************************************************
 *          Copyright 2006 by ACcESS MNRF                   *
 *                                                          *
 *              http://www.access.edu.au                    *
 *       Primary Business: Queensland, Australia            *
 *  Licensed under the Open Software License version 3.0    *
 *     http://www.opensource.org/licenses/osl-3.0.php       *
 *                                                          *
 ************************************************************
*/
                                                                           
#if !defined  esysUtils_esysExceptionTranslator_20040419_H
#define esysUtils_esysExceptionTranslator_20040419_H

#include "EsysException.h"

#include "boost/python/errors.hpp"

#include <iostream>

namespace esysUtils {
  /**
     \brief
     Function which translates an EsysException into a python exception
  */
  void esysExceptionTranslator(EsysException const& e);
} // end of namespace

#endif