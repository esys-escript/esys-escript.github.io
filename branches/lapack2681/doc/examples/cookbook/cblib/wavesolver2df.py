
########################################################
#
# Copyright (c) 2009 by University of Queensland
# Earth Systems Science Computational Center (ESSCC)
# http://www.uq.edu.au/esscc
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
########################################################

__copyright__="""Copyright (c) 2009 by University of Queensland
Earth Systems Science Computational Center (ESSCC)
http://www.uq.edu.au/esscc
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"

# You can shorten the execution time by reducing variable tend from 60 to 0.5

# Importing all the necessary modules required.
from esys.escript import *
from esys.escript.pdetools import Locator
from esys.escript.linearPDEs import LinearPDE
from esys.finley import Rectangle
from numpy import identity,zeros,ones
import os
from phones import *

########################################################
# subroutine: wavesolver2d
# Can solve a generic 2D wave propagation problem with a
# point source in a homogeneous medium with friction.
# Arguments:
#	domain  : domain to solve over
#	h       : time step
#	tend    : end time
#	lam, mu : lames constants for domain
#	rho	: density of domain
#	U0	: magnitude of source
#	xc	: source location in domain (Vector)
#	savepath: where to output the data files
########################################################
def wavesolver2df(domain,h,tend,lam,mu,rho,U0,xc,savepath):
   x=domain.getX()
   # ... open new PDE ...
   mypde=LinearPDE(domain)
   #mypde.setSolverMethod(LinearPDE.LUMPING)
   mypde.setSymmetryOn()
   kmat = kronecker(domain)
   mypde.setValue(D=kmat)
   b=0.9

   # define small radius around point xc
   # Lsup(x) returns the maximum value of the argument x
   src_radius = 50#2*Lsup(domain.getSize())
   print "src_radius = ",src_radius

   dunit=numpy.array([0.,1.]) # defines direction of point source

   
   # ... set initial values ....
   n=0
   # initial value of displacement at point source is constant (U0=0.01)
   # for first two time steps
   u=U0*(cos(length(x-xc)*3.1415/src_radius)+1)*whereNegative(length(x-xc)-src_radius)*dunit
   u_m1=u
   t=0

   u_pot = cbphones(domain,u,[[0,500],[250,500],[400,500]],2)
   u_pc_x1 = u_pot[0,0]
   u_pc_y1 = u_pot[0,1]
   u_pc_x2 = u_pot[1,0]
   u_pc_y2 = u_pot[1,1]
   u_pc_x3 = u_pot[2,0]
   u_pc_y3 = u_pot[2,1]

   # open file to save displacement at point source
   u_pc_data=open(os.path.join(savepath,'U_pc.out'),'w')
   u_pc_data.write("%f %f %f %f %f %f %f\n"%(t,u_pc_x1,u_pc_y1,u_pc_x2,u_pc_y2,u_pc_x3,u_pc_y3))
 
   while t<tend:
     # ... get current stress ....
     
##OLD WAY
     g=grad(u)
     stress=lam*trace(g)*kmat+mu*(g+transpose(g))
     ### ... get new acceleration ....
     #mypde.setValue(X=-stress)          
     #a=mypde.getSolution()
     ### ... get new displacement ...
     #u_p1=2*u-u_m1+h*h*a
###NEW WAY
     y = ((rho/(-rho-b*h))*(u_m1-2*u))+(((b*h)/(-rho-(b*h)))*-u)
     mypde.setValue(X=-stress*((h*h)/(-rho-h*b)),Y=y)
     u_p1 = mypde.getSolution()
     # ... shift displacements ....
     u_m1=u
     u=u_p1
     #stress = 
     t+=h
     n+=1
     print n,"-th time step t ",t
     u_pot = cbphones(domain,u,[[300.,200.],[500.,200.],[750.,200.]],2)

#     print "u at point charge=",u_pc
     u_pc_x1 = u_pot[0,0]
     u_pc_y1 = u_pot[0,1]
     u_pc_x2 = u_pot[1,0]
     u_pc_y2 = u_pot[1,1]
     u_pc_x3 = u_pot[2,0]
     u_pc_y3 = u_pot[2,1]
           
     # save displacements at point source to file for t > 0
     u_pc_data.write("%f %f %f %f %f %f %f\n"%(t,u_pc_x1,u_pc_y1,u_pc_x2,u_pc_y2,u_pc_x3,u_pc_y3))
 
     # ... save current acceleration in units of gravity and displacements 
     #saveVTK(os.path.join(savepath,"usoln.%i.vtu"%n),acceleration=length(a)/9.81,
     #displacement = length(u), tensor = stress, Ux = u[0] )
     saveVTK(os.path.join(savepath,"tonysol.%i.vtu"%n),output1 = length(u),tensor=stress)

   u_pc_data.close()