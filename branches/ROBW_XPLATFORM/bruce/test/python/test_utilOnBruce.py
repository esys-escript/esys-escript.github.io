# $Id$

import unittest
from esys.escript.test_util import Test_util_no_tagged_data as Test_util
from esys.escript.test_symbols import Test_symbols
from esys.escript import ContinuousFunction
from esys.finley import Rectangle
import sys

class Test_UtilOnBruce(Test_util,Test_symbols):
   def setUp(self):
       self.domain =Rectangle(10,10,2)
       self.functionspace = ContinuousFunction(self.domain)

if __name__ == '__main__':
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(Test_UtilOnBruce))
   s=unittest.TextTestRunner(verbosity=2).run(suite)
   if s.wasSuccessful():
     sys.exit(0)
   else:
     sys.exit(1)
   