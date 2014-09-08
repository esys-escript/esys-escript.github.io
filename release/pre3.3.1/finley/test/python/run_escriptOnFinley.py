
##############################################################################
#
# Copyright (c) 2003-2013 by University of Queensland
# http://www.uq.edu.au
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
# Development until 2012 by Earth Systems Science Computational Center (ESSCC)
# Development since 2012 by School of Earth Sciences
#
##############################################################################

__copyright__="""Copyright (c) 2003-2013 by University of Queensland
http://www.uq.edu.au
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"

import os
import sys
import unittest

from esys.escript import *
from esys.finley import Rectangle, Brick
from test_objects import Test_Dump, Test_SetDataPointValue, Test_saveCSV, \
        Test_TableInterpolation, Test_Domain, Test_GlobalMinMax, Test_Lazy
from test_shared import Test_Shared

try:
     FINLEY_WORKDIR=os.environ['FINLEY_WORKDIR']
except KeyError:
     FINLEY_WORKDIR='.'

NE=4 # number elements, must be even

class Test_SharedOnFinley(Test_Shared):
  def setUp(self):
        self.domain=Rectangle(NE,NE)
        self.tol=0.001
  def tearDown(self):
        del self.domain
        del self.tol

class Test_DomainOnFinley(Test_Domain):
   def setUp(self):
       self.boundary_tag_list = [1, 2, 10, 20]
       self.domain =Rectangle(NE,NE+1,2)
   def tearDown(self):
       del self.domain
       del self.boundary_tag_list

   def test_setXError(self):
       domain=Rectangle(NE,NE)
       x=domain.getX()
       z=interpolate(x, Function(domain))
       self.assertRaises(RuntimeError, domain.setX, z)
       del x
       del z
       del domain

   def test_tagsContinuousFunction(self):
       ref_tags=[0]
       tags=ContinuousFunction(self.domain).getListOfTags()
       self.assertTrue(len(tags)==len(ref_tags), "tags list has wrong length.")
       for i in ref_tags: self.assertTrue(i in tags,"tag %s is missing."%i)

   def test_tagsFunction(self):
       ref_tags=[0]
       tags=Function(self.domain).getListOfTags()
       self.assertTrue(len(tags)==len(ref_tags), "tags list has wrong length.")
       for i in ref_tags: self.assertTrue(i in tags,"tag %s is missing."%i)
   def test_tagsReducedFunction(self):
       ref_tags=[0]
       tags=ReducedFunction(self.domain).getListOfTags()
       self.assertTrue(len(tags)==len(ref_tags), "tags list has wrong length.")
       for i in ref_tags: self.assertTrue(i in tags,"tag %s is missing."%i)
   def test_tagsFunctionOnBoundary(self):
       ref_tags=[1, 2, 10, 20]
       tags=FunctionOnBoundary(self.domain).getListOfTags()
       # For an MPI-distributed domain some tags may be missing
       if getMPISizeWorld() == 1: self.assertTrue(len(tags)==len(ref_tags), "tags list has wrong length.")
       for i in tags: self.assertTrue(i in ref_tags,"tag %s is missing."%i)
   def test_tagsReducedFunctionOnBoundary(self):
       ref_tags=[1, 2, 10, 20]
       tags=ReducedFunctionOnBoundary(self.domain).getListOfTags()
       # For an MPI-distributed domain some tags may be missing
       if getMPISizeWorld() == 1: self.assertTrue(len(tags)==len(ref_tags), "tags list has wrong length.")
       for i in tags: self.assertTrue(i in ref_tags,"tag %s is missing."%i)
   def test_tagsFunctionOnContactOne(self):
       ref_tags=[]
       tags=FunctionOnContactOne(self.domain).getListOfTags()
       self.assertTrue(len(tags)==len(ref_tags), "tags list has wrong length.")
       for i in ref_tags: self.assertTrue(i in tags,"tag %s is missing."%i)
   def test_tagsFunctionOnContactZero(self):
       ref_tags=[]
       tags=FunctionOnContactZero(self.domain).getListOfTags()
       self.assertTrue(len(tags)==len(ref_tags), "tags list has wrong length.")
       for i in ref_tags: self.assertTrue(i in tags,"tag %s is missing."%i)
   def test_tagsReducedFunctionOnContactOne(self):
       ref_tags=[]
       tags=ReducedFunctionOnContactOne(self.domain).getListOfTags()
       self.assertTrue(len(tags)==len(ref_tags), "tags list has wrong length.")
       for i in ref_tags: self.assertTrue(i in tags,"tag %s is missing."%i)
   def test_tagsReducedFunctionOnContactZero(self):
       ref_tags=[]
       tags=ReducedFunctionOnContactZero(self.domain).getListOfTags()
       self.assertTrue(len(tags)==len(ref_tags), "tags list has wrong length.")
       for i in ref_tags: self.assertTrue(i in tags,"tag %s is missing."%i)

class Test_DataOpsOnFinley(Test_Dump, Test_SetDataPointValue, Test_GlobalMinMax, Test_Lazy):
   def setUp(self):
       self.domain =Rectangle(NE,NE+1,2)
       self.domain_with_different_number_of_samples =Rectangle(2*NE,NE+1,2)
       self.domain_with_different_number_of_data_points_per_sample =Rectangle(2*NE,NE+1,2,integrationOrder=2)
       self.domain_with_different_sample_ordering =Rectangle(NE,NE+1,2, optimize=True)
       self.filename_base=FINLEY_WORKDIR
       self.mainfs=Function(self.domain)
       self.otherfs=Solution(self.domain)

   def tearDown(self):
       del self.domain
       del self.domain_with_different_number_of_samples
       del self.domain_with_different_number_of_data_points_per_sample
       del self.domain_with_different_sample_ordering
       del self.mainfs
       del self.otherfs


class Test_TableInterpolationOnFinley(Test_TableInterpolation):
    def setUp(self):
        self.domain=Brick(4,4,4)
        self.functionspaces=[ContinuousFunction(self.domain), Function(self.domain), ReducedFunction(self.domain),
            FunctionOnBoundary(self.domain), ReducedFunctionOnBoundary(self.domain),
            FunctionOnContactZero(self.domain), FunctionOnContactOne(self.domain),
            ReducedFunctionOnContactZero(self.domain), ReducedFunctionOnContactOne(self.domain)]
            #We aren't testing DiracDeltaFunctions
        self.xn=3       # number of grids on x axis
        self.yn=3       # number of grids on y axis
        self.zn=3       # number of grids on z axis

    def tearDown(self):
        del self.domain
        del self.functionspaces


#This functionality is only testes on Finley.
#It is not finley specific but it does need a known set of input points so I've chosen to put it here
class Test_OtherInterpolationOnFinley(unittest.TestCase):
    def setUp(self):
        self.r=Rectangle(4,1).getX()[0]+2
        self.z=Data(2)
        
    def tearDown(self):
        del self.z
        del self.r
       
    def test_nonuniformint(self):
        self.assertRaises(RuntimeError, self.z.nonuniformInterpolate, [0,1], [5,6], True)
        self.assertRaises(RuntimeError, self.z.nonuniformInterpolate, [3,4], [5,6], True)
        self.assertTrue(Lsup(self.z.nonuniformInterpolate([0,1], [5,6], False)-6)<0.00001, "RHS edge not fitted")
        self.assertTrue(Lsup(self.z.nonuniformInterpolate([3,4], [5,6], False)-5)<0.00001, "LHS edge not fitted")
        tmp=self.r.nonuniformInterpolate([2.125, 2.4, 2.5, 2.8], [1, -1, 2, 4], False)
        self.assertTrue(Lsup(sup(tmp)-4)<0.0001, "RHS edge not fitted for Rect")
        self.assertTrue(Lsup(inf(tmp)-0.090909)<0.00001, "Internal interpolate failed")
        tmp=self.r.nonuniformInterpolate([2.125, 2.4, 2.5, 3.2], [1, -1, 2, 4], False)
        self.assertTrue(Lsup(sup(tmp)-3.42857)<0.00001, "Internal interpolate failed")
        
    def test_nonuniformSlope(self):
        self.assertRaises(RuntimeError, self.z.nonuniformSlope, [0,1], [5,6], True)
        self.assertRaises(RuntimeError, self.z.nonuniformSlope, [3,4], [5,6], True)
        self.assertTrue(Lsup(self.z.nonuniformSlope([0,1], [5,6], False))<0.00001, "RHS edge not fitted")
        self.assertTrue(Lsup(self.z.nonuniformSlope([3,4], [5,6], False))<0.00001, "LHS edge not fitted")
        tmp=self.r.nonuniformSlope([2.125, 2.4, 2.5, 3.2], [1, -1, 2, 4], False)
        self.assertTrue(Lsup(sup(tmp)-30)<0.00001, "Internal interpolate failed")
        self.assertTrue(Lsup(inf(tmp)+7.27273)<0.00001, "Internal interpolate failed")
        
class Test_CSVOnFinley(Test_saveCSV):
    def setUp(self):
        NE0=NE
        NE1=NE+1
        self.domain = Rectangle(NE0, NE1, order=2)
        self.functionspaces = [ ContinuousFunction ]
        # number of total data points for each function space
        self.linecounts=[ (2*NE0+1)*(2*NE1+1)-NE0*NE1+1 ]
        # number of masked points, i.e. where X[0] is non-zero
        self.linecounts_masked=[ (2*NE0+1)*(2*NE1+1)-(2+NE0)*NE1 ]
        # expected values in first line of masked data = [ X[:], X[0] ]
        self.firstline=[ [1./(2*NE0), 0., 1./(2*NE0)] ]

        if getMPISizeWorld() == 1:
            self.functionspaces += [ ReducedContinuousFunction, Function,
                ReducedFunction, FunctionOnBoundary, ReducedFunctionOnBoundary ]
            self.linecounts += [ 31, 181, 81, 55, 37 ]
            self.linecounts_masked += [ 25, 181, 81, 40, 27 ]
            self.firstline += [ [.25, 0., .25],
                    [.02817541634481463,.02254033307585171,.02817541634481463],
                    [.05283121635129676,.04226497308103741,.05283121635129676],
                    [.02817541634481463,0.,.02817541634481463],
                    [.05283121635129676,0.,.05283121635129676]
                    ]
        else:
            print("Skipping some CSV tests on finley since MPI size > 1")

    def tearDown(self):
        del self.domain

    def test_csv_multiFS(self):
        if getMPISizeWorld() == 1:
            fname=os.path.join(FINLEY_WORKDIR, "test_multifs.csv")
            sol=Data(8,Solution(self.domain))
            ctsfn=Data(9,ContinuousFunction(self.domain))
            #test line 0
            dirac=Data(-1,DiracDeltaFunctions(self.domain))
            saveDataCSV(fname, A=sol, B=ctsfn, C=dirac)
            #test line 1
            fun=Data(5,Function(self.domain))
            rfun=Data(3,ReducedFunction(self.domain))
            saveDataCSV(fname, A=sol,B=ctsfn,C=fun, D=rfun)
            #test line 2
            bound=Data(1,FunctionOnBoundary(self.domain))
            rbound=Data(3,ReducedFunctionOnBoundary(self.domain))
            saveDataCSV(fname,A=sol,B=ctsfn,C=bound, D=rbound)
            #test line 3
            conzz=Data(7,FunctionOnContactZero(self.domain))
            rconz=Data(8,ReducedFunctionOnContactZero(self.domain))
            saveDataCSV(fname,A=sol,B=ctsfn, C=conzz, D=rconz)
            #check for cross line exceptions
            self.assertRaises(RuntimeError, saveDataCSV, fname, A=dirac, B=rfun)
            self.assertRaises(RuntimeError, saveDataCSV, fname, A=bound, B=conzz)
        else:
            print("Skipping CSV multiFS tests on finley since MPI size > 1")


if __name__ == '__main__':
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(Test_SharedOnFinley))
   suite.addTest(unittest.makeSuite(Test_DataOpsOnFinley))
   suite.addTest(unittest.makeSuite(Test_DomainOnFinley))
   suite.addTest(unittest.makeSuite(Test_TableInterpolationOnFinley))
   suite.addTest(unittest.makeSuite(Test_CSVOnFinley))
   suite.addTest(unittest.makeSuite(Test_OtherInterpolationOnFinley))
   s=unittest.TextTestRunner(verbosity=2).run(suite)
   if not s.wasSuccessful(): sys.exit(1)
