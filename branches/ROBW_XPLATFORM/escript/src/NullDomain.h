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

#if !defined escript_NullDomain_20040604_H
#define escript_NullDomain_20040604_H

#include "AbstractDomain.h"

#include <string>

namespace escript {

/**
   \brief
   NullDomain provides a null value for domain. Needed for the construction
   of a default FunctionSpace.

   Description:
   NullDomain provides a null value for domain. Needed for the construction
   of a default FunctionSpace. Inherits from AbstractDomain and overrides its
   methods.
*/

class NullDomain : public AbstractDomain {

 public:

  /**
     \brief
     Default constructor for NullDomain.

     Description:
     Default constructor for NullDomain.

  */
  NullDomain();

  /**
     \brief
     Returns true if the given integer is a valid function space type
     for this domain.
  */
  virtual bool isValidFunctionSpaceType(int functionSpaceType) const;

  /**
     \brief
     Return a description for this domain.
  */
  virtual std::string getDescription() const;

  /**
     \brief
     Return a continuous FunctionSpace.
  */
  virtual int getContinuousFunctionCode() const;

  /**
     \brief
     Return a function FunctionSpace.
  */
  virtual int getFunctionCode() const;

  /**
     \brief
     Return a function on boundary FunctionSpace.
  */
  virtual int getFunctionOnBoundaryCode() const;

  /**
     \brief
     Return a FunctionSpace.
  */
  virtual int getFunctionOnContactZeroCode() const;

  /**
     \brief
     Return a FunctionSpace.
  */
  virtual int getFunctionOnContactOneCode() const;

  /**
     \brief
     Return a FunctionSpace.
  */
  virtual int getSolutionCode() const;

  /**
     \brief
     Return a FunctionSpace.
  */
  virtual int getReducedSolutionCode() const;

  /**
     \brief
     Return a FunctionSpace.
  */
  virtual int getDiracDeltaFunctionCode() const;

  /**
     \brief
     Return the number of data points per sample, and the number of samples as a pair.
     \param functionSpaceCode Input - Code for the function space type.
     \return pair, first - number of data points per sample, second - number of samples
  */
  virtual std::pair<int,int> getDataShape(int functionSpaceCode) const;

  /**
     \brief
     Return the tag key for the given sample number.
     \param functionSpaceType Input - The function space type.
     \param sampleNo Input - The sample number.
  */
  virtual int getTagFromSampleNo(int functionSpaceType, int sampleNo) const;

  /**
     \brief
     Return the reference number of the given sample number.
     \param functionSpaceType Input - The function space type.
     \param sampleNo Input - The sample number.
  */
  virtual int getReferenceNoFromSampleNo(int functionSpaceType, int sampleNo) const;

  /**
     \brief
  */
  virtual int getDim() const;

  /**
     \brief
     Return true if given domains are equal.
  */
  virtual bool operator==(const AbstractDomain& other) const;
  virtual bool operator!=(const AbstractDomain& other) const;

 protected:

 private:

};

} // end of namespace

#endif
