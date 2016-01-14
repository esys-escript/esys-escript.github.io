
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

#include <boost/python/tuple.hpp>
#include "WrappedArray.h"
#include "DataException.h"
#if HAVE_NUMPY_H
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <numpy/ndarrayobject.h>
#endif

#include <iostream>

using namespace escript;
using namespace boost::python;

namespace
{

void checkFeatures(const boost::python::object& obj)
{
	using namespace std;
	boost::python::object o2;
	try
	{
	   /*int len=*/ extract<int>(obj.attr("__len__")());
	}
	catch (...)
	{
	   PyErr_Clear();
	   throw DataException("Object passed to WrappedArray must support __len__");
	}
	try
	{
	   o2=obj.attr("__getitem__");
	}
	catch (...)
	{
	   PyErr_Clear();
	   throw DataException("Object passed to WrappedArray must support __getitem__");
	}
}

void getObjShape(const boost::python::object& obj, DataTypes::ShapeType& s)
{
	int len=0;
	try
	{
	   len=extract<int>(obj.attr("__len__")());
	}
	catch(...)
	{
	   PyErr_Clear();		// tell python the error isn't there anymore
	   return;
	}
	if (len<1)
	{
	   throw DataException("Array filter - no empty components in arrays please.");
	}
	s.push_back(len);	

	if (s.size()>ESCRIPT_MAX_DATA_RANK)
	{
	   throw DataException("Array filter - Maximum rank exceeded in array");
	}
	getObjShape(obj[0],s);
}

}

WrappedArray::WrappedArray(const boost::python::object& obj_in)
:obj(obj_in),iscomplex(false),scalar_r(nan("")),scalar_c(nan(""))
{
	dat_r=0;
	dat_c=0;
	// First we check for scalars
	try
	{
	   extract<complextype> ec(obj_in);
	   extract<double> er(obj_in);
	   if (er.check())		// check for double first because complex will fail this
	   {
	      scalar_r=er();
	   }
	   else
	   {
	      scalar_c=ec();
	      iscomplex=true;
	     
	   }
	   rank=0;
	   return;
	} 
	catch (...)
	{		// so we clear the failure
	   PyErr_Clear();
	}
	try
	{
	   const boost::python::object obj_in_t=obj_in[make_tuple()];
	   extract<complextype> ec(obj_in_t);
	   extract<double> er(obj_in_t);
	   if (er.check())
	   {	     
	      scalar_r=er();
	     
	   }
	   else
	   {
	      scalar_c=ec();
	      iscomplex=true;
	   }	   
	   rank=0;
	   return;
	} 
	catch (...)
	{		// so we clear the failure
	   PyErr_Clear();
	}


	scalar_c=0;
	scalar_r=0;
	checkFeatures(obj_in);
	getObjShape(obj,shape);
	rank=shape.size();

#if HAVE_NUMPY_H
	// if obj is a numpy array it is much faster to copy the array through the
	// __array_struct__ interface instead of extracting single values from the
	// components via getElt(). For this to work we check below that
	// (1) this is a valid PyArrayInterface instance
	// (2) the data is stored as a contiguous C array
	// (3) the data type is suitable (correct type and byte size)
	try
	{
		object o = (extract<object>(obj.attr("__array_struct__")));
		if (PyCObject_Check(o.ptr()))
		{
			PyObject* cobj=(PyObject*)o.ptr();
			PyArrayInterface* arr=(PyArrayInterface*)PyCObject_AsVoidPtr(cobj);
#ifndef NPY_1_7_API_VERSION
  #define NPY_ARRAY_IN_ARRAY NPY_IN_ARRAY
  #define NPY_ARRAY_NOTSWAPPED NPY_NOTSWAPPED
#endif
			if (arr->two==2 && arr->flags&NPY_ARRAY_IN_ARRAY && arr->flags&NPY_ARRAY_NOTSWAPPED)
			{
				std::vector<int> strides;
				// convert #bytes to #elements
				for (int i=0; i<arr->nd; i++)
				{
					strides.push_back(arr->strides[i]/arr->itemsize);
				}

				if (arr->typekind == 'f')
				{
					if (arr->itemsize==sizeof(double))
					{
						convertNumpyArray<double>((const double*)arr->data, strides);
					}
					else if (arr->itemsize==sizeof(float))
			   		{
						convertNumpyArray<float>((const float*)arr->data, strides);
					}
				}
				else if (arr->typekind == 'i')
				{
					if (arr->itemsize==sizeof(int))
				   	{
						convertNumpyArray<int>((const int*)arr->data, strides);
					}
					else if (arr->itemsize==sizeof(long))
				   	{
						convertNumpyArray<long>((const long*)arr->data, strides);
					}
				}
				else if (arr->typekind == 'u')
				{
					if (arr->itemsize==sizeof(unsigned))
				   	{
						convertNumpyArray<unsigned>((const unsigned*)arr->data, strides);
					}
					else if (arr->itemsize==sizeof(unsigned long))
				   	{
						convertNumpyArray<unsigned long>((const unsigned long*)arr->data, strides);
					}
				}
				else if (arr->typekind == 'c')
				{
					if (arr->itemsize==sizeof(complextype))
				   	{
						convertNumpyArrayC<complextype>((const complextype*)arr->data, strides);
						iscomplex=true;
					}
					// not accomodating other types of complex values
				}				
			}
		}
	} catch (...)
	{
		PyErr_Clear();
	}
#endif
}


