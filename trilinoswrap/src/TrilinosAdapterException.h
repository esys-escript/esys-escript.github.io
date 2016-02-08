
/*****************************************************************************
*
* Copyright (c) 2003-2016 by The University of Queensland
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

#ifndef __TRILINOSADAPTEREXCEPTION_H__
#define __TRILINOSADAPTEREXCEPTION_H__

#include <esysUtils/EsysException.h>

namespace esys_trilinos {

class TrilinosAdapterException : public esysUtils::EsysException
{
protected:
    typedef EsysException Parent;

public:
    TrilinosAdapterException() : Parent() { updateMessage(); }

    TrilinosAdapterException(const char* cstr) : Parent(cstr) {
        updateMessage();
    }

    TrilinosAdapterException(const std::string& str) : Parent(str) {
        updateMessage();
    }

    TrilinosAdapterException(const TrilinosAdapterException& other) :
        Parent(other)
    {
        updateMessage();
    }

    virtual ~TrilinosAdapterException() THROW(NO_ARG) {}

    inline TrilinosAdapterException &
    operator=(const TrilinosAdapterException& other) THROW(NO_ARG)
    {
        Parent::operator=(other);
        updateMessage();
        return *this;
    }

    virtual const std::string& exceptionName() const;

private:
    static const std::string exceptionNameValue;
};


} // namespace esys_trilinos

#endif // __TRILINOSADAPTEREXCEPTION_H__

