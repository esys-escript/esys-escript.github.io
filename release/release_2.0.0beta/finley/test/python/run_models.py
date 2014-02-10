
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

import unittest
import tempfile
      
from esys.escript import *
from esys.finley import Rectangle
from esys.escript.models import DarcyFlow
import sys
import os
try:
     FINLEY_WORKDIR=os.environ['FINLEY_WORKDIR']
except KeyError:
     FINLEY_WORKDIR='.'


VERBOSE=False # or True

from esys.escript import *
from esys.escript.models import StokesProblemCartesian
from esys.finley import Rectangle, Brick

#====================================================================================================================
class Test_StokesProblemCartesian2D(unittest.TestCase):
   def setUp(self):
       NE=6
       self.TOL=1.e-5
       self.domain=Rectangle(NE,NE,order=2,useFullElementOrder=True)
   def tearDown(self):
       del self.domain
   def test_PCG_P_0(self):
       ETA=1.
       P1=0.

       x=self.domain.getX()
       F=-P1*x[1]*[1.,0]+(2*ETA-P1*x[0])*[0.,1.]
       mask=whereZero(x[0])    * [1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.] \
              +whereZero(x[1])    * [1.,0.] \
              +whereZero(x[1]-1)  * [1.,1.]
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*[0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(self.TOL)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=100,useUzawa=True)
       
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])/0.25
       error_p=Lsup(p+P1*x[0]*x[1])
       self.failUnless(error_p<10*self.TOL, "pressure error too large.")
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")

   def test_PCG_P_small(self):
       ETA=1.
       P1=1.

       x=self.domain.getX()
       F=-P1*x[1]*[1.,0]+(2*ETA-P1*x[0])*[0.,1.]
       mask=whereZero(x[0])    * [1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.] \
              +whereZero(x[1])    * [1.,0.] \
              +whereZero(x[1]-1)  * [1.,1.]
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*[0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(self.TOL)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE or True,max_iter=100,useUzawa=True)
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])/0.25
       error_p=Lsup(P1*x[0]*x[1]+p)
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")
       self.failUnless(error_p<11*self.TOL, "pressure error too large.")

   def test_PCG_P_large(self):
       ETA=1.
       P1=1000.

       x=self.domain.getX()
       F=-P1*x[1]*[1.,0]+(2*ETA-P1*x[0])*[0.,1.]
       mask=whereZero(x[0])    * [1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.] \
              +whereZero(x[1])    * [1.,0.] \
              +whereZero(x[1]-1)  * [1.,1.]
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*[0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(self.TOL)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=100,useUzawa=True)
       
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])/0.25
       error_p=Lsup(P1*x[0]*x[1]+p)/P1
       self.failUnless(error_p<10*self.TOL, "pressure error too large.")
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")

   def test_GMRES_P_0(self):
       ETA=1.
       P1=0.

       x=self.domain.getX()
       F=-P1*x[1]*[1.,0]+(2*ETA-P1*x[0])*[0.,1.]
       mask=whereZero(x[0])    * [1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.] \
              +whereZero(x[1])    * [1.,0.] \
              +whereZero(x[1]-1)  * [1.,1.]
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*[0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(self.TOL)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=50,useUzawa=False,iter_restart=18)
       # u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=100,useUzawa=False,iter_restart=20)
       
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])/0.25
       zz=P1*x[0]*x[1]+p
       error_p=Lsup(zz-integrate(zz))
       self.failUnless(error_p<10*self.TOL, "pressure error too large.")
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")

   def test_GMRES_P_small(self):
       ETA=1.
       P1=1.

       x=self.domain.getX()
       F=-P1*x[1]*[1.,0]+(2*ETA-P1*x[0])*[0.,1.]
       mask=whereZero(x[0])    * [1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.] \
              +whereZero(x[1])    * [1.,0.] \
              +whereZero(x[1]-1)  * [1.,1.]
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*[0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(self.TOL*0+1.e-6)
       # sp.setSubToleranceReductionFactor(0.1)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=20,useUzawa=False)
       
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])/0.25
       zz=P1*x[0]*x[1]+p
       error_p=Lsup(zz-integrate(zz))
       # print error_p, error_v0,error_v1
       self.failUnless(error_p<10*self.TOL, "pressure error too large.")
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")

   def test_GMRES_P_large(self):
       ETA=1.
       P1=1000.

       x=self.domain.getX()
       F=-P1*x[1]*[1.,0]+(2*ETA-P1*x[0])*[0.,1.]
       mask=whereZero(x[0])    * [1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.] \
              +whereZero(x[1])    * [1.,0.] \
              +whereZero(x[1]-1)  * [1.,1.]
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*[0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(self.TOL)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=100,useUzawa=False)
       
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])/0.25
       zz=P1*x[0]*x[1]+p
       error_p=Lsup(zz-integrate(zz))/P1
       self.failUnless(error_p<10*self.TOL, "pressure error too large.")
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")
#====================================================================================================================
class Test_StokesProblemCartesian3D(unittest.TestCase):
   def setUp(self):
       NE=6
       self.TOL=1.e-4
       self.domain=Brick(NE,NE,NE,order=2,useFullElementOrder=True)
   def tearDown(self):
       del self.domain
   def test_PCG_P_0(self):
       ETA=1.
       P1=0.

       x=self.domain.getX()
       F=-P1*x[1]*x[2]*[1.,0.,0.]-P1*x[0]*x[2]*[0.,1.,0.]+(2*ETA*((1-x[0])*x[0]+(1-x[1])*x[1])-P1*x[0]*x[1])*[0.,0.,1.]
       x=self.domain.getX()
       mask=whereZero(x[0])    * [1.,1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.,1.] \
              +whereZero(x[1])    * [1.,1.,1.] \
              +whereZero(x[1]-1)  * [1.,1.,1.] \
              +whereZero(x[2])    * [1.,1.,0.] \
              +whereZero(x[2]-1)  * [1.,1.,1.]
       
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*(1-x[1])*x[1]*[0.,0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(1.e-8)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=100,useUzawa=True)
       
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])
       error_v2=Lsup(u[2]-u0[2])/0.25**2
       zz=P1*x[0]*x[1]*x[2]+p
       error_p=Lsup(zz-integrate(zz))
       # print error_p, error_v0,error_v1,error_v2
       self.failUnless(error_p<10*self.TOL, "pressure error too large.")
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")
       self.failUnless(error_v2<10*self.TOL, "2-velocity error too large.")

   def test_PCG_P_small(self):
       ETA=1.
       P1=1.

       x=self.domain.getX()
       F=-P1*x[1]*x[2]*[1.,0.,0.]-P1*x[0]*x[2]*[0.,1.,0.]+(2*ETA*((1-x[0])*x[0]+(1-x[1])*x[1])-P1*x[0]*x[1])*[0.,0.,1.]
       mask=whereZero(x[0])    * [1.,1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.,1.] \
              +whereZero(x[1])    * [1.,1.,1.] \
              +whereZero(x[1]-1)  * [1.,1.,1.] \
              +whereZero(x[2])    * [1.,1.,0.] \
              +whereZero(x[2]-1)  * [1.,1.,1.]
       
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*(1-x[1])*x[1]*[0.,0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(1.e-8)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=100,useUzawa=True)
       
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])
       error_v2=Lsup(u[2]-u0[2])/0.25**2
       zz=P1*x[0]*x[1]*x[2]+p
       error_p=Lsup(zz-integrate(zz))/P1
       self.failUnless(error_p<10*self.TOL, "pressure error too large.")
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")
       self.failUnless(error_v2<10*self.TOL, "2-velocity error too large.")
   def test_PCG_P_large(self):
       ETA=1.
       P1=1000.

       x=self.domain.getX()
       F=-P1*x[1]*x[2]*[1.,0.,0.]-P1*x[0]*x[2]*[0.,1.,0.]+(2*ETA*((1-x[0])*x[0]+(1-x[1])*x[1])-P1*x[0]*x[1])*[0.,0.,1.]
       mask=whereZero(x[0])    * [1.,1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.,1.] \
              +whereZero(x[1])    * [1.,1.,1.] \
              +whereZero(x[1]-1)  * [1.,1.,1.] \
              +whereZero(x[2])    * [1.,1.,0.] \
              +whereZero(x[2]-1)  * [1.,1.,1.]
       
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*(1-x[1])*x[1]*[0.,0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(1.e-8)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=100,useUzawa=True)
       
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])
       error_v2=Lsup(u[2]-u0[2])/0.25**2
       zz=P1*x[0]*x[1]*x[2]+p
       error_p=Lsup(zz-integrate(zz))/P1
       # print error_p, error_v0,error_v1,error_v2
       self.failUnless(error_p<10*self.TOL, "pressure error too large.")
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")
       self.failUnless(error_v2<10*self.TOL, "2-velocity error too large.")

   def test_GMRES_P_0(self):
       ETA=1.
       P1=0.

       x=self.domain.getX()
       F=-P1*x[1]*x[2]*[1.,0.,0.]-P1*x[0]*x[2]*[0.,1.,0.]+(2*ETA*((1-x[0])*x[0]+(1-x[1])*x[1])-P1*x[0]*x[1])*[0.,0.,1.]
       x=self.domain.getX()
       mask=whereZero(x[0])    * [1.,1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.,1.] \
              +whereZero(x[1])    * [1.,1.,1.] \
              +whereZero(x[1]-1)  * [1.,1.,1.] \
              +whereZero(x[2])    * [1.,1.,0.] \
              +whereZero(x[2]-1)  * [1.,1.,1.]
       
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*(1-x[1])*x[1]*[0.,0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(1.e-8)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=100,useUzawa=False,iter_restart=20)
       
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])
       error_v2=Lsup(u[2]-u0[2])/0.25**2
       zz=P1*x[0]*x[1]*x[2]+p
       error_p=Lsup(zz-integrate(zz))
       # print error_p, error_v0,error_v1,error_v2
       self.failUnless(error_p<10*self.TOL, "pressure error too large.")
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")
       self.failUnless(error_v2<10*self.TOL, "2-velocity error too large.")
   def test_GMRES_P_small(self):
       ETA=1.
       P1=1.

       x=self.domain.getX()
       F=-P1*x[1]*x[2]*[1.,0.,0.]-P1*x[0]*x[2]*[0.,1.,0.]+(2*ETA*((1-x[0])*x[0]+(1-x[1])*x[1])-P1*x[0]*x[1])*[0.,0.,1.]
       mask=whereZero(x[0])    * [1.,1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.,1.] \
              +whereZero(x[1])    * [1.,1.,1.] \
              +whereZero(x[1]-1)  * [1.,1.,1.] \
              +whereZero(x[2])    * [1.,1.,0.] \
              +whereZero(x[2]-1)  * [1.,1.,1.]
       
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*(1-x[1])*x[1]*[0.,0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(1.e-8)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=100,useUzawa=False)
       
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])
       error_v2=Lsup(u[2]-u0[2])/0.25**2
       zz=P1*x[0]*x[1]*x[2]+p
       error_p=Lsup(zz-integrate(zz))/P1
       # print error_p, error_v0,error_v1,error_v2
       self.failUnless(error_p<10*self.TOL, "pressure error too large.")
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")
       self.failUnless(error_v2<10*self.TOL, "2-velocity error too large.")
   def test_GMRES_P_large(self):
       ETA=1.
       P1=1000.

       x=self.domain.getX()
       F=-P1*x[1]*x[2]*[1.,0.,0.]-P1*x[0]*x[2]*[0.,1.,0.]+(2*ETA*((1-x[0])*x[0]+(1-x[1])*x[1])-P1*x[0]*x[1])*[0.,0.,1.]
       mask=whereZero(x[0])    * [1.,1.,1.] \
              +whereZero(x[0]-1)  * [1.,1.,1.] \
              +whereZero(x[1])    * [1.,1.,1.] \
              +whereZero(x[1]-1)  * [1.,1.,1.] \
              +whereZero(x[2])    * [1.,1.,0.] \
              +whereZero(x[2]-1)  * [1.,1.,1.]
       
       
       sp=StokesProblemCartesian(self.domain)
       
       sp.initialize(f=F,fixed_u_mask=mask,eta=ETA)
       u0=(1-x[0])*x[0]*(1-x[1])*x[1]*[0.,0.,1.]
       p0=Scalar(P1,ReducedSolution(self.domain))
       sp.setTolerance(self.TOL+0*1.e-8)
       # sp.setSubToleranceReductionFactor(1.e-8/self.TOL)
       # sp.setSubToleranceReductionFactor(None)
       u,p=sp.solve(u0,p0,show_details=VERBOSE, verbose=VERBOSE,max_iter=100,useUzawa=False)
       
       error_v0=Lsup(u[0]-u0[0])
       error_v1=Lsup(u[1]-u0[1])
       error_v2=Lsup(u[2]-u0[2])/0.25**2
       zz=P1*x[0]*x[1]*x[2]+p
       error_p=Lsup(zz-integrate(zz))/P1
       # print error_p, error_v0,error_v1,error_v2
       self.failUnless(error_p<10*self.TOL, "pressure error too large.")
       self.failUnless(error_v0<10*self.TOL, "0-velocity error too large.")
       self.failUnless(error_v1<10*self.TOL, "1-velocity error too large.")
       self.failUnless(error_v2<10*self.TOL, "2-velocity error too large.")
