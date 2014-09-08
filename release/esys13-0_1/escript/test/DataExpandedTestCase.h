// $Id$
/* 
 *****************************************************************************
 *                                                                           *
 *       COPYRIGHT  ACcESS  -  All Rights Reserved                           *
 *                                                                           *
 * This software is the property of ACcESS. No part of this code             *
 * may be copied in any form or by any means without the expressed written   *
 * consent of ACcESS.  Copying, use or modification of this software         *
 * by any unauthorised person is illegal unless that person has a software   *
 * license agreement with ACcESS.                                            *
 *                                                                           *
 *****************************************************************************
*/
#if !defined  DataExpandedTestCase_20040413_H
#define  DataExpandedTestCase_20040413_H

#include "tools/CppUnitTest/TestCase.h"
#include "tools/CppUnitTest/TestSuite.h"
#include "tools/CppUnitTest/TestCaller.h"

class DataExpandedTestCase : public CppUnitTest::TestCase
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
  // DataExpanded class

  //
  // General test case
  void testAll();

  //
  // Test case that tests reshaping of rank 0 object
  void testReshape();

  //
  // Test cases to test slicing of DataExpanded objects
  void testSlicing();
  void testSlicing2();
  void testSlicing3();
  void testSliceSetting();
  void testSliceSetting2();

  // Test cases for setRefValue and GetRefValue methods
  void testRefValue();

  DataExpandedTestCase (std::string name) : TestCase (name) {}
  ~DataExpandedTestCase() {}

  //
  // return the suite of tests to perform
  static CppUnitTest::TestSuite* suite ();
};

#endif