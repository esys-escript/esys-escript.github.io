
/*******************************************************
*
* Copyright (c) 2003-2008 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/

#ifndef escript_EscriptParams_H
#define escript_EscriptParams_H
#include "system_dep.h"
#include <boost/python/list.hpp>
#include "Data.h"    // for the operators

namespace escript
{

class Data;

class EscriptParams
{
public:
  ESCRIPT_DLL_API
  EscriptParams();

  ESCRIPT_DLL_API
  int getInt(const char* name, int sentinel=0) const;
  
  ESCRIPT_DLL_API
  void setInt(const char* name, int value);

private:

  // If we get more params we can replace this with a map
	int too_many_lines;
	int autolazy;

protected: 
  // This is to provide fast access for methods in Data.
  // Its a little bit ugly, needing all those friends but I really want to
  // limit outside access to the char* interface

  int getTOO_MANY_LINES() {return too_many_lines;}
  int getAUTOLAZY() { return autolazy;}

  friend class escript::Data;
  friend escript::Data escript::operator+(const boost::python::api::object&, const escript::Data&);
  friend escript::Data escript::operator-(const boost::python::api::object&, const escript::Data&);
  friend escript::Data escript::operator*(const boost::python::api::object&, const escript::Data&);
  friend escript::Data escript::operator/(const boost::python::api::object&, const escript::Data&);
  friend escript::Data escript::operator+(const escript::Data&, const escript::Data&);
  friend escript::Data escript::operator-(const escript::Data&, const escript::Data&);
  friend escript::Data escript::operator*(const escript::Data&, const escript::Data&);
  friend escript::Data escript::operator/(const escript::Data&, const escript::Data&);
  friend escript::Data escript::operator+(const escript::Data&, const boost::python::api::object&);
  friend escript::Data escript::operator-(const escript::Data&, const boost::python::api::object&);
  friend escript::Data escript::operator*(const escript::Data&, const boost::python::api::object&);
  friend escript::Data escript::operator/(const escript::Data&, const boost::python::api::object&);

};


extern EscriptParams escriptParams;

/**
  \brief Set the value of a named parameter.
  See listEscriptParams() (showEscriptParams() in python) for available parameters.
*/
ESCRIPT_DLL_API
void setEscriptParamInt(const char* name, int value);

/**
  \brief get the value of a named parameter.
  See listEscriptParams() (showEscriptParams() in python) for available parameters.
*/
ESCRIPT_DLL_API
int getEscriptParamInt(const char* name, int sentinel=0);

/**
  \brief describe available paramters.
  \return a list of tuples (parameter name, description)
*/
ESCRIPT_DLL_API
boost::python::list listEscriptParams();

}
#endif