#====================================================================================================================
class Test_Darcy(unittest.TestCase):
    # this is a simple test for the darcy flux problem
    #
    # 
    #  p = 1/k * ( 1/2* (fb-f0)/xb* x **2 + f0 * x - ub*x ) +  p0
    # 
    #  with f = (fb-f0)/xb* x + f0 
    #
    #    u = f - k * p,x = ub
    #
    #  we prescribe pressure at x=x0=0 to p0
    # 
    #  if we prescribe the pressure on the bottom x=xb we set
    # 
    #  pb= 1/k * ( 1/2* (fb-f0)* xb + f0 * xb - ub*xb ) +  p0 = 1/k * ((fb+f0)/2 - ub ) * xb  + p0
    # 
    #  which leads to ub = (fb+f0)/2-k*(pb-p0)/xb
    #
    def rescaleDomain(self):
        x=self.dom.getX().copy()
        for i in xrange(self.dom.getDim()):
             x_inf=inf(x[i])
             x_sup=sup(x[i])
             if i == self.dom.getDim()-1:
                x[i]=-self.WIDTH*(x[i]-x_sup)/(x_inf-x_sup)
             else:
                x[i]=self.WIDTH*(x[i]-x_inf)/(x_sup-x_inf)
        self.dom.setX(x)
    def getScalarMask(self,include_bottom=True):
        x=self.dom.getX().copy()
        x_inf=inf(x[self.dom.getDim()-1])
        x_sup=sup(x[self.dom.getDim()-1])
        out=whereZero(x[self.dom.getDim()-1]-x_sup)
        if include_bottom: out+=whereZero(x[self.dom.getDim()-1]-x_inf)
        return wherePositive(out)
    def getVectorMask(self,include_bottom=True):
        x=self.dom.getX().copy()
        out=Vector(0.,Solution(self.dom))
        for i in xrange(self.dom.getDim()):
             x_inf=inf(x[i])
             x_sup=sup(x[i])
             if i != self.dom.getDim()-1: out[i]+=whereZero(x[i]-x_sup)
             if i != self.dom.getDim()-1 or include_bottom: out[i]+=whereZero(x[i]-x_inf)
        return wherePositive(out)

    def setSolutionFixedBottom(self, p0, pb, f0, fb, k):
         d=self.dom.getDim()
         x=self.dom.getX()[d-1]
         xb=inf(x)
         u=Vector(0.,Solution(self.dom))+kronecker(d)[d-1]*((f0+fb)/2.-k*(pb-p0)/xb)
         p=1./k*((fb-f0)/(xb*2.)* x**2 - (fb-f0)/2.*x)+(pb-p0)/xb*x +  p0
         f= ((fb-f0)/xb* x + f0)*kronecker(Function(self.dom))[d-1]
         return u,p,f
        
    def testConstF_FixedBottom_smallK(self):
        k=1.e-10
        mp=self.getScalarMask(include_bottom=True)
        mv=self.getVectorMask(include_bottom=False)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=10.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

    def testConstF_FixedBottom_mediumK(self):
        k=1.
        mp=self.getScalarMask(include_bottom=True)
        mv=self.getVectorMask(include_bottom=False)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=10.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

    def testConstF_FixedBottom_largeK(self):
        k=1.e10
        mp=self.getScalarMask(include_bottom=True)
        mv=self.getVectorMask(include_bottom=False)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=10.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

    def testVarioF_FixedBottom_smallK(self):
        k=1.e-10
        mp=self.getScalarMask(include_bottom=True)
        mv=self.getVectorMask(include_bottom=False)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=30.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

    def testVarioF_FixedBottom_mediumK(self):
        k=1.
        mp=self.getScalarMask(include_bottom=True)
        mv=self.getVectorMask(include_bottom=False)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=30.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

    def testVarioF_FixedBottom_largeK(self):
        k=1.e10
        mp=self.getScalarMask(include_bottom=True)
        mv=self.getVectorMask(include_bottom=False)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=30.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

    def testConstF_FreeBottom_smallK(self):
        k=1.e-10
        mp=self.getScalarMask(include_bottom=False)
        mv=self.getVectorMask(include_bottom=True)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=10.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

    def testConstF_FreeBottom_mediumK(self):
        k=1.
        mp=self.getScalarMask(include_bottom=False)
        mv=self.getVectorMask(include_bottom=True)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=10.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

    def testConstF_FreeBottom_largeK(self):
        k=1.e10
        mp=self.getScalarMask(include_bottom=False)
        mv=self.getVectorMask(include_bottom=True)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=10.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

    def testVarioF_FreeBottom_smallK(self):
        k=1.e-10
        mp=self.getScalarMask(include_bottom=False)
        mv=self.getVectorMask(include_bottom=True)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=30.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

    def testVarioF_FreeBottom_mediumK(self):
        k=1.
        mp=self.getScalarMask(include_bottom=False)
        mv=self.getVectorMask(include_bottom=True)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=30.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

    def testVarioF_FreeBottom_largeK(self):
        k=1.e10
        mp=self.getScalarMask(include_bottom=False)
        mv=self.getVectorMask(include_bottom=True)
        u_ref,p_ref,f=self.setSolutionFixedBottom(p0=2500,pb=4000.,f0=10.,fb=30.,k=k)
        p=p_ref*mp
        u=u_ref*mv
        df=DarcyFlow(self.dom)
        df.setValue(g=f,
                      location_of_fixed_pressure=mp,
                      location_of_fixed_flux=mv,
                      permeability=Scalar(k,Function(self.dom)))
        v,p=df.solve(u,p,atol=0,rtol=self.TOL, max_iter=100, verbose=VERBOSE,sub_rtol=self.TOL/200)
        self.failUnless(Lsup(v-u_ref)<self.TOL*10.*Lsup(u_ref), "flux error too big.")
        self.failUnless(Lsup(p-p_ref)<self.TOL*10.*Lsup(p_ref), "pressure error too big.")

class Test_Darcy2D(Test_Darcy):
    TOL=1e-5
    WIDTH=1.
    def setUp(self):
        NE=60  # wrning smaller NE may case a failure for VarioF tests due to discretization errors.
        self.dom = Rectangle(NE,NE)
        self.rescaleDomain()
    def tearDown(self):
        del self.dom
class Test_Darcy3D(Test_Darcy):
    TOL=1e-4
    WIDTH=1.
    def setUp(self):
        NE=25  # wrning smaller NE may case a failure for VarioF tests due to discretization errors.
        self.dom = Brick(NE,NE,NE)
        self.rescaleDomain()
    def tearDown(self):
        del self.dom



if __name__ == '__main__':
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(Test_StokesProblemCartesian2D))
   suite.addTest(unittest.makeSuite(Test_Darcy3D))
   suite.addTest(unittest.makeSuite(Test_Darcy2D))
   suite.addTest(unittest.makeSuite(Test_StokesProblemCartesian3D))
   s=unittest.TextTestRunner(verbosity=2).run(suite)
   if not s.wasSuccessful(): sys.exit(1)
