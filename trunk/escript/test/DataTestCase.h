
/*******************************************************
*
* Copyright (c) 2003-2010 by University of Queensland
* Earth Systems Science Computational Center (ESSCC)
* http://www.uq.edu.au/esscc
*
* Primary Business: Queensland, Australia
* Licensed under the Open Software License version 3.0
* http://www.opensource.org/licenses/osl-3.0.php
*
*******************************************************/


#if !defined  DataTestCase_20040624_H
#define  DataTestCase_20040624_H

#include "tools/CppUnitTest/TestCase.h"
#include "tools/CppUnitTest/TestSuite.h"
#include "tools/CppUnitTest/TestCaller.h"

#define REL_TOL ((double)1.e-10)

class DataTestCase : public CppUnitTest::TestCase
{
 public:

  //
  // setUp is called before each test method to set up test state
  void setUp();

  //
  // tearDown is called after each test method is called.
  void tearDown(); 

  //
  // A test method must return void and have no arguments

  void testSome();
  void testConstructors();
  void testDataConstant();
  void testDataTagged();
  void testDataTaggedExceptions();
  void testSlicing();
  void testOperations();
  void testMoreOperations();
  void testMemAlloc();
  void testCopying();
  void testResolveType();
  void testBinary();


  DataTestCase (std::string name) : TestCase (name) {}
  ~DataTestCase() {}

  //
  //
  // return the suite of tests to perform
  //

  static CppUnitTest::TestSuite* suite ();

private:
  void testCopyingWorker(bool delayed);
  void testSlicingWorker(bool delayed);


  void testSomeDriver(bool autolazy);

};

#endif
