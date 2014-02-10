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
                                                                           
#if !defined escript_DataExpanded_20040323_H
#define escript_DataExpanded_20040323_H
#ifdef MSVC
#ifdef ESCRIPT_EXPORTS
#define ESCRIPT_DLL __declspec(dllexport)
#else
#define ESCRIPT_DLL __declspec(dllimport)
#endif
#else
#define ESCRIPT_DLL
#endif

#include "DataAbstract.h"
#include "DataBlocks2D.h"
#include "DataArrayView.h"

#include <boost/scoped_ptr.hpp>
#include <boost/python/numeric.hpp>

namespace escript {

//
// Forward declarations of other Data types.
class DataEmpty;
class DataConstant;
class DataTagged;

/**
   \brief
   Give a short description of what DataExpanded does.

   Description:
   Give a detailed description of DataExpanded.

   Template Parameters:
   For templates describe any conditions that the parameters used in the
   template must satisfy.
*/

class ESCRIPT_DLL DataExpanded : public DataAbstract {

 public:

  /**
     \brief
     Constructor for DataExpanded.

     Description:
     Constructor for DataExpanded.

     The given single data value is copied to all the data points in 
     this data object, where the number of data points is defined by
     the given function space.

     \param value - Input - A single data value.
     \param what - Input - A description of what this data represents.
  */
  DataExpanded(const boost::python::numeric::array& value,
               const FunctionSpace& what);

  /**
     \brief
     Alternative constructor for DataExpanded.

     Description:
     Alternative Constructor for DataExpanded.

     The given single data value is copied to all the data points in 
     this data object, where the number of data points is defined by
     the given function space.

     \param value - Input - A single data value.
     \param what - Input - A description of what this data represents.
  */
  DataExpanded(const DataArrayView& value,
               const FunctionSpace& what);

  /**
     \brief
     Alternative constructor for DataExpanded that copies a slice from
     another DataExpanded.

     \param other - Input - DataExpanded object to slice from.
     \param region - Input - region to copy.
  */
  DataExpanded(const DataExpanded& other,
               const DataArrayView::RegionType& region);

  /**
     \brief
     Alternative constructor for DataExpanded objects.

     Description:
     Alternative Constructor for DataExpanded objects.
     \param what - Input - A description of what this data object represents.
     \param shape - Input - the shape of each data-point.
     \param data - the array of data values for the data-points.
  */
  DataExpanded(const FunctionSpace& what,
               const DataArrayView::ShapeType &shape,
               const DataArrayView::ValueType &data);

  /**
     \brief
     Copy constructor for DataExpanded.
     Performs a deep copy from another DataExpanded.
  */
  DataExpanded(const DataExpanded& other);

  /**
     \brief
     Copy constructor for DataExpanded.
     Construct a DataExpanded from a DataConstant.
  */
  DataExpanded(const DataConstant& other);

  /**
     \brief
     Copy constructor for DataExpanded.
     Construct a DataExpanded from a DataTagged.
  */
  DataExpanded(const DataTagged& other);

  /**
     \brief
     Default destructor for DataExpanded.
  */
  virtual
  ~DataExpanded();

  /**
     \brief
     Return a textual representation of the data.
  */
  virtual
  std::string
  toString() const;

  /**
     \brief
     Reshape the data point if the data point is currently rank 0.
     The original data point value is used for all values of the new
     data point.
  */
  void
  reshapeDataPoint(const DataArrayView::ShapeType& shape);

  /**
     \brief
     Return the offset for the given given data point. This returns
     the offset in bytes for the given point into the container
     holding the point data.

     \param sampleNo - Input - sample number.
     \param dataPointNo - Input - data point number.
  */
  virtual
  DataArrayView::ValueType::size_type
  getPointOffset(int sampleNo,
                 int dataPointNo) const;

  /**
     \brief
     Return a view into the data array for the data point specified.

     NOTE: Construction of the DataArrayView is a relatively expensive 
     operation.

     \param sampleNo - Input - sample number.
     \param dataPointNo - Input - data point number.
     \return DataArrayView for the data point.
  */
  DataArrayView
  getDataPoint(int sampleNo,
               int dataPointNo);

