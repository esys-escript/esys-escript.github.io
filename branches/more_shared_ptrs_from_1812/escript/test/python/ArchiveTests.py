
########################################################
#
# Copyright (c) 2003-2008 by University of Queensland
# Earth Systems Science Computational Center (ESSCC)
# http://www.uq.edu.au/esscc
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
########################################################

__copyright__="""Copyright (c) 2003-2008 by University of Queensland
Earth Systems Science Computational Center (ESSCC)
http://www.uq.edu.au/esscc
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="http://www.uq.edu.au/esscc/escript-finley"

"""

Miscellaneous escript/Data tests.

"""

import sys
import unittest
import os

from esys.escript import *
from esys import bruce
from esys import finley

import numarray
from numarray import array,Float64,ones,greater

#
# ==============================================================

print "\n\n"

mshList=(bruce.Rectangle(),
         bruce.Brick(),
         finley.Rectangle(2, 5, 1, l0 = 7.0, l1 = 11.0),
         finley.Brick(2, 5, 7, 1, l0 = 11.0, l1 = 13.0, l2 = 17.0),
         finley.Rectangle(2, 5, 2, l0 = 7.0, l1 = 11.0),
         finley.Brick(2, 5, 7, 2, l0 = 11.0, l1 = 13.0, l2 = 17.0))

for msh in mshList:

  print "\nX -- Continuous:"
  archDataX = msh.getX()
  archDataX.archiveData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archiveX")
  exDataX=Data()
  exDataX.extractData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archiveX",ContinuousFunction(msh))

  diff = archDataX - exDataX
  (infdiff, supdiff) = (inf(diff), sup(diff))
  if infdiff != 0 or supdiff != 0:
    print "*** ERROR: Data value discrepancies %f < X < %f" \
          % (infdiff, supdiff)
    sys.exit(1)

  exDataX.archiveData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archive2X");

  print "\nDataExpanded:"
  archDataE=Data([[1.00001],[2.00001]],Function(msh),True)
  archDataE.archiveData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archiveE")
  exDataE=Data()
  exDataE.extractData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archiveE",Function(msh))
  exDataE.archiveData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archive2E");

  print "\nDataTagged:"
  archDataT=Data([[1.00001],[2.00001]],Function(msh))
  archDataT.tag()
  archDataT.archiveData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archiveT")
  exDataT=Data()
  exDataT.extractData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archiveT",Function(msh))
  exDataT.archiveData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archive2T");

  print "\nDataConstant:"
  archDataC=Data([1.00001], Function(msh))
  archDataC.archiveData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archiveC")
  exDataC=Data()
  exDataC.extractData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archiveC",Function(msh))
  exDataC.archiveData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archive2C");

  print "\nDataEmpty:"
  archDataM=Data()
  archDataM.archiveData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archiveE")
  exDataM=Data()
  exDataM.extractData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archiveE",FunctionSpace())
  exDataM.archiveData(os.environ['ESCRIPT_WORKING_DIR']+"/data-archive2E")

sys.exit(0)
# end
