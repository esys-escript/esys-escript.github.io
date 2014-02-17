
/* $Id$ */

/*******************************************************
 *
 *           Copyright 2003-2007 by ACceSS MNRF
 *       Copyright 2007 by University of Queensland
 *
 *                http://esscc.uq.edu.au
 *        Primary Business: Queensland, Australia
 *  Licensed under the Open Software License version 3.0
 *     http://www.opensource.org/licenses/osl-3.0.php
 *
 *******************************************************/

#if !defined BruceTestCase_20050829_H
#define BruceTestCase_20050829_H

#include "tools/CppUnitTest/TestCase.h"
#include "tools/CppUnitTest/TestSuite.h"
#include "tools/CppUnitTest/TestCaller.h"

#define REL_TOL ((double)1.e-10)

class BruceTestCase : public CppUnitTest::TestCase
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
  void testConstructorException();
  void testNull();
  void testZero();
  void test1d();
  void test2d();
  void test3d();
  void testBig();
  void testSetToXcon();
  void testSetToXfun();
  void testSetToSizecon();
  void testSetToSizefun();
  void testSetToXException();
  void testSetToSizeException();
  void testGetReferenceNoFromSampleNo();

  BruceTestCase (std::string name) : TestCase (name) {}
  ~BruceTestCase() {}
  //
  //
  // return the suite of tests to perform
  //
  static CppUnitTest::TestSuite* suite ();
};

#endif