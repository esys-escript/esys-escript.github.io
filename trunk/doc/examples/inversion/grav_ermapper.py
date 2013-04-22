
##############################################################################
#
# Copyright (c) 2009-2013 by University of Queensland
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

"""3D gravity inversion example using ER Mapper data"""

__copyright__="""Copyright (c) 2009-2013 by University of Queensland
http://www.uq.edu.au
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"

# Import required modules
from esys.downunder import *
from esys.weipa import *
from esys.escript import unitsSI as U
from esys.escript import saveDataCSV

# Set parameters
DATASET = 'data/GravitySmall.ers'
DATA_UNITS = 1e-6 * U.m/(U.sec**2)
PAD_X = 0.2
PAD_Y = 0.2
thickness = 40. * U.km
l_air = 6. * U.km
n_cells_v = 25
MU = 0.1
#COORDINATES=CartesianReferenceSystem()
COORDINATES=GRS80ReferenceSystem()

def work():
  # Setup and run the inversion
  source=ErMapperData(DataSource.GRAVITY, DATASET, scale_factor=DATA_UNITS, reference_system=COORDINATES)
  db=DomainBuilder(dim=3, reference_system=COORDINATES)
  db.addSource(source)
  db.setVerticalExtents(depth=thickness, air_layer=l_air, num_cells=n_cells_v)
  db.setFractionalPadding(pad_x=PAD_X, pad_y=PAD_Y)
  db.fixDensityBelow(depth=thickness)

  inv=GravityInversion()
  inv.setSolverTolerance(1e-4)
  inv.setSolverMaxIterations(50)
  inv.setup(db)
  inv.getCostFunction().setTradeOffFactorsModels(MU)

  density = inv.run()
  print("density = %s"%density)

  g, w =  db.getGravitySurveys()[0]
  saveSilo("result0.silo", density=density, gravity_anomaly=g, gravity_weight=w)
  print("Results saved in result0.silo")

  saveVTK("result0.vtu", density=density, gravity_anomaly=g, gravity_weight=w)
  print("Results saved in result0.vtu")

  saveDataCSV("result0.csv", density=density, x=density.getFunctionSpace().getX())
  print("Results saved in result0.csv")

  print("All done. Have a nice day.!")

try:
  import pyproj
  havepyproj=True
except ImportError:
  havepyproj=False

if havepyproj:
  work()
else:
  print("This example requires the pyproj package which does not appear to be accessible.")
