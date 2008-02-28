
/* $Id$ */

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

#if !defined escript_EsysAssertException_20040330_H
#define escript_EsysAssertException_20040330_H
#include "system_dep.h"

#include "EsysException.h"

namespace esysUtils {

  /**
  \brief
  EsysAssertException exception class.

  Description:
  EsysAssertException exception class.
  The class provides a public function returning the exception name.
  */
  class EsysAssertException : public EsysException
  {

  public:

    /**
    \brief
    Default constructor for the exception.
    */
    EsysAssertException() : EsysException() {}

    /**
    \brief
    Constructor for the exception.
    */
    EsysAssertException(const char *cstr) : EsysException(cstr) {}

    /**
    \brief
    Constructor for the exception.
    */
    EsysAssertException(const std::string &str) : EsysException(str) {}

    /// Destructor
    virtual ~EsysAssertException() {}

    /**
    \brief
    Returns the name of the exception.
    */
    virtual const std::string & exceptionName() const;

    /**
    \brief
    Builds a formatted message and throws an EsysAssertException.
    */
    static void assertFailure (const std::string& assertion,
                               const std::string& date,
                               const std::string& file,
                               int line, const std::string& errDesc);
  private:

    //
    // the exception name is immutable and class-wide.
    // Inheritor note; you need one of these too.
    // and an overloaded exceptionName() in your .cpp implementation file. 
    static const std::string exceptionNameValue;
  };

} // end of namespace
 
#endif
