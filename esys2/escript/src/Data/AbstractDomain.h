// $Id$
/* 
 ******************************************************************************
 *                                                                            *
 *       COPYRIGHT  ACcESS 2004 -  All Rights Reserved                        *
 *                                                                            *
 * This software is the property of ACcESS. No part of this code              *
 * may be copied in any form or by any means without the expressed written    *
 * consent of ACcESS.  Copying, use or modification of this software          *
 * by any unauthorised person is illegal unless that person has a software    *
 * license agreement with ACcESS.                                             *
 *                                                                            *
 ******************************************************************************
*/
                                                                           
#if !defined  escript_AbstractDomain_20040609_H
#define escript_AbstractDomain_20040609_H
                                                                                                                    
#include <string>
#include <utility>

namespace escript {

    class Data;
    class AbstractSystemMatrix;
    class FunctionSpace;
/**
   \brief
   Base class for all escript domains.

   Description:
   Base class for all escript domains.
*/
class AbstractDomain {

 public:

  /**
     \brief
     Default constructor for AbstractDomain

     Description:
     Default constructor for AbstractDomain. As the name suggests
     this is intended to be an abstract base class but by making it
     constructable avoid a boost.python wrapper class. A call to 
     almost any of the base class functions will throw an exception
     as they are not intended to be used.

     Preconditions:
     Describe any preconditions

     Throws:
     Describe any exceptions thrown
  */
  AbstractDomain();
  /**
     \brief
     Destructor for AbstractDomain

     Description:
     Destructor for AbstractDomain
  */
  virtual ~AbstractDomain();
  /**
     \brief
     Returns true if the given integer is a valid function space type
     for this domain.
  */
  virtual bool isValidFunctionSpaceType(int functionSpaceType) const;
  /**
     \brief
     Return a description for this domain
  */
  virtual std::string getDescription() const;
  /**
     \brief
     Return a description for the given function space type code
  */
  virtual std::string functionSpaceTypeAsString(int functionSpaceType) const;
  /**
     \brief
     Throw a standard exception. This function is called if any attempt 
     is made to use a base class function.
  */
  void throwStandardException(const std::string& functionName) const;
  /**
     \brief
      returns the spatial dimension of the domain.
      has to be implemented by the actual Domain adapter.
  */
  virtual int getDim() const;

  /**
   \brief
   Return true if domains equal. 
  */
  virtual bool operator==(const AbstractDomain& other) const;
  virtual bool operator!=(const AbstractDomain& other) const;
  /**
     \brief
     writes the doamin to an external file filename.
     has to be implemented by the actual Domain adapter.
  */
  virtual void write(const std::string& filename) const;

  /**
     \brief
     sets the tagList pointer and length of tag list numTags.
     *tagList may be null in which case on tags are used for functionSpaceType on the Domain.
     has to be implemented by the actual Domain adapter.
  */
  virtual void getTagList(int functionSpaceType, int** tagList, int* numTags) const;

 /**
     \brief
     Return the number of data points per sample, and the number of samples as a pair.
     has to be implemented by the actual Domain adapter.
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
     assigns new location to the domain
     has to be implemented by the actual Domain adapter.
  */
  virtual void setNewX(const escript::Data& arg);

  /**
     \brief
     interpolates data given on source onto target where source and target have to be given on the same domain.
     has to be implemented by the actual Domain adapter.
  */
  virtual void interpolateOnDomain(escript::Data& target,const escript::Data& source) const;
  virtual bool probeInterpolationOnDomain(int functionSpaceType_source,int functionSpaceType_target) const;
  /**
     \brief
     interpolates data given on source onto target where source and target are given on different domains.
     has to be implemented by the actual Domain adapter.
  */
  virtual void interpolateACross(escript::Data& target, const escript::Data& source) const;
  virtual bool probeInterpolationACross(int functionSpaceType_source,const AbstractDomain& targetDomain, int functionSpaceType_target) const;

  /**
     \brief returns locations in the domain. The function space is chosen appropriatly.
  */
  virtual escript::Data getX() const;
  /**
     \brief return boundary normals. The function space is chosen appropriatly.
  */
  virtual escript::Data getNormal() const;
  /**
     \brief returns the local size od samples. The function space is chosen appropriatly.
  */
  virtual escript::Data getSize() const;
  
  /**
     \brief
     copies the location of data points on the domain into out. The actual function space to be considered
     is defined by out. out has to be defined on this.
     has to be implemented by the actual Domain adapter.
  */
  virtual void setToX(escript::Data& out) const;
  /**
     \brief
     copies the surface normals at data points into out.  The actual function space to be considered
     is defined by out. out has to be defined on this.
     has to be implemented by the actual Domain adapter.
  */
  virtual void setToNormal(escript::Data& out) const;
  /**
     \brief
     copies the size of samples into out. The actual function space to be considered
     is defined by out. out has to be defined on this.
     has to be implemented by the actual Domain adapter.
  */
  virtual void setToSize(escript::Data& out) const;

  /**
     \brief
     copies the gradient of arg into grad. The actual function space to be considered
     for the gradient is defined by grad. arg and grad have to be defined on this.
     has to be implemented by the actual Domain adapter.
  */
  virtual void setToGradient(escript::Data& grad, const escript::Data& arg) const;

  /**
     \brief
     saves data arg to a OpenDX input file.
     considered as cell centered data.
     has to be implemented by the actual Domain adapter.
  */
  virtual void saveDX(const std::string& filename,const escript::Data& arg) const;
  /**
     \brief
     returns the function space representation of the type functionSpaceCode on this domain
     as a vtkObject.
     has to be implemented by the actual Domain adapter.
  */
  //virtual vtkObject createVtkObject(int functionSpaceCode) const;

    /**
     \brief
     returns true if data on this domain and a function space of type functionSpaceCode has to
     considered as cell centered data.
     has to be implemented by the actual Domain adapter.
  */
  virtual bool isCellOriented(int functionSpaceCode) const;


 protected:

 private:
};

} // end of namespace
#endif
