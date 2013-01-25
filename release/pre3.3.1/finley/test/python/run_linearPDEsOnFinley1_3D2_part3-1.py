
########################################################
#
# Copyright (c) 2003-2013 by University of Queensland
# Earth Systems Science Computational Center (ESSCC)
# http://www.uq.edu.au
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
########################################################

__copyright__="""Copyright (c) 2003-2013 by University of Queensland
Earth Systems Science Computational Center (ESSCC)
http://www.uq.edu.au
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"

"""
Test suite for the linearPDE  and pdetools test on finley

:remark:

:var __author__: name of author
:var __licence__: licence agreement
:var __url__: url entry point on documentation
:var __version__: version
:var __date__: date of the version
"""

__author__="Lutz Gross, l.gross@uq.edu.au"

import os

import unittest
#from test_linearPDEs import Test_Poisson,Test_LinearPDE, Test_LinearPDE_noLumping, Test_TransportPDE
from test_assemblage_3Do2 import Test_assemblage_3Do2
#from test_pdetools import Test_pdetools, Test_pdetools_noLumping
#from esys.escript import *
from esys.finley import Rectangle,Brick,JoinFaces, ReadMesh
import sys

try:
     FINLEY_TEST_DATA=os.environ['FINLEY_TEST_DATA']
except KeyError:
     FINLEY_TEST_DATA='.'

FINLEY_TEST_MESH_PATH=os.path.join(FINLEY_TEST_DATA,"data_meshes")

NE=10 # number of element in each spatial direction (must be even)


class Test_LinearPDEOnFinleyHex3DOrder2_part3_1(Test_assemblage_3Do2):
   RES_TOL=1.e-7
   ABS_TOL=1.e-8
   def setUp(self):
        self.domain = Brick(NE,NE,NE,2)
        self.order = 2
   def tearDown(self):
        del self.domain

if __name__ == '__main__':
   suite = unittest.TestSuite()
   if True :
      suite.addTest(unittest.makeSuite(Test_LinearPDEOnFinleyHex3DOrder2_part3_1))
   else:
      suite.addTest(Test_LinearPDEOnFinleyHex2DOrder1("testProjector_rank1_fast_reduced"))
      pass

   s=unittest.TextTestRunner(verbosity=2).run(suite)
   if not s.wasSuccessful(): sys.exit(1)

