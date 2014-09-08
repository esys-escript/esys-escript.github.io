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

#if !defined escript_FunctionSpace_20040323_H
#define escript_FunctionSpace_20040323_H
#include "system_dep.h"

#include "AbstractDomain.h"
#include "NullDomain.h"

#include <string>

namespace escript {

//
// Forward declaration for class Data.
class Data;

/**
   \brief
   Give a short description of what FunctionSpace does.

   Description:
   Give a detailed description of FunctionSpace.

   Template Parameters:
   For templates describe any conditions that the parameters used in the
   template must satisfy.
*/

class ESCRIPT_DLL_API FunctionSpace {

 public:
  /**
     \brief
     Default constructor for FunctionSpace.

     Description:
     Default constructor for FunctionSpace
     Generates a function space with a null domain.

     Preconditions:
     Describe any preconditions.

     Throws:
     Describe any exceptions thrown.
  */
  FunctionSpace();

  /**
     \brief
     Constructor for FunctionSpace.

     Description:
     Constructor for FunctionSpace.

     NOTE: The FunctionSpace class relies on the domain existing
     for the lifetime of the FunctionSpace object. ie: domain must
     be an externally managed object (!).
  */
  FunctionSpace(const AbstractDomain& domain,
                int functionSpaceType);

  /**
    \brief
    Return the function space type code.
  */
  int
  getTypeCode() const;

  /**
   \brief
   Return the function space domain.
  */
  const
  AbstractDomain&
  getDomain() const;

  /**
   \brief
   Assignment operator. 
   NOTE: Assignment copies the domain object pointer
   as this object is managed externally to this class.
  */
  FunctionSpace&
  operator=(const FunctionSpace& other);


  /**
     \brief assigns new tag newTag to all samples with a positive
     value of mask for any its sample point.

  */
  void setTags(const int newTag, const escript::Data& mask) const;


  /**
   \brief
   Return the shape of the data needed to represent the function space.
  */
  std::pair<int,int>
  getDataShape() const;

  /**
   \brief
   Comparison operator.
   Return true if function spaces are equal.
   ie: Same domain and same function space type.
  */
  bool
  operator==(const FunctionSpace& other) const;

  bool
  operator!=(const FunctionSpace& other) const;

  /**
   \brief
   Return a text description of the function space.
  */
  std::string
  toString() const;

  /**
   \brief
   Return the tag associated with the given sample number.
  */
  int
  getTagFromSampleNo(int sampleNo) const;

  /**
   \brief
   Return the tag associated with the given data-point number.
  */
  int
  getTagFromDataPointNo(int dataPointNo) const;

  /**
   \brief
   Return the reference number associated with the given sample number.
   This function is not efficient. It is better to first call 
   borrowSampleReferenceIDs and then when iterating over sampleNo to use sampleNo as an offset.
  */
  inline
  int
  getReferenceIDOfSample(int sampleNo) const
  {
      return borrowSampleReferenceIDs()[sampleNo];
  }
  /**
   \brief
   Return a borrowed reference to the list of sample reference IDs
  */
  int*
  borrowSampleReferenceIDs() const;

  /**
   \brief
   Return the spatial locations of the data points.
  */
  escript::Data
  getX() const;
 
  /**
   \brief
   Return the surface normal field.
  */
  escript::Data
  getNormal() const;

  /**
   \brief
   Return the sample size (e.g. the diameter of elements, radius of particles).
  */
  escript::Data
  getSize() const;

  /**
   \brief
   Return the number of samples.
  */
  inline
  int
  getNumSamples() const {
     return getDataShape().second;
  }

  /**
   \brief
   Return the number of data points per sample.
  */
  inline
  int
  getNumDPPSample() const {
     return getNumDataPointsPerSample();
  }

  inline
  int
  getNumDataPointsPerSample() const {
     return getDataShape().first;
  }

  /**
   \brief
   Return the spatial dimension of the underlying domain.
  */
  inline
  int
  getDim() const {
      return getDomain().getDim();
  }

 protected:

 private:

  //
  // static null domain value
  static NullDomain m_nullDomainValue;

  //
  // function space domain
  const AbstractDomain*  m_domain;

  //
  // function space type code.
  int m_functionSpaceType;

};

} // end of namespace

#endif