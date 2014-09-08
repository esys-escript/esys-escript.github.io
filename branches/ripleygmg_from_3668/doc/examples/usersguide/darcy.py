
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

from esys.escript import *
from esys.escript.models import DarcyFlow
from esys.finley import Rectangle
from esys.weipa import saveVTK
# generate domain:
mydomain = Rectangle(l0=2.,l1=1.,n0=40, n1=20)
# normal flux is given 
x = mydomain.getX()

# set location of fixed pressure and flux:
p_BC=whereZero(x[1]-1.)*wherePositive(x[0]-1.)
u_BC=(whereZero(x[0])+whereZero(x[0]-2.)) * [1.,0.] + \
     (whereZero(x[1]) + whereZero(x[1]-1.)*whereNonPositive(x[0]-1.0)) * [0., 1.]

# define darcy flow solver:
mypde = DarcyFlow(domain=mydomain)

mypde.setValue(g=[0., 2],
               location_of_fixed_pressure=p_BC,
               location_of_fixed_flux=u_BC,
               permeability=100.)

u,p=mypde.solve(u0=x[1]*[0., -1.], p0=0)

# write u to an external file
saveVTK("u.vtu",flux=u, pressure=p)
