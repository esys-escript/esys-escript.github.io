// $Id$
/*
 ******************************************************************************
 *                                                                            *
 *       COPYRIGHT ACcESS 2004 -  All Rights Reserved                         *
 *                                                                            *
 * This software is the property of ACcESS.  No part of this code             *
 * may be copied in any form or by any means without the expressed written    *
 * consent of ACcESS.  Copying, use or modification of this software          *
 * by any unauthorised person is illegal unless that                          *
 * person has a software license agreement with ACcESS.                       *
 *                                                                            *
 ******************************************************************************
 
******************************************************************************/

extern "C" {
#include "finley/finleyC/Finley.h"
}
#include "finley/CPPAdapter/MeshAdapter.h"
#include "finley/CPPAdapter/MeshAdapterFactory.h"
#include "finley/CPPAdapter/SystemMatrixAdapter.h"

#include "esysUtils/EsysException.h"
#include "esysUtils/esysExceptionTranslator.h"

#include "escript/Data/AbstractContinuousDomain.h"

#include <boost/python.hpp>
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include <boost/python/detail/defaults_gen.hpp>

using namespace boost::python;

/**
   @memo
   finley is the python module name that contains the interfaces
   to the C++ wrapper to finley.

   @version 1.0.0 

   @doc

   Class Description:
   Data

   Class Limitations:
   None

   Class Conditions of Use:
   None

   Throws:
   None

*/

//
// The BOOST_PYTHON_FUNCTION_OVERLOADS macro generates function overloads for optional
// arguments to the respective finley functions.
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//
// NOTE: If the number of arguments to the finley functions change
// the magic numbers in the BOOST_PYTHON_FUNCTION_OVERLOADS call 
// must change.
//
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// BOOST_PYTHON_FUNCTION_OVERLOADS(readMesh_overloads,finley::readMesh,1,2)
// BOOST_PYTHON_FUNCTION_OVERLOADS(brick_overloads,finley::brick,0,12)
// BOOST_PYTHON_FUNCTION_OVERLOADS(rectangle_overloads,finley::rectangle,0,9)
// BOOST_PYTHON_FUNCTION_OVERLOADS(interval_overloads,finley::interval,0,6)
// BOOST_PYTHON_FUNCTION_OVERLOADS(glueFaces_overloads,finley::glueFaces,1,3)
// BOOST_PYTHON_FUNCTION_OVERLOADS(joinFaces_overloads,finley::joinFaces,1,3)

BOOST_PYTHON_MODULE(finleycpp)
{

  // def("ReadMesh",finley::readMesh,readMesh_overloads());
  // def("Brick",finley::brick,brick_overloads());
  // def("Rectangle",finley::rectangle,rectangle_overloads());
  // def("Interval",finley::interval,interval_overloads());
  // def("GlueFaces",finley::glueFaces,glueFaces_overloads());
  // def("JoinFaces",finley::joinFaces,joinFaces_overloads());
  //
  // NOTE: The return_value_policy is necessary for functions that
  // return pointers.

  def("ReadMesh",finley::readMesh,
      (arg("fileName"),arg("integrationOrder")=-1),
      return_value_policy<manage_new_object>());

  def ("Brick",finley::brick,
      (arg("n0")=1,arg("n1")=1,arg("n2")=1,
      arg("order")=1,
      arg("l0")=1.0,arg("l1")=1.0,arg("l2")=1.0,
      arg("periodic0")=false,arg("periodic1")=false,arg("periodic2")=false,
      arg("integrationOrder")=-1,
      arg("useElementsOnFace")=false),
      return_value_policy<manage_new_object>());

  def ("Rectangle",finley::rectangle,
      (arg("n0")=1,arg("n1")=1,arg("order")=1,
      arg("l0")=1.0,arg("l1")=1.0,
      arg("periodic0")=false,arg("periodic1")=false,
      arg("integrationOrder")=-1,
      arg("useElementsOnFace")=false),
      return_value_policy<manage_new_object>());

  def("Interval",finley::interval,
      (arg("n1")=1,arg("order")=1,
      arg("l1")=1.0,arg("periodic0")=false,
      arg("integrationOrder")=-1,
      arg("useElementsOnFace")=false),
      return_value_policy<manage_new_object>());

  def("Merge",finley::meshMerge,
      return_value_policy<manage_new_object>());

  def("GlueFaces",finley::glueFaces,
      (arg("safetyFactor")=0.2,
      arg("tolerance")=std::numeric_limits<double>::epsilon()),
      return_value_policy<manage_new_object>());

  def("JoinFaces",finley::joinFaces,
      (arg("safetyFactor")=0.2,
      arg("tolerance")=std::numeric_limits<double>::epsilon()),
      return_value_policy<manage_new_object>());

  register_exception_translator<esysUtils::EsysException>(&esysUtils::esysExceptionTranslator);

  class_<finley::MeshAdapter, bases<escript::AbstractContinuousDomain> >
      ("MeshAdapter",init<optional <Finley_Mesh*> >())
      .def(init<const finley::MeshAdapter&>())
      .def("write",&finley::MeshAdapter::write)
      .def("getDescription",&finley::MeshAdapter::getDescription)
      .def("getDim",&finley::MeshAdapter::getDim)
      .def("getDataShape",&finley::MeshAdapter::getDataShape)
      .def("addPDEToSystem",&finley::MeshAdapter::addPDEToSystem)
      .def("addPDEToRHS",&finley::MeshAdapter::addPDEToRHS)
      .def("newOperator",&finley::MeshAdapter::newSystemMatrix)
      .def("getSystemMatrixTypeId",&finley::MeshAdapter::getSystemMatrixTypeId)
      .def("setX",&finley::MeshAdapter::setNewX)
      .def("getX",&finley::MeshAdapter::getX)
      .def("getNormal",&finley::MeshAdapter::getNormal)
      .def("getSize",&finley::MeshAdapter::getSize);


  class_<finley::SystemMatrixAdapter, bases<escript::AbstractSystemMatrix> >
      ("OperatorAdapter",no_init)
      .def("nullifyRowsAndCols",&finley::SystemMatrixAdapter::nullifyRowsAndCols)
      .def("setValue",&finley::SystemMatrixAdapter::setValue)
      .def("resetSolver",&finley::SystemMatrixAdapter::resetSolver)
      .def("saveMM",&finley::SystemMatrixAdapter::saveMM);

}
