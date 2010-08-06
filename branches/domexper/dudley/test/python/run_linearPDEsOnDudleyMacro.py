
########################################################
#
# Copyright (c) 2003-2010 by University of Queensland
# Earth Systems Science Computational Center (ESSCC)
# http://www.uq.edu.au/esscc
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
########################################################

__copyright__="""Copyright (c) 2003-2010 by University of Queensland
Earth Systems Science Computational Center (ESSCC)
http://www.uq.edu.au/esscc
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"

"""
Test suite for the linearPDE  and pdetools test on dudley

:remark:

:var __author__: name of author
:var __licence__: licence agreement
:var __url__: url entry point on documentation
:var __version__: version
:var __date__: date of the version
"""

__author__="Lutz Gross, l.gross@uq.edu.au, Joel Fenwick"

import os

import unittest
from test_linearPDEs import Test_Poisson,Test_LinearPDE, Test_LinearPDE_noLumping, Test_TransportPDE
from test_assemblage import Test_assemblage_2Do1, Test_assemblage_2Do2, Test_assemblage_3Do1, Test_assemblage_3Do2, \
                            Test_assemblage_2Do1_Contact,Test_assemblage_2Do2_Contact, Test_assemblage_3Do1_Contact, Test_assemblage_3Do2_Contact
from test_pdetools import Test_pdetools, Test_pdetools_noLumping
from esys.escript import *
from esys.dudley import Rectangle,Brick,JoinFaces, ReadMesh
import sys


try:
     DUDLEY_TEST_DATA=os.environ['DUDLEY_TEST_DATA']
except KeyError:
     DUDLEY_TEST_DATA='.'

DUDLEY_TEST_MESH_PATH=os.path.join(DUDLEY_TEST_DATA,"data_meshes")

NE=3

class Test_LinearPDEOnDudleyHex2DMacro(Test_LinearPDE,Test_pdetools,Test_assemblage_2Do1, Test_TransportPDE):
   RES_TOL=1.e-7
   ABS_TOL=1.e-8
   def setUp(self):
        self.domain = Rectangle(NE,NE,-1)
        self.order = 1
   def tearDown(self):
        del self.domain

class Test_LinearPDEOnDudleyHex3DMacro(Test_LinearPDE,Test_pdetools,Test_assemblage_3Do1, Test_TransportPDE):
   RES_TOL=1.e-7
   ABS_TOL=1.e-8
   def setUp(self):
        self.domain = Brick(NE,NE,NE,-1)
        self.order = 1
   def tearDown(self):
        del self.domain

class Test_LinearPDEOnDudleyTet2DMacro(Test_LinearPDE,Test_pdetools,Test_assemblage_2Do1, Test_TransportPDE):
   RES_TOL=1.e-7
   ABS_TOL=1.e-8
   def setUp(self):
        self.domain = ReadMesh(os.path.join(DUDLEY_TEST_MESH_PATH,"tet_2D_macro.fly"),optimize=False)
        # self.domain = ReadMesh(os.path.join(DUDLEY_TEST_MESH_PATH,"../rec.fly"),optimize=False)
        self.order = 1
   def tearDown(self):
        del self.domain

class Test_LinearPDEOnDudleyTet3DMacro(Test_LinearPDE,Test_pdetools,Test_assemblage_3Do1, Test_TransportPDE):
   RES_TOL=1.e-7
   ABS_TOL=1.e-8
   def setUp(self):
        self.domain = ReadMesh(os.path.join(DUDLEY_TEST_MESH_PATH,"tet_3D_macro.fly"),optimize=False)
        self.order = 1
   def tearDown(self):
        del self.domain

if __name__ == '__main__':
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(Test_LinearPDEOnDudleyHex2DMacro))
   suite.addTest(unittest.makeSuite(Test_LinearPDEOnDudleyHex3DMacro))
   suite.addTest(unittest.makeSuite(Test_LinearPDEOnDudleyTet2DMacro))
   suite.addTest(unittest.makeSuite(Test_LinearPDEOnDudleyTet3DMacro))

   s=unittest.TextTestRunner(verbosity=2).run(suite)
   if not s.wasSuccessful(): sys.exit(1)

