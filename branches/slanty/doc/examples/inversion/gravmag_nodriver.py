##############################################################################
#
# Copyright (c) 2012-2013 by University of Queensland
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

"""
Advanced 3D gravity/magnetic joint inversion example without using any
inversion drivers
"""

__copyright__="""Copyright (c) 2012-2013 by University of Queensland
http://www.uq.edu.au
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"

# Import required modules
import numpy as np
from esys.downunder import *
from esys.escript import unitsSI as U
from esys.escript import *
from esys.weipa import *

# Set parameters
MAGNETIC_DATASET = 'data/MagneticSmall.nc'
MAG_UNITS = U.Nano * U.V * U.sec / (U.m**2)
GRAVITY_DATASET = 'data/GravitySmall.nc'
GRAV_UNITS = 1e-6 * U.m/(U.sec**2)
latitude=-20.5

thickness = 40. * U.km # below surface
l_air = 6. * U.km      # above surface
n_cells_v = 25         # number of cells in vertical direction

# apply 20% padding
PAD_X = 0.2
PAD_Y = 0.2

MU_GRAVITY = 10.
MU_MAGNETIC = 0.1

# read data:
source_g=NetCdfData(NetCdfData.GRAVITY, GRAVITY_DATASET, scale_factor=GRAV_UNITS)
source_m=NetCdfData(NetCdfData.MAGNETIC, MAGNETIC_DATASET, scale_factor=MAG_UNITS)
B_b=simpleGeoMagneticFluxDensity(latitude=latitude)

# create domain:
db=DomainBuilder(dim=3)
db.addSource(source_g)
db.addSource(source_m)
db.setVerticalExtents(depth=thickness, air_layer=l_air, num_cells=n_cells_v)
db.setFractionalPadding(pad_x=PAD_X, pad_y=PAD_Y)
db.fixDensityBelow(depth=thickness)
db.fixSusceptibilityBelow(depth=thickness)

dom=db.getDomain()
DIM=dom.getDim()

# create mappings with standard parameters
rho_mapping=DensityMapping(dom)
k_mapping=SusceptibilityMapping(dom)

# create regularization with two level set functions:
reg_mask=Data(0.,(2,), Solution(dom))
reg_mask[0] = db.getSetDensityMask()        # mask for locations where m[0]~rho is known
reg_mask[1] = db.getSetSusceptibilityMask() # mask for locations where m[0]~k is known
regularization=Regularization(dom, numLevelSets=2,
                               w1=np.ones((2,DIM)), # consider gradient terms
                               wc=[[0,1],[0,0]],    # and cross-gradient term
                               location_of_set_m=reg_mask)

# create forward model for gravity
# get data with deviation
g,sigma_g=db.getGravitySurveys()[0]
# turn the scalars into vectors (vertical direction)
d=kronecker(DIM)[DIM-1]
w=safeDiv(1., sigma_g)

gravity_model=GravityModel(dom, w*d, g*d)
gravity_model.rescaleWeights(rho_scale=rho_mapping.getTypicalDerivative())

# create forward model for magnetic
d=normalize(np.array(B_b)) # direction of measurement
B,sigma_B=db.getMagneticSurveys()[0]
w=safeDiv(1., sigma_B)

magnetic_model=MagneticModel(dom, w*d, B*d, B_b)
magnetic_model.rescaleWeights(k_scale=k_mapping.getTypicalDerivative())


# finally we can set up the cost function:
cf=InversionCostFunction(regularization,
             ((rho_mapping,0), (k_mapping, 1)),
             ((gravity_model,0), (magnetic_model,1)) )

cf.setTradeOffFactorsModels([MU_GRAVITY, MU_MAGNETIC])

# sun solver:
solver=MinimizerLBFGS()
solver.setCostFunction(cf)
solver.setTolerance(1e-4)
solver.setMaxIterations(50)
solver.run(Data(0.,(2,),Solution(dom)))
m=solver.getResult()
density, susceptibility = cf.getProperties(m)


# write everything to file:
saveSilo("result_gravmag.silo",
         density=density, susceptability=susceptibility,
         g_data=g, sigma_g=sigma_g, B_data=B, sigma_B=sigma_B)
saveVTK("result_gravmag.vtu",
         density=density, susceptability=susceptibility,
         g_data=g, sigma_g=sigma_g, B_data=B, sigma_B=sigma_B)

print("All done. Have a nice day!")
