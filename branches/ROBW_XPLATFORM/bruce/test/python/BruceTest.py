# $Id$

import os
import sys
import unittest

from esys.escript import *
from esys.bruce import *

"""

Some simple tests of Bruce.

"""

class bruceTestCase(unittest.TestCase):

  def setUp(self):
    self.b = Rectangle(11,11,10,10)

  def tearDown(self):
    del self.b

  def testGetDescription(self):
    assert (self.b.getDescription()=="Bruce")

  def testValidFunctionSpace(self):
    assert (self.b.isValidFunctionSpaceType(0))
    assert (self.b.isValidFunctionSpaceType(1))
    assert (not(self.b.isValidFunctionSpaceType(2)))

  def testFunctionCode(self):
    assert (self.b.getContinuousFunctionCode()==0)
    assert (self.b.getFunctionCode()==1)

  def testFunctionSpaceTypeAsString(self):
    assert (self.b.functionSpaceTypeAsString(0) == "Bruce_ContinuousFunction")
    assert (self.b.functionSpaceTypeAsString(1) == "Bruce_Function")

  def testGetDim(self):
    assert (self.b.getDim()==2)

  def testGetNumSamples(self):
    numSamples = self.b.getNumSamples(0)
    assert (numSamples == 121)
    numSamples = self.b.getNumSamples(1)
    assert (numSamples == 100)

  def testGetNumDataPointsPerSample(self):
    numDataPointsPerSample = self.b.getNumDataPointsPerSample(0)
    assert (numDataPointsPerSample == 1)
    numDataPointsPerSample = self.b.getNumDataPointsPerSample(1)
    assert (numDataPointsPerSample == 1)

  def testGetReferenceNoFromSampleNo(self):
    numSamples = self.b.getNumSamples(0)
    for sampleNo in range(numSamples):
      assert (sampleNo == self.b.getReferenceNoFromSampleNo(0,sampleNo))
    numSamples = self.b.getNumSamples(1)
    for sampleNo in range(numSamples):
      assert (sampleNo == self.b.getReferenceNoFromSampleNo(1,sampleNo))

  def testTagFromSampleNo(self):
    numSamples = self.b.getNumSamples(0)
    for sampleNo in range(numSamples):
      assert (0 == self.b.getTagFromSampleNo(0,sampleNo))
    numSamples = self.b.getNumSamples(1)
    for sampleNo in range(numSamples):
      assert (0 == self.b.getTagFromSampleNo(1,sampleNo))

  def testBrick(self):
    brick = Brick(11,11,11,10,10,10)
    assert (brick.getDim()==3)

  def testRectangle(self):
    rectangle = Rectangle(11,11,10,10)
    assert (rectangle.getDim()==2)

  def testSaveVTK(self):
    filename = "testVTK.vts"
    fs1 = ContinuousFunction(self.b)
    fs2 = Function(self.b)
    testData1 = Scalar(1.0, fs1)
    testData2 = Scalar(1.0, fs2)
    testData3 = Vector(1.0, fs1)
    testData4 = Vector(1.0, fs2)
    testData5 = Tensor(1.0, fs1)
    testData6 = Tensor(1.0, fs2)
    dict = {'testData1':testData1,
            'testData2':testData2,
#            'testData3':testData3,
            'testData4':testData4,
            'testData5':testData5,
            'testData6':testData6}
    self.b.saveVTK(filename, dict)

if __name__ == '__main__':
  suite=unittest.TestSuite()
  suite.addTest(unittest.makeSuite(bruceTestCase))
  unittest.TextTestRunner(verbosity=2).run(suite)

sys.exit(0)