template<typename T>
void WrappedArray::convertNumpyArrayC(const T* array, const std::vector<int>& strides) const
{
	// this method is only called by the constructor above which does the
	// necessary checks and initialisations
	int size=DataTypes::noValues(shape);
	dat_c=new complextype[size];
	switch (rank)
	{
		case 1:
#pragma omp parallel for
			for (int i=0;i<shape[0];i++)
			{
				dat_c[i]=array[i*strides[0]];
			}
		break;
		case 2:
#pragma omp parallel for
			for (int i=0;i<shape[0];i++)
			{
				for (int j=0;j<shape[1];j++)
				{
					dat_c[DataTypes::getRelIndex(shape,i,j)]=array[i*strides[0]+j*strides[1]];
				}
			}
		break;
		case 3:
#pragma omp parallel for
			for (int i=0;i<shape[0];i++)
			{
				for (int j=0;j<shape[1];j++)
				{
					for (int k=0;k<shape[2];k++)
					{
						dat_c[DataTypes::getRelIndex(shape,i,j,k)]=array[i*strides[0]+j*strides[1]+k*strides[2]];
					}
				}
			}
		break;
		case 4:
#pragma omp parallel for
			for (int i=0;i<shape[0];i++)
			{
				for (int j=0;j<shape[1];j++)
				{
					for (int k=0;k<shape[2];k++)
					{
						for (int m=0;m<shape[3];m++)
						{
							dat_c[DataTypes::getRelIndex(shape,i,j,k,m)]=array[i*strides[0]+j*strides[1]+k*strides[2]+m*strides[3]];
						}
					}
				}
			}
		break;
	}
}


template<typename T>
void WrappedArray::convertNumpyArray(const T* array, const std::vector<int>& strides) const
{
	// this method is only called by the constructor above which does the
	// necessary checks and initialisations
	int size=DataTypes::noValues(shape);
	dat_r=new double[size];
	switch (rank)
	{
		case 1:
#pragma omp parallel for
			for (int i=0;i<shape[0];i++)
			{
				dat_r[i]=array[i*strides[0]];
			}
		break;
		case 2:
#pragma omp parallel for
			for (int i=0;i<shape[0];i++)
			{
				for (int j=0;j<shape[1];j++)
				{
					dat_r[DataTypes::getRelIndex(shape,i,j)]=array[i*strides[0]+j*strides[1]];
				}
			}
		break;
		case 3:
#pragma omp parallel for
			for (int i=0;i<shape[0];i++)
			{
				for (int j=0;j<shape[1];j++)
				{
					for (int k=0;k<shape[2];k++)
					{
						dat_r[DataTypes::getRelIndex(shape,i,j,k)]=array[i*strides[0]+j*strides[1]+k*strides[2]];
					}
				}
			}
		break;
		case 4:
#pragma omp parallel for
			for (int i=0;i<shape[0];i++)
			{
				for (int j=0;j<shape[1];j++)
				{
					for (int k=0;k<shape[2];k++)
					{
						for (int m=0;m<shape[3];m++)
						{
							dat_r[DataTypes::getRelIndex(shape,i,j,k,m)]=array[i*strides[0]+j*strides[1]+k*strides[2]+m*strides[3]];
						}
					}
				}
			}
		break;
	}
}


