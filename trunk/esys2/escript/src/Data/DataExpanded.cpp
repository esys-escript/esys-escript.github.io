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

#include "escript/Data/DataException.h"
#include "escript/Data/DataExpanded.h"
#include "escript/Data/DataConstant.h"
#include "escript/Data/DataTagged.h"
#include "escript/Data/DataArrayView.h"

#include <boost/python/extract.hpp>

#include <iostream>

using namespace std;
using namespace boost::python;
using namespace boost;

namespace escript {

  DataExpanded::DataExpanded(const boost::python::numeric::array& value, const FunctionSpace& what) : DataAbstract(what)
  {
    //cout << "Calling DataExpanded constructor 1." << endl;
    DataArrayView::ShapeType tempShape;
    //
    // extract the shape from the python array
    for (int i=0; i<value.getrank(); ++i) {
      cout << extract<int>(value.getshape()[i]) << endl;
      tempShape.push_back(extract<int>(value.getshape()[i]));
    }
    initialise(tempShape,what.getNumSamples(),what.getNumDPPSample());
    //
    // copy the given value to every data point
    copy(value);
  }

  DataExpanded::DataExpanded(const DataExpanded& other) : DataAbstract(other.getFunctionSpace()), m_data(other.m_data)
  {    
    //cout << "Calling DataExpanded copy constructor." << endl;
    //
    // create the view for the data
    DataArrayView temp(m_data.getData(),other.getPointDataView().getShape());
    setPointDataView(temp);
  }

  DataExpanded::DataExpanded(const DataConstant& other) : DataAbstract(other.getFunctionSpace())
  {    
    //cout << "Creating DataExpanded from DataConstant." << endl;
    initialise(other.getPointDataView().getShape(),other.getNumSamples(), other.getNumDPPSample());
    //
    // DataConstant only has one value
    copy(other.getPointDataView());
  }

  DataExpanded::DataExpanded(const DataTagged& other) : DataAbstract(other.getFunctionSpace())
  {    
    //cout << "Creating DataExpanded from DataTagged." << endl;
    initialise(other.getPointDataView().getShape(),other.getNumSamples(), other.getNumDPPSample());
    int i,j;
    DataArrayView::ValueType::size_type numRows=m_data.getNumRows();
    DataArrayView::ValueType::size_type numCols=m_data.getNumCols();
#pragma omp parallel for private(i,j) schedule(static)
    for (i=0;i<numRows;++i) {
      for (j=0;j<numCols;++j) {
	try {
	  getPointDataView().copy(getPointOffset(i,j), other.getPointDataView(), other.getPointOffset(i,j));
	}
	catch (std::exception& e) {
	  cout << e.what() << endl;
	}
      }
    }
  }

  DataExpanded::DataExpanded(const DataExpanded& other, const DataArrayView::RegionType& region) : DataAbstract(other.getFunctionSpace())
  {
    //cout << "Creating DataExpanded by slicing from another DataExpanded." << endl;
    //
    // get the shape of the slice
    DataArrayView::ShapeType shape(DataArrayView::getResultSliceShape(region));
    initialise(shape,other.getNumSamples(),other.getNumDPPSample());
    //
    // copy the data
    DataArrayView::ValueType::size_type numRows=m_data.getNumRows();
    DataArrayView::ValueType::size_type numCols=m_data.getNumCols();
    int i,j;
#pragma omp parallel for private(i,j) schedule(static)
    for (i=0;i<numRows;++i) {
      for (j=0;j<numCols;++j) {
	try {
	  getPointDataView().copySlice(getPointOffset(i,j), other.getPointDataView(), other.getPointOffset(i,j), region);
	}
	catch (std::exception& e) {
	  cout << e.what() << endl;
	}
      }
    }
  }

  DataExpanded::DataExpanded(const DataArrayView& value,const FunctionSpace& what): DataAbstract(what)
  {
    //cout << "Calling DataExpanded constructor 2." << endl;
    DataArrayView::ShapeType tempShape=value.getShape();
    initialise(tempShape,what.getNumSamples(),what.getNumDPPSample());
    copy(value);
  }

  DataExpanded::~DataExpanded()
  {
    //cout << "Destructing DataExpanded." << endl;
  }

  DataAbstract* DataExpanded::getSlice(const DataArrayView::RegionType& region) const 
  {
    return new DataExpanded(*this,region);
  }

  void DataExpanded::reshapeDataPoint(const DataArrayView::ShapeType& shape) 
  {
    //
    // reshape a rank zero data point
    if (getPointDataView().getRank()!=0) {
      stringstream temp;
      temp << "Error - Can only reshape Data with data points of rank 0. "
	   << "This Data has data points with rank: " 
	   << getPointDataView().getRank();
      throw DataException(temp.str());
    }
    DataBlocks2D newData(getNumSamples(),getNumDPPSample(), DataArrayView::noValues(shape));
    DataArrayView newView(newData.getData(),shape);
    //
    // Copy the original data to every value for the new shape
    int i,j;
    int nRows=m_data.getNumRows();
    int nCols=m_data.getNumCols();
    #pragma omp parallel for private(i,j) schedule(static)
    for (i=0;i<nRows;++i) {
      for (j=0;j<nCols;++j) {
	//
	// Copy the data into the specified offset
	// NOTE: An exception may be thown from this call if 
	// DOASSERT is on which of course will play
	// havoc with the omp threads. Run single threaded
	// if using DOASSERT. 
	newView.copy(newData.index(i,j),m_data.getData()[m_data.index(i,j)]);
      }
    }
    m_data.Swap(newData);
    DataArrayView temp(m_data.getData(),shape);
    setPointDataView(temp);
  }

