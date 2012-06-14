
/*******************************************************
*
* Copyright (c) 2003-2012 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/

#include "DataEmptyTestCase.h"

#include "escript/DataEmpty.h"
#include "escript/FunctionSpace.h"
#include "esysUtils/EsysException.h"

#include <cppunit/TestCaller.h>

using namespace CppUnit;
using namespace escript;
using namespace std;
using namespace esysUtils;

void DataEmptyTestCase::testAll()
{
  cout << endl;
  cout << "\tTest default constructor." << endl;
  DataEmpty testData;

  cout << "\tTest toString method." << endl;
  CPPUNIT_ASSERT(testData.toString() == "(Empty Data)");

  cout << "\tTest getPointOffset." << endl;
  CPPUNIT_ASSERT_THROW(testData.getPointOffset(0,0), EsysException);
  
  cout << "\tTest getDataPoint." << endl;
  CPPUNIT_ASSERT_THROW(testData.getPointOffset(0,0), EsysException);

  cout << "\tTest getLength." << endl;
  CPPUNIT_ASSERT(testData.getLength() == 0);

  DataTypes::RegionType region;

  cout << "\tTest getSlice." << endl;
  CPPUNIT_ASSERT_THROW(testData.getSlice(region), EsysException);

  cout << "\tTest setSlice." << endl;
  CPPUNIT_ASSERT_THROW(testData.setSlice(0,region), EsysException);
}

TestSuite* DataEmptyTestCase::suite()
{
  TestSuite *testSuite = new TestSuite("DataEmptyTestCase");

  testSuite->addTest(new TestCaller<DataEmptyTestCase>(
              "testAll",&DataEmptyTestCase::testAll));
  return testSuite;
}

