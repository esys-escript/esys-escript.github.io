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
#include "escript/Data/FunctionSpace.h"
#include "escript/Data/NullDomain.h"

#include "FunctionSpaceTestCase.h"

#include <iostream>
#include <sstream>

using namespace CppUnitTest;
using namespace escript;
using namespace std;

void FunctionSpaceTestCase::setUp() {
  //
  // This is called before each test is run
 
}

void FunctionSpaceTestCase::tearDown() {
  //
  // This is called after each test has been run
 
}

void FunctionSpaceTestCase::testAll() {
  //
  // The test code may be entered here
  // There is nothing special about the function name, it may be renamed to
  // something more suitable. 
  // As many test methods as desired may be added.

  cout << endl;

  // Test Default constructor
  FunctionSpace testFunctionSpace1;

  // Test constructor
  NullDomain nullDomain;
  int testfunctionSpaceType = nullDomain.getFunctionCode();

  FunctionSpace testFunctionSpace2(nullDomain, testfunctionSpaceType);
  
  // Test getTypeCode
  cout << "Test getTypeCode" << endl;
  assert(testFunctionSpace1.getTypeCode()==1);

  // Test getDomain
  cout << "Test getDomain" << endl;
  assert(testFunctionSpace2.getDomain()==nullDomain);

  // Test getDim
  cout << "Test getDim" << endl;
  assert(testFunctionSpace1.getDim()==1);

  // Test == operator
  cout << "Test == operator" << endl;
  assert(testFunctionSpace1==testFunctionSpace1);
  assert(!(testFunctionSpace1!=testFunctionSpace1));

  // Test = operator
  cout << "Test = operator" << endl;
  testFunctionSpace1=testFunctionSpace2;
  assert(testFunctionSpace1==testFunctionSpace2);

}

TestSuite* FunctionSpaceTestCase::suite ()
{
  //
  // create the suite of tests to perform.
  TestSuite *testSuite = new TestSuite ("FunctionSpaceTestCase");

  testSuite->addTest (new TestCaller< FunctionSpaceTestCase>("testAll",&FunctionSpaceTestCase::testAll));
  return testSuite;
}

