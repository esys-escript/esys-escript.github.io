/*=============================================================================
 
 ******************************************************************************
 *                                                                            *
 *       COPYRIGHT  ???????  -  All Rights Reserved                           *
 *                                                                            *
 * This software is the property of ??????????????.  No part of this code     *
 * may be copied in any form or by any means without the expressed written    *
 * consent of ???????????.  Copying, use or modification of this software     *
 * by any unauthorised person is illegal unless that                          *
 * person has a software license agreement with ?????????????.                *
 *                                                                            *
 ******************************************************************************
 
*********************************************************************************/

#ifndef DATA_H
#define DATA_H

#include <string>
#include <Python.h>
#include <boost/python/object.hpp>
#include <boost/python/list.hpp>
#include <boost/python/numeric.hpp>

/**
   @memo
   Data

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
class Data {
  public:
  /**
     @memo
     Constructor which copies data from a python numarray.
     
     @param exceptionReason Input - Exception message.
  */
  Data(const boost::python::numeric::array& data);
  /**
     @memo
     Constructor which copies data from any object that can be converted into
     a numarray.
     
     @param exceptionReason Input - Exception message.
  */
  Data(const boost::python::object& data);

 private:

  std::auto_ptr<AbstractAccessor> m_dataAccessor;
  //
  // The vector containing the data
  std::vector<double> m_values;
};

#endif






