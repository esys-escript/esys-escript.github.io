
########################################################
#
# Copyright (c) 2003-2012 by University of Queensland
# Earth Systems Science Computational Center (ESSCC)
# http://www.uq.edu.au/esscc
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
########################################################

__copyright__="""Copyright (c) 2003-2012 by University of Queensland
Earth Systems Science Computational Center (ESSCC)
http://www.uq.edu.au/esscc
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"

import logging
import os
from esys.escript import unitsSI as U
from esys.downunder.datasources import SyntheticDataSource,SmoothAnomaly
from esys.downunder.inversions import GravityInversion


try: 
   WORKDIR=os.environ['DOWNUNDER_WORKDIR']
except KeyError:
   WORKDIR='.'

features=[SmoothAnomaly(lx=50*U.km, ly=20*U.km, lz=40*U.km, \
     x=100*U.km, y=3*U.km, depth=25*U.km, rho_inner=200., rho_outer=1e-6),\
          SmoothAnomaly(lx=50*U.km, ly=20*U.km, lz=40*U.km,
     x=400*U.km, y=1*U.km, depth=40*U.km, rho_inner=-200, rho_outer=1e-6)]

logger=logging.getLogger('inv')
logger.setLevel(logging.INFO)
handler=logging.StreamHandler()
handler.setLevel(logging.INFO)
logger.addHandler(handler)
source=SyntheticDataSource(DIM=2, NE=20, l=500*U.km, h=60*U.km, features=features)
source.setPadding(5, 0.1)
inv=GravityInversion()
inv.setDataSource(source)
inv.setSolverTolerance(1e-5)
inv.setSolverMaxIterations(100)
inv.setSolverOptions(initialHessian=100)
inv.setup()
rho_new=inv.run()

