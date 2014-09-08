#
# $Id$
#
#######################################################
#
#           Copyright 2003-2007 by ACceSS MNRF
#       Copyright 2007 by University of Queensland
#
#                http://esscc.uq.edu.au
#        Primary Business: Queensland, Australia
#  Licensed under the Open Software License version 3.0
#     http://www.opensource.org/licenses/osl-3.0.php
#
#######################################################
#

"""General test environment to test the solvers for scalar and vector equations 

   test parameters are 

     numDim = spatial dimension 
     totalNumElem = number of func in each direction 
     problem = solveScalar,solveVector

     solver_method = true/false 
     len_x0 = length of the domain in x0 direction (number of func in x0 is round(totalNumElem*len_x0) )
     alpha = a parameter of the PDE (not well defined yet)

"""

__copyright__="""  Copyright (c) 2006 by ACcESS MNRF
                    http://www.access.edu.au
                Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
             http://www.opensource.org/licenses/osl-3.0.php"""
from esys.escript import *
from esys.escript.linearPDEs import *
import esys.finley as pdelib
from time import time

from numarray import *

# these values are currently fixed:
len_x0=1.
alpha=10.
tm=0

#############################################################################################################3
def solveVector(numDim, totalNumElem, len_x0, alpha, solver_method,prec):
    
    if prec=="":
        prec_id=0
    else:
       prec_id=eval("LinearPDE.%s"%prec)
    solver_method_id=eval("LinearPDE.%s"%solver_method)
    print "Vector solver:"
    recDim=array([len_x0,1.,1.])
    # Define Computational Domain
    numElem=int((totalNumElem/(len_x0*1.))**(1./numDim))
    elemDim = array([int(len_x0*numElem), numElem, numElem],Int)

    # Set Mesh
    if (numDim == 2):
        mesh = pdelib.Rectangle(elemDim[0], elemDim[1], 2, \
                         l0 = len_x0, l1 = 1.)
        totElem=elemDim[0]*elemDim[1]
    elif (numDim == 3):
        mesh = pdelib.Brick(elemDim[0], elemDim[1], elemDim[2], 2, \
                     l0 = len_x0, l1 = 1., l2 = 1.)
        totElem=elemDim[0]*elemDim[1]*elemDim[2]

    print "  length of domain: ",recDim[:numDim]
    print "  requested elements: ",totalNumElem
    print "  num elements:  ",totElem
    # Set Mesh Descriptors
    meshDim = mesh.getDim()
    contfunc = ContinuousFunction(mesh)
    func = Function(mesh)
    x = contfunc.getX()

    # Set Boundary Mask / pdelib Template "q" Parameter Vector
    bndryMask = Vector(value = 0, what = contfunc)
    for i in range(meshDim):
        bndryMask += (whereZero(x[i]) + whereZero(x[i]-recDim[i])) \
                * ones((numDim,))

    # Set True Solution / pdelib Template "r" Parameter Vector
    u = Vector(value = 0, what = contfunc)
    for i in range(meshDim):
        for j in range(meshDim - 1):
            u[i] += x[(i + j + 1) % meshDim]**2
    # Set pdelib Template "A" Parameter Tensor
    A = Tensor4(value = 0, what = func)
    for i in range(meshDim):
      for j in range(meshDim):
        A[i,i,j,j] += 1.
        A[i,j,j,i] += alpha 
        A[i,j,i,j] += alpha 

    # Build the pdelib System Matrix and RHS
    mypde=LinearPDE(mesh)
    mypde.setValue(A = A, Y = - 2 * alpha * (meshDim - 1)*ones(meshDim), q = bndryMask, r = u)
    mypde.setSolverMethod(solver_method_id)
    # mypde.getOperator().saveMM("g.mm")

    # Solve for Approximate Solution
    tm=time()
    u_approx = mypde.getSolution(verbose=True,preconditioner=prec_id,iter_max=10000)
    tm=time()-tm

    # Report Results
    error=Lsup(u - u_approx)/Lsup(u)
    print "@@ Vector %d : %d : %s(%s): error L^sup Norm : %e, time %e"%(mypde.getDim(),totElem,solver_method,prec,error,tm)
  
    return error

#################################################################################################################

def solveScalar(numDim, totalNumElem, len_x0, alpha, solver_method,prec):

    if prec=="":
        prec_id=0
    else:
       prec_id=eval("LinearPDE.%s"%prec)
    solver_method_id=eval("LinearPDE.%s"%solver_method)
    print "Scalar solver:"
    recDim=array([len_x0,1.,1.])
    # Define Computational Domain
    numElem=int((totalNumElem/(len_x0*1.))**(1./numDim))
    elemDim = array([int(len_x0*numElem), numElem, numElem],Int)
    # Set Mesh
    if (numDim == 2):
        mesh = pdelib.Rectangle(elemDim[0], elemDim[1], 2, \
                         l0 = len_x0, l1 = 1.)
        totElem=elemDim[0]*elemDim[1]
    elif (numDim == 3):
        mesh = pdelib.Brick(elemDim[0], elemDim[1], elemDim[2], 2, \
                     l0 = len_x0, l1 = 1., l2 = 1.)
        totElem=elemDim[0]*elemDim[1]*elemDim[2]

    print "  length of domain: ",recDim[:numDim]
    print "  requested elements: ",totalNumElem
    print "  num elements:  ",totElem

    # Set Mesh Descriptors
    meshDim = mesh.getDim()
    contfunc = ContinuousFunction(mesh)
    func = Function(mesh)
    x = contfunc.getX()

    # Set Boundary Mask / pdelib Template "q" Parameter Vector
    bndryMask = Scalar(value = 0, what = contfunc)
    for i in range(meshDim):
        bndryMask += (whereZero(x[i]) + whereZero(x[i]-recDim[i])) * 1.0

    # Set True Solution / pdelib Template "r" Parameter Vector
    u = Scalar(value = 0, what = contfunc)
    for j in range(meshDim):
        u += x[j] * x[j]

    # Build the pdelib System Matrix and RHS
    mypde=LinearPDE(mesh)
    mypde.setValue(A = identity(numDim), D = alpha, Y = alpha * u - 2 * meshDim, q = bndryMask, r = u)
    mypde.setSolverMethod(solver_method_id)

    # Solve for Approximate Solution
    tm=time()
    u_approx = mypde.getSolution(verbose=True,preconditioner=prec_id,iter_max=10000)
    tm=time()-tm

    # Report Results
    error=Lsup(u - u_approx)/Lsup(u)
    print "@@ Scalar %d : %d : %s(%s): error L^sup Norm : %e, time %e"%(mypde.getDim(),totElem,solver_method,prec,error,tm)
  
    return error

#######################################################################################


print "Test is started:"
print "----------------"
error=0.
for numDim in [2, 3]:
   # for totalNumElem in [51200]:
   for totalNumElem in [100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400,204800]:
      for problem in [solveScalar,solveVector]:
      #for problem in [solveVector]:
         error=max([problem(numDim, totalNumElem, len_x0, alpha,"PCG",""),error])
         error=max([problem(numDim, totalNumElem, len_x0, alpha,"DIRECT",""),error])
         #if totalNumElem*2**numDim*numDim< 200000: error=max([problem(numDim, totalNumElem, len_x0, alpha,"DIRECT",""),error])
         # for solver_method in [ "PCG" ]:
         #    for prec in [ "JACOBI", "ILU0" ]:
         #       error=max([problem(numDim, totalNumElem, len_x0, alpha, solver_method,prec),error])
print "----------------"
print "maximum error over all tests is ",error
print "----------------"