  /**
     \brief
     Return the number of doubles stored for the Data.
  */
  virtual
  ValueType::size_type
  getLength() const;

  /**
     \brief
     Factory method that returns a newly created DataExpanded.
     The caller is reponsible for managing the object created.

     \param region - Input - Region to copy.
  */
  virtual
  DataAbstract*
  getSlice(const DataArrayView::RegionType& region) const;

  /**
     \brief
     Copy the specified region from the given value.

     \param value - Input - Data object to copy from.
     \param region - Input - Region to copy.
  */
  virtual
  void
  setSlice(const DataAbstract* value,
           const DataArrayView::RegionType& region);

  /**
     \brief
     Assign the given value to all data-points associated with the given
     reference number.

     A reference number corresponds to a sample, and thus to all data-points
     in that sample.

     If the given reference number does not correspond to any sample in this
     Data object, an exception will be thrown.

     If the given value is a different shape to this Data object, an exception
     will be thrown.

     \param ref - Input - reference number which determines sample numebr to
                          assign given values to.
     \param value - Input - Value to assign to data-point associated with
                            the given reference number.
  */
  virtual
  void
  setRefValue(int ref,
              const DataArray& value);

  /**
     \brief
     Return the value of the first data-point in the sample associated with
     the given reference number.

     A reference number corresponds to a sample, and thus to all data-points
     in that sample. If there is more than one data-point per sample number
     in this Data object, the value of the first data-point will be returned.

     If the given reference number does not correspond to any sample in this
     Data object, an exception will be thrown.

     If the given value is a different shape to this Data object, an exception
     will be thrown.

     \param ref - Input - reference number which determines sample number to
                          read from.
     \param value - Output - Object to receive data-points associated with
                            the given reference number.
  */
  virtual
  void
  getRefValue(int ref,
              DataArray& value);

  /**
    \brief
    Archive the underlying data values to the file referenced
    by ofstream. A count of the number of values expected to be written
    is provided as a cross-check.

    The return value indicates success (0) or otherwise (1).
  */
  int
  archiveData(std::ofstream& archiveFile,
              const DataArrayView::ValueType::size_type noValues) const;

  /**
    \brief
    Extract the number of values specified by noValues from the file
    referenced by ifstream to the underlying data structure.

    The return value indicates success (0) or otherwise (1).
  */
  int
  extractData(std::ifstream& archiveFile,
              const DataArrayView::ValueType::size_type noValues);

 protected:

 private:

  /**
     \brief
     Common initialisation called from constructors.

     Description:
     Common initialisation called from constructors.

     Resizes the underlying data array to provide sufficient storage for the
     given shape and number of data points, and creates the corresponding
     DataArrayView of this data.

     \param shape - Input - The shape of the point data.
     \param noSamples - Input - number of samples.
     \param noDataPointsPerSample - Input - number of data points per sample.
  */
  void
  initialise(const DataArrayView::ShapeType& shape,
             int noSamples,
             int noDataPointsPerSample);

  /**
     \brief
     Copy the given data point value to all data points in this object.

     Description:
     Copy the given data point to all data points in this object.

     \param value Input - A single data point value.
  */
  void
  copy(const DataArrayView& value);

  /**
     \brief
     Copy the given data point value given a numarray object to all data points in this object.

     Description:
     Copy the given data point value given a numarray object to all data points in this object.

     \param value Input - A single data point value.
  */
  void
  copy(const boost::python::numeric::array& value);

  /**
     \brief
     Copy the numarray object to the data points in this object.

     Description:
     Copy the numarray object to the data points in this object.

     \param value Input - new values for the data points
  */
  void
  copyAll(const boost::python::numeric::array& value);

  //
  // The main data storage array, a 2D array of data blocks.
  // noSamples * noDataPointsPerSample
  DataBlocks2D m_data;

};

} // end of namespace

#endif