void WrappedArray::convertArrayR() const
{
	if ((converted) || (rank<=0) || (rank>4))	// checking illegal rank here to avoid memory issues later
	{					// yes the failure is silent here but not doing the copy 
	    return;				// will just cause an error to be raised later
	}
	int size=DataTypes::noValues(shape);
	double* tdat=new double[size];
	switch (rank)
	{
	case 1: for (int i=0;i<shape[0];i++)
		{
			tdat[i]=getElt(i);
		}
		break;
	case 2: for (int i=0;i<shape[0];i++)
		{
		    for (int j=0;j<shape[1];j++)
		    {
			tdat[DataTypes::getRelIndex(shape,i,j)]=getElt(i,j);
		    }
		}
		break;
	case 3: for (int i=0;i<shape[0];i++)
		{
		    for (int j=0;j<shape[1];j++)
		    {
			for (int k=0;k<shape[2];k++)
			{
			    tdat[DataTypes::getRelIndex(shape,i,j,k)]=getElt(i,j,k);
			}
		    }
		}
		break;
	case 4: for (int i=0;i<shape[0];i++)
		{
		    for (int j=0;j<shape[1];j++)
		    {
			for (int k=0;k<shape[2];k++)
			{
			    for (int m=0;m<shape[3];m++)
			    {
			    	tdat[DataTypes::getRelIndex(shape,i,j,k,m)]=getElt(i,j,k,m);
			    }
			}
		    }
		}
		break;
	default:
		;  // do nothing
		// can't happen. We've already checked the bounds above
	}
	dat_r=tdat;    
	converted=true;
}  


void WrappedArray::convertArrayC() const
{
	if ((converted) || (rank<=0) || (rank>4))	// checking illegal rank here to avoid memory issues later
	{					// yes the failure is silent here but not doing the copy 
	    return;				// will just cause an error to be raised later
	}
	int size=DataTypes::noValues(shape);
	complextype* tdat=new complextype[size];
	switch (rank)
	{
	case 1: for (int i=0;i<shape[0];i++)
		{
			tdat[i]=getElt(i);
		}
		break;
	case 2: for (int i=0;i<shape[0];i++)
		{
		    for (int j=0;j<shape[1];j++)
		    {
			tdat[DataTypes::getRelIndex(shape,i,j)]=getElt(i,j);
		    }
		}
		break;
	case 3: for (int i=0;i<shape[0];i++)
		{
		    for (int j=0;j<shape[1];j++)
		    {
			for (int k=0;k<shape[2];k++)
			{
			    tdat[DataTypes::getRelIndex(shape,i,j,k)]=getElt(i,j,k);
			}
		    }
		}
		break;
	case 4: for (int i=0;i<shape[0];i++)
		{
		    for (int j=0;j<shape[1];j++)
		    {
			for (int k=0;k<shape[2];k++)
			{
			    for (int m=0;m<shape[3];m++)
			    {
			    	tdat[DataTypes::getRelIndex(shape,i,j,k,m)]=getElt(i,j,k,m);
			    }
			}
		    }
		}
		break;
	default:
		;  // do nothing
		// can't happen. We've already checked the bounds above
	}
	dat_c=tdat;    
	converted=true;
}  


void WrappedArray::convertArray() const
{
    if (iscomplex)
    {
	convertArrayC();
    }
    else
    {
	convertArrayR();
    }
}

WrappedArray::~WrappedArray()
{
    if (dat_r!=0)
    {
	delete[] dat_r;
    }
    if (dat_c!=0)
    {
	delete[] dat_c;
    }
}