  void DataExpanded::setSlice(const DataAbstract* value, const DataArrayView::RegionType& region) 
  {
    const DataExpanded* tempDataExp=dynamic_cast<const DataExpanded*>(value);
    if (tempDataExp==0) {
      throw DataException("Programming error - casting to DataExpanded.");
    }
    if (getPointDataView().getRank()!=region.size()) {
      throw DataException("Error - Invalid slice region.");
    }
    if (!value->getPointDataView().checkShape(DataArrayView::getResultSliceShape(region))) {
      throw DataException (value->getPointDataView().createShapeErrorMessage(
				"Error - Couldn't copy slice due to shape mismatch.",DataArrayView::getResultSliceShape(region)));
    }
    //
    // copy the data
    DataArrayView::ValueType::size_type numRows=m_data.getNumRows();
    DataArrayView::ValueType::size_type numCols=m_data.getNumCols();
    int i,j;
#pragma omp parallel for private(i,j) schedule(static)
    for (i=0;i<numRows;++i) {
      for (j=0;j<numCols;++j) {
	getPointDataView().copySliceFrom(getPointOffset(i,j), tempDataExp->getPointDataView(), tempDataExp->getPointOffset(i,j), region);
      }
    }
  }

  void DataExpanded::copy(const DataArrayView& value) 
  {
    //
    // Copy a single value to every data point
    int i,j;
    int nRows=m_data.getNumRows();
    int nCols=m_data.getNumCols();
    #pragma omp parallel for private(i,j) schedule(static)
    for (i=0;i<nRows;++i) {
      for (j=0;j<nCols;++j) {
	//
	// Copy the data into the specified offset
	// NOTE: An exception may be thown from this call if 
	// DOASSERT is on which of course will play
	// havoc with the omp threads. Run single threaded
	// if using DOASSERT. 
	getPointDataView().copy(m_data.index(i,j),value);
      }
    }
  }

  void DataExpanded::copy(const boost::python::numeric::array& value) 
  {
    //
    // first convert the numarray into a DataArrayView format
    DataArray temp(value);
    //
    // check the input shape matches this shape, this will throw an exception
    if (!getPointDataView().checkShape(temp.getView().getShape())) {
      throw DataException(getPointDataView().createShapeErrorMessage(
		 "Error - (DataExpanded) Cannot copy due to shape mismatch.",
		 temp.getView().getShape()));
    }
    //
    // now copy over the entire data structure
    copy(temp.getView());
  }

  void DataExpanded::initialise(const DataArrayView::ShapeType& shape, int noSamples, int noDataPointsPerSample)
  {
    //
    // resize data to the required size
    //cout << "noDataPointsPerSample=" << noDataPointsPerSample
    //     << " noSamples=" << noSamples
    //     << " noValuesPerDataPoint=" << DataArrayView::noValues(shape) << endl;
    m_data.resize(noSamples,noDataPointsPerSample, DataArrayView::noValues(shape));
    //
    // create a point data viewer of the data
    DataArrayView temp(m_data.getData(),shape);
    setPointDataView(temp);
    //cout << "leaving initialise." << endl;
  }

  string DataExpanded::toString() const
  {
    stringstream temp;
    //
    // create a temporary view as the offset will be changed
    DataArrayView tempView(getPointDataView().getData(), getPointDataView().getShape(), getPointDataView().getOffset());
    for (int i=0;i<m_data.getNumRows();++i) {
      for (int j=0;j<m_data.getNumCols();++j) {
        tempView.setOffset(m_data.index(i,j));
	stringstream suffix;
	suffix << "(" << i << "," << j << ")";
	temp << tempView.toString(suffix.str());
	if (!(i==(m_data.getNumRows()-1) && j==(m_data.getNumCols()-1))) {
	  temp << endl;
	}
      }
    }
    return temp.str();
  }

  DataArrayView::ValueType::size_type DataExpanded::getPointOffset(int sampleNo, int dataPointNo) const
  {
    return m_data.index(sampleNo,dataPointNo);
  }

  DataArrayView DataExpanded::getDataPoint(int sampleNo, int dataPointNo)
  {
    DataArrayView temp(m_data.getData(), getPointDataView().getShape(), m_data.index(sampleNo,dataPointNo));
    return temp;
  }

  DataArrayView::ValueType::size_type DataExpanded::getLength() const
  {
    return m_data.getData().size();
  }

}  // end of namespace
