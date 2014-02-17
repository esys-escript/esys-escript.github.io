
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


#include "DataVector.h"

#include "Taipan.h"
#include "DataException.h"
#include <boost/python/extract.hpp>
#include "DataTypes.h"
#include "WrappedArray.h"

#include <cassert>

using namespace std;
using namespace escript;
using namespace boost::python;

namespace escript {

Taipan arrayManager;

void releaseUnusedMemory()
{
   arrayManager.release_unused_arrays();
}


DataVector::DataVector() :
  m_size(0),
  m_dim(0),
  m_N(0),
  m_array_data(0)
{
}

DataVector::DataVector(const DataVector& other) :
  m_size(other.m_size),
  m_dim(other.m_dim),
  m_N(other.m_N),
  m_array_data(0)
{
  m_array_data = arrayManager.new_array(m_dim,m_N);
  int i;
  #pragma omp parallel for private(i) schedule(static)
  for (i=0; i<m_size; i++) {
    m_array_data[i] = other.m_array_data[i];
  }
}

DataVector::DataVector(const DataVector::size_type size,
                       const DataVector::value_type val,
                       const DataVector::size_type blockSize) :
  m_size(size),
  m_dim(blockSize),
  m_array_data(0)
{
  resize(size, val, blockSize);
}

DataVector::~DataVector()
{
  // dispose of data array
  if (m_array_data!=0) {
    arrayManager.delete_array(m_array_data);
  }

  // clear data members
  m_size = -1;
  m_dim = -1;
  m_N = -1;
  m_array_data = 0;
}

void
DataVector::resize(const DataVector::size_type newSize,
                   const DataVector::value_type newValue,
                   const DataVector::size_type newBlockSize)
{
  assert(m_size >= 0);

  if ( newBlockSize == 0) {
    throw DataException("DataVector: invalid blockSize specified (newBlockSize)");
  }

  if ( (newSize % newBlockSize) != 0) {
    throw DataException("DataVector: invalid blockSize specified");
  }

  if (m_array_data!=0) {
    arrayManager.delete_array(m_array_data);
  }

  m_size = newSize;
  m_dim = newBlockSize;
  m_N = newSize / newBlockSize;
  m_array_data = arrayManager.new_array(m_dim,m_N);

  int i;
  #pragma omp parallel for private(i) schedule(static)
  for (i=0; i<m_size; i++) {
    m_array_data[i] = newValue;
  }
}

DataVector&
DataVector::operator=(const DataVector& other)
{
  assert(m_size >= 0);

  if (m_array_data!=0) {
    arrayManager.delete_array(m_array_data);
  }

  m_size = other.m_size;
  m_dim = other.m_dim;
  m_N = other.m_N;

  m_array_data = arrayManager.new_array(m_dim,m_N);
  int i;
  #pragma omp parallel for private(i) schedule(static)
  for (i=0; i<m_size; i++) {
    m_array_data[i] = other.m_array_data[i];
  }

  return *this;
}

bool
DataVector::operator==(const DataVector& other) const
{
  assert(m_size >= 0);

  if (m_size!=other.m_size) {
    return false;
  }
  if (m_dim!=other.m_dim) {
    return false;
  }
  if (m_N!=other.m_N) {
    return false;
  }
  for (int i=0; i<m_size; i++) {
    if (m_array_data[i] != other.m_array_data[i]) {
      return false;
    }
  }
  return true;
}

bool
DataVector::operator!=(const DataVector& other) const
{
  return !(*this==other);
}

void 
DataVector::copyFromArrayToOffset(const WrappedArray& value, size_type offset)
{
  using DataTypes::ValueType;
  const DataTypes::ShapeType& tempShape=value.getShape();
  size_type len=DataTypes::noValues(tempShape);
  if (offset+len>size())
  {
cerr << "offset=" << offset << " len=" << len << " >= " << size() << endl;
     throw DataException("Error - not enough room for that DataPoint at that offset.");
  }
  size_t si=0,sj=0,sk=0,sl=0;
  switch (value.getRank())
  {
  case 0:
	m_array_data[offset]=value.getElt();
	break;
  case 1:
	for (size_t i=0;i<tempShape[0];++i)
	{
	  m_array_data[offset+i]=value.getElt(i);
	}
	break;
  case 2:
	si=tempShape[0];
	sj=tempShape[1];
        for (ValueType::size_type i=0;i<si;i++) {
           for (ValueType::size_type j=0;j<sj;j++) {
              m_array_data[offset+DataTypes::getRelIndex(tempShape,i,j)]=value.getElt(i,j);
           }
        }
	break;
  case 3:
	si=tempShape[0];
	sj=tempShape[1];
	sk=tempShape[2];
        for (ValueType::size_type i=0;i<si;i++) {
           for (ValueType::size_type j=0;j<sj;j++) {
              for (ValueType::size_type k=0;k<sk;k++) {
                 m_array_data[offset+DataTypes::getRelIndex(tempShape,i,j,k)]=value.getElt(i,j,k);
              }
           }
        }
	break;
  case 4:
	si=tempShape[0];
	sj=tempShape[1];
	sk=tempShape[2];
	sl=tempShape[3];
        for (ValueType::size_type i=0;i<si;i++) {
           for (ValueType::size_type j=0;j<sj;j++) {
              for (ValueType::size_type k=0;k<sk;k++) {
                 for (ValueType::size_type l=0;l<sl;l++) {
                    m_array_data[offset+DataTypes::getRelIndex(tempShape,i,j,k,l)]=value.getElt(i,j,k,l);
                 }
              }
           }
        }
	break;
  default:
	ostringstream oss;
	oss << "Error - unknown rank. Rank=" << value.getRank();
	throw DataException(oss.str());
  }
}


void
DataVector::copyFromArray(const WrappedArray& value)
{
  using DataTypes::ValueType;
  if (m_array_data!=0) {
    arrayManager.delete_array(m_array_data);
  }
  DataTypes::ShapeType tempShape=value.getShape();
  DataVector::size_type nelements=DataTypes::noValues(tempShape);
  m_array_data = arrayManager.new_array(1,nelements);
  m_size=nelements;	// total amount of elements
  m_dim=m_size;		// elements per sample
  m_N=1;			// number of samples
  copyFromArrayToOffset(value,0);
}

} // end of namespace