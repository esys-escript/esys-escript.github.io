# -*- coding: utf-8 -*-

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
__unknownrl__="https://launchpad.net/escript-finley"

"""
:var __author__: name of author
:var __copyright__: copyrights
:var __license__: licence agreement
:var __unknownrl__: url entry point on documentation
:var __version__: version
:var __date__: date of the version
"""

import numpy
from time import time
from esys.escript.linearPDEs import LinearPDE, IllegalCoefficient, IllegalCoefficientValue
from esys.escript import util, Data, Symbol, Evaluator

__author__="Cihan Altinay"

class iteration_steps_maxReached(Exception):
   """
   Exception thrown if the maximum number of iteration steps is reached.
   """
   pass
class DivergenceDetected(Exception):
   """
   Exception thrown if Newton-Raphson did not converge.
   """
   pass
class InadmissiblePDEOrdering(Exception):
   """
   Exception thrown if the ordering of the PDE equations should be revised.
   """
   pass
   

class NonlinearPDE(object):
    """
    This class is used to define a general nonlinear, steady, second order PDE
    for an unknown function *u* on a given domain defined through a `Domain`
    object.

    For a single PDE having a solution with a single component the nonlinear
    PDE is defined in the following form:

    *-div(X) + Y = 0*

    where *X*,*Y*=f(*u*,*grad(u)*), *div(F)* denotes the divergence of *F* and
    *grad(F)* is the spatial derivative of *F*.

    The coefficients *X* (rank 1) and *Y* (scalar) have to be specified through
    `Symbol` objects.

    The following natural boundary conditions are considered:

    *n[j]*X[j] - y = 0*

    where *n* is the outer normal field. Notice that the coefficient *X*
    is defined in the PDE. The coefficient *y* is a scalar `Symbol`.

    Constraints for the solution prescribe the value of the solution at certain
    locations in the domain. They have the form

    *u=u0* where *q>0*

    *u0* and *q* are each scalar where *q* is the characteristic function
    defining where the constraint is applied. The constraints override any
    other condition set by the PDE or the boundary condition.

    For a system of PDEs and a solution with several components, *u* is rank
    one, while the PDE coefficient *X* is rank two and *Y* and *y* is rank one.

    The PDE is solved by linearising the coefficients and iteratively solving
    the corresponding linear PDE until the error is smaller than a tolerance
    or a maximum number of iterations is reached.

    Typical usage::

        u = Symbol('u', dim=dom.getDim())
        p = NonlinearPDE(dom, u)
        p.setValue(X=grad(u), Y=5*u)
        v = p.getSolution(u=0.)
    """
    DEBUG0=0 # no debug info
    DEBUG1=1 # info on Newton-Raphson solver printed
    DEBUG2=2 # in addition info from linear solver are printed
    DEBUG3=3 # in addition info on linearization printed
    DEBUG4=4 # in addition info on LinearPDE handeling printed.
    def __init__(self,domain,u,debug=0):
        """
        Initializes a new nonlinear PDE.

        :param domain: domain of the PDE
        :type domain: `Domain`
        :param u: The symbol for the unknown PDE function u.
        :type u: `Symbol`
        :param debug: level of debug information to be printed
        """
        self.__COEFFICIENTS = [ "X", "X_reduced", "Y", "Y_reduced", "y", "y_reduced", "y_contact", "y_contact_reduced", "y_dirac" ]

        self.r=Data()
        self._set_coeffs={}
        self._unknown=u
        self._debug=debug
        self._rtol=1e-6
        self._atol=0.
        self._iteration_steps_max=100
        self._omega_min=0.01
        self._quadratic_convergence_limit=0.2
        self._simplified_newton_limit=0.1

        self.dim = domain.getDim()
        if u.getRank()==0:
            numEquations=1
        else:
            numEquations=u.getShape()[0]
        numSolutions=numEquations
        self._lpde=LinearPDE(domain,numEquations,numSolutions,self._debug > self.DEBUG4 )
        
    def __str__(self):
        """
        Returns the string representation of the PDE.

        :return: a simple representation of the PDE
        :rtype: ``str``
        """
        return "<NonlinearPDE %d>"%id(self)
    def getUnknownSymbol(self):
        """
        Returns the symbol of the PDE unknown

        :return: the symbol of the PDE unknown
        :rtype: `Symbol`
        """
        return self._unknown
      
    def trace1(self, text):
        """
        Prints the text message if debug mode is switched on.

        :param text: message to be printed
        :type text: ``string``
        """
        if self._debug > self.DEBUG0:
            print("%s: %s"%(str(self), text))
            
    def trace3(self, text):
        """
        Prints the text message if debug mode level DEBUG3 is switched on.

        :param text: message to be printed
        :type text: ``string``
        """
        if self._debug > self.DEBUG2:
            print("%s: %s"%(str(self), text))

    def getLinearSolverOptions(self):
        """
        Returns the options of the linear PDE solver class.
        """
        return self._lpde.getSolverOptions()

    def setOptions(self, **opts):
        """
        Allows setting options for the nonlinear PDE.
        The supported options are:
          'tolerance' - error tolerance for the Newton method
          'iteration_steps_max'   - maximum number of Newton iterations
          'omega_min'   - minimum relaxation factor
          'atol'   - solution norms less then 'atol' are assumed to be 'atol'.
                     this can be use full if one of your solution is expected to be zero.
          'quadratic_convergence_limit' - if the norm of the Newton-Raphson correction is 
                                          reduced by less then 'quadratic_convergence_limit' 
                                          between two iteration steps quadratic convergence 
                                          is assumed.
          'simplified_newton_limit' - if the norm of the defect is reduced by less then 'simplified_newton_limit'
                                      between two iteration steps and quadratic convergence is detected
                                      the iteration swiches to the simplified Newton-Raphson scheme.
        """
        for key in opts:
            if key=='tolerance':
                self._rtol=opts[key]
            elif key=='iteration_steps_max':
                self._iteration_steps_max=opts[key]
            elif key=='omega_min':
                self._omega_min=opts[key]
            elif key=='atol':
                self._atol=opts[key] 
            elif key=='quadratic_convergence_limit':
                self._quadratic_convergence_limit=opts[key] 
            elif key=='simplified_newton_limit':
                self._simplified_newton_limit=opts[key] 
            else:
                raise KeyError("Invalid option '%s'"%key)

    def getSolution(self, **subs):
        """
        Returns the solution of the PDE.
        :param subs: Substitutions for all symbols used in the coefficients
                     including the initial value for *u*.
        :return: the solution
        :rtype: `Data`
        """
        # get the initial value for the iteration process:
        u_sym=self._unknown.atoms().pop().name
        if not subs.has_key(u_sym):
            raise KeyError("Initial value for '%s' missing."%u_sym)

        ui=subs.pop(u_sym)
        if not isinstance(ui,Data):
            ui=Data(ui, self._lpde.getFunctionSpaceForSolution())

        # modify ui so it meets the constraints:
        q=self._lpde.getCoefficient("q")
        if not q.isEmpty():
           if subs.has_key("r"): self.r=subs.pop("r")
           r=self.r
           if hasattr(r, "atoms"):
              r=Evaluator(r).evaluate(**subs)
           elif not isinstance(r, Data):
              ui=Data(r, self._lpde.getFunctionSpaceForSolution())
           elif r.isEmpty():
              r=0  
           ui = q * r + (1-q) * ui
           
        # separate symbolic expressions from other coefficients
        constants={}
        expressions={}
        for n, e in self._set_coeffs.items():
            if hasattr(e, "atoms"):
                expressions[n]=e
            else:
                constants[n]=e

        # set constant PDE values now
        self._lpde.setValue(**constants)
        self._lpde.getSolverOptions().setAbsoluteTolerance(0.)
        self._lpde.getSolverOptions().setVerbosity(self._debug > self.DEBUG1)
        #============================================================================================================
        # perform Newton iterations until error is small enough or
        # maximum number of iterations reached
        n=0
        omega=1. # relaxation factor
        use_simplified_Newton=False
        defect_norm=None
        delta_norm=None
        converged=False
        
        subs[u_sym]=ui
        while not converged:
            if n > self._iteration_steps_max:
               raise iteration_steps_maxReached("maximum number of iteration steps reach. Giving up.")
            self.trace1(5*"="+" %s-th iteration step."%n + 5*"=") 
            # calculate the correction delta_u
            if n == 0:
                self._unknownpdateLinearPDE(expressions, subs)
                defect_norm=self._getDefectNorm(self._lpde.getRightHandSide())
                LINTOL=0.1
            else:
                if not use_simplified_Newton: self._unknownpdateMatrix(expressions, subs)
                if q_u == None:
                   LINTOL = 0.1 * min(qtol/defect_norm)
                else:
                   LINTOL = 0.1 * max( q_u**2, min(qtol/defect_norm) )
                LINTOL=max(1e-4,min(LINTOL, 0.1))
            self._lpde.getSolverOptions().setTolerance(LINTOL)
            self.trace1("PDE is solved with rel. tolerance = %e"%(LINTOL,))
            delta_u=self._lpde.getSolution()
            
            #check for reduced defect:
            omega=min(2*omega, 1.) # raise omega 
            defect_reduced=False
            while not defect_reduced:
                ui=ui-delta_u * omega               
                subs[u_sym]=ui        
                self._unknownpdateRHS(expressions, subs)
                new_defect_norm=self._getDefectNorm(self._lpde.getRightHandSide())
                q_defect=max(self._getSafeRatio(new_defect_norm, defect_norm)) # if defect_norm==0 and new_defect_norm!=0 
                                                                               # this will be util.DBLE_MAX
                self.trace1("Defect reduction = %e with relaxation factor %e."%(q_defect, omega))
                if q_defect < 1:
                    defect_reduced=True
                else:
                    omega*=0.5
                    if omega < self._omega_min:
                        raise DivergenceDetected("Underrelaxtion failed to reduce defect. Giving up.")
                        
            delta_norm, delta_norm_old = self._getSolutionNorm(delta_u) * omega, delta_norm   
            defect_norm, defect_norm_old = new_defect_norm, defect_norm
            u_norm=self._getSolutionNorm(ui, atol=self._atol)
            # set the tolerance on equation level: 
            qtol=self._getSafeRatio(defect_norm_old * u_norm * self._rtol, delta_norm) 
            # if defect_norm_old==0 and defect_norm_old!=0 this will be util.DBLE_MAX
            #    -> the ordering of the equations is not appropriate.
            # if defect_norm_old==0 and defect_norm_old==0  this is zero so convergence can happen for defect_norm==0 only.
            if not max(qtol)<util.DBLE_MAX:
                     raise InadmissiblePDEOrdering("Review ordering of PDE equations.")
            # check stoping criteria
            if not delta_norm_old == None: 
               q_u=max(self._getSafeRatio(delta_norm , delta_norm_old))  # if delta_norm_old==0 and delta_norm!=0 
                                                                           # this will be util.DBLE_MAX
               if q_u <= self._quadratic_convergence_limit and not omega<1. :
                 quadratic_convergence=True
                 self.trace1("Quadratic convergence detected (rate %e <= %e)"%(q_u, self._quadratic_convergence_limit))

                 converged = all( [ defect_norm[i] <= qtol[i] for i in range(len(qtol)) ])
                  
               else:
                   self.trace1("No quadratic convergence detected (rate %e > %e, omega=%e)"%(q_u, self._quadratic_convergence_limit,omega ))
                   quadratic_convergence=False
	           converged=False
            else:
               q_u=None
               converged=False 
               quadratic_convergence=False
            if self._debug > self.DEBUG0:
                for i in range(len(u_norm)):
                     self.trace1("Component %s: u: %e, du: %e, defect: %e, qtol: %e"%(i, u_norm[i], delta_norm[i], defect_norm[i], qtol[i]))
                if converged: self.trace1("Iteration has converged.")                
            # Can we switch to simplified Newton?
            if quadratic_convergence:
                q_defect=max(self._getSafeRatio(defect_norm, defect_norm_old))
                if q_defect < self._simplified_newton_limit:
                    use_simplified_Newton=True
                    self.trace1("Simplified Newton-Raphson is applied (rate %e < %e)."%(q_defect, self._simplified_newton_limit))
            n+=1
        self.trace1(5*"="+" Newton-Raphson iteration completed after %s steps."%n + 5*"=")
        return ui
    def _getDefectNorm(self, f):
        """
        calculates the norm of the defect ``f``
        
        :param f: defect vector
        :type f: `Data` of rank 0 or 1.
        :return: component-by-component norm of ``f``
        :rtype: `numpy.array` of rank 1
        :raise ValueError: if shape if ``f`` is incorrect.
        
        """
        # this still needs some work!!!
        out=[]
        s=f.getShape()
        if len(s) == 0:
           out.append(util.Lsup(f))
        elif len(s) == 1:
           for i in range(s[0]):
                out.append(util.Lsup(f[i]))
        else:
           raise ValueError("Illegal shape %s."%(s,))
        return numpy.array(out)
        
    def _getSolutionNorm(self, u, atol=0.):
        """
        calculates the norm of the defect ``u``
        
        :param f: defect vector
        :type f: `Data` of rank 0 or 1.
        :return: component-by-component norm of ``u``
        :rtype: `numpy.array` of rank 1
        :raise ValueError: if shape if ``u`` is incorrect.
        
        """
        out=[]
        s=u.getShape()
        if len(s) == 0:
           out.append(max(util.Lsup(u),atol) )
        elif len(s) == 1:
           for i in range(s[0]):
                out.append(max(util.Lsup(u[i]), atol))
        else:
           raise ValueError("Illegal shape %s."%(s,))
        return numpy.array(out)
    def _getSafeRatio(self, a , b):
        """
        return the component-by-component ratio of ''a'' and ''b''
        
        If for a component ``i`` the values ``a[i]`` and ``b[i]`` both are equal to zero their ratio is set to zero.
        If ``b[i]`` equals zero but ``a[i]`` is positive the ratio is set to `util.DBLE_MAX`.  
        
        :param a: numerator
        :param b: denominator
        :type a: `numpy.array` of rank 1 with non-negative entries.
        :type b: `numpy.array` of rank 1 with non-negative entries.
        :return: ratio of ``a`` and ``b`` 
        :rtype: `numpy.array`
        """
        out=0.
        if a.shape !=b.shape:
            raise ValueError("shapes must match.")
        s=a.shape
        if len(s) != 1:
            raise ValueError("rank one is expected.") 
        out=numpy.zeros(s)   
        for i in range(s[0]): 
           if abs(b[i]) > 0:
               out[i]=a[i]/b[i]
           elif abs(a[i]) > 0:
               out[i] = util.DBLE_MAX
           else:
               out[i] = 0
        return out
        
    def getNumSolutions(self):
        """
        Returns the number of the solution components
        :rtype: ``int``
        """
        s=self._unknown.getShape()
        if len(s) > 0:
            return s[0]
        else:
            return 1

    def getShapeOfCoefficient(self,name):
        """
        Returns the shape of the coefficient ``name``.

        :param name: name of the coefficient enquired
        :type name: ``string``
        :return: the shape of the coefficient ``name``
        :rtype: ``tuple`` of ``int``
        :raise IllegalCoefficient: if ``name`` is not a coefficient of the PDE
        """
        numSol=self.getNumSolutions()
        dim = self.dim
        if name=="X" or name=="X_reduced":
            if numSol > 1: 
                return (numSol,dim)         
            else:
                return (dim,)
        elif name=="r" or name == "q" :
            if numSol > 1: 
                return (numSol,)         
            else:
                return ()
        elif name=="Y" or name=="Y_reduced":
            if numSol > 1:
                return (numSol,)         
            else:
                return ()
        elif name=="y" or name=="y_reduced":
            if numSol > 1: 
                return (numSol,)         
            else:
                return ()         
        elif name=="y_contact" or name=="y_contact_reduced":
            if numSol > 1: 
                return (numSol,)         
            else:
                return ()         
        elif name=="y_dirac":
            if numSol > 1: 
                return (numSol,)         
            else:
                return ()         
        else:
            raise IllegalCoefficient("Attempt to request unknown coefficient %s"%name) 

    def createCoefficient(self, name):
        """
        create a new coefficient ``name`` as Symbol

        :param name: name of the coefficient requested
        :type name: ``string``
        :return: the value of the coefficient
        :rtype: `Symbol` or `Data` 
        :raise IllegalCoefficient: if ``name`` is not a coefficient of the PDE
        """   
        if name == q:
            return self._lpde.createCoefficient("q")           
        else:
           s=self.getShapeOfCoefficient(name)
           return Symbol(name, s)

    def getCoefficient(self, name):
        """
        Returns the value of the coefficient ``name`` as Symbol

        :param name: name of the coefficient requested
        :type name: ``string``
        :return: the value of the coefficient
        :rtype: `Symbol`
        :raise IllegalCoefficient: if ``name`` is not a coefficient of the PDE
        """
        if self._set_coeffs.has_key(name):
            return self._set_coeffs[name]
        else:
            raise IllegalCoefficient("Attempt to request undefined coefficient %s"%name)

    def setValue(self,**coefficients):
        """
        Sets new values to one or more coefficients.

        :param coefficients: new values assigned to coefficients
        :keyword X: value for coefficient ``X``
        :type X: `Symbol` or any type that can be cast to a `Data` object
        :keyword Y: value for coefficient ``Y``
        :type Y: `Symbol` or any type that can be cast to a `Data` object
        :keyword y: value for coefficient ``y``
        :type y: `Symbol` or any type that can be cast to a `Data` object
        :keyword y_contact: value for coefficient ``y_contact``
        :type y_contact: `Symbol` or any type that can be cast to a `Data` object
        :keyword y_dirac: value for coefficient ``y_dirac``
        :type y_dirac: `Symbol` or any type that can be cast to a `Data` object
        :keyword q: mask for location of constraint
        :type q: any type that can be cast to a `Data` object       
        :keyword r: value of solution prescribed by constraint
        :type r: `Symbol` or any type that can be cast to a `Data` object       
        :raise IllegalCoefficient: if an unknown coefficient keyword is used
        :raise IllegalCoefficientValue: if a supplied coefficient value has an
                                        invalid shape
        """

        u=self._unknown
        for name,val in coefficients.iteritems():
            shape=util.getShape(val)
            if not shape == self.getShapeOfCoefficient(name):
                raise IllegalCoefficientValue("%s has shape %s but must have shape %d"%(name, self.getShapeOfCoefficient(name), shape))
            rank=len(shape)
            if name == "q":
                self._lpde.setValue(q=val)  
            elif name == "r":
                self.r=val
            elif name=="X" or name=="X_reduced":
                # DX/Du = del_X/del_unknown + del_X/del_grad(u)*del_grad(u)/del_unknown
                #            \   /         \   /
                #              B             A
                
                if rank != u.getRank()+1:
                    raise IllegalCoefficientValue("%s must have rank %d"%(name,u.getRank()+1))
                T0=time()
                if not hasattr(val, 'diff'):
                    A=numpy.zeros(shape+u.grad().getShape())
                    B=numpy.zeros(shape+u.getShape())
                elif u.getRank()==0:
                    X=self._removeFsFromGrad(val)
                    dXdu=X.diff(u)
                    dgdu=u.grad().diff(u)
                    A=numpy.empty(shape+dgdu.getShape(), dtype=object)
                    B=numpy.empty(shape, dtype=object)
                    for i in numpy.ndindex(shape):
                        for j in numpy.ndindex(dgdu.getShape()):
                            y=dXdu[i]
                            x=dgdu[j]
                            # expand() and coeff() are very expensive so
                            # we set the unwanted factors to zero to extract
                            # the one we need
                            for jj in numpy.ndindex(dgdu.getShape()):
                                if j==jj: continue
                                y=y.subs(dgdu[jj], 0)
                            B[i]=y.subs(x,0) # terms in u and constants
                            A[i,j]=y.subs(x,1)-B[i]
                    A=Symbol(A)
                    B=Symbol(B)
                else:  #u.getRank()==1
                    X=self._removeFsFromGrad(val)
                    dXdu=X.diff(u)
                    dgdu=u.grad().diff(u).transpose(2)
                    I,J=shape
                    K,L=u.grad().getShape()
                    A=numpy.empty((I,J,K,L), dtype=object)
                    B=numpy.empty((I,J,K), dtype=object)
                    for i,j,k,l in numpy.ndindex(I,J,K,L):
                        if dgdu[k,k,l]==0:
                            A[i,j,k,l]=0
                            B[i,j,k]=0
                        else:
                            y=dXdu[i,j,k]
                            x=dgdu[k,k,l]
                            for kk,ll in numpy.ndindex(K,L):
                                if k==kk and l==ll: continue
                                y=y.subs(dgdu[kk,kk,ll], 0)
                            B[i,j,k]=y.subs(x,0) # terms in u and constants
                            A[i,j,k,l]=y.subs(x,1)-B[i,j,k]

                    A=Symbol(A)
                    B=Symbol(B)

                if name=='X_reduced':
                    self.trace3("Computing A_reduced, B_reduced took %f seconds."%(time()-T0))
                    self._set_coeffs['A_reduced']=A
                    self._set_coeffs['B_reduced']=B
                    self._set_coeffs['X_reduced']=val
                else:
                    self.trace3("Computing A, B took %f seconds."%(time()-T0))
                    self._set_coeffs['A']=A
                    self._set_coeffs['B']=B
                    self._set_coeffs['X']=val
            elif name=="Y" or name=="Y_reduced":
                # DY/Du = del_Y/del_unknown + del_Y/del_grad(u)*del_grad(u)/del_unknown
                #            \   /         \   /
                #              D             C
                if rank != u.getRank():
                    raise IllegalCoefficientValue("%s must have rank %d"%(name,u.getRank()))
                T0=time()
                if not hasattr(val, 'diff'):
                    C=numpy.zeros(shape+u.grad().getShape())
                    D=numpy.zeros(shape+u.getShape())
                elif u.getRank()==0:
                    Y=self._removeFsFromGrad(val)
                    dYdu=Y.diff(u)
                    dgdu=u.grad().diff(u)
                    C=numpy.empty(dgdu.getShape(), dtype=object)
                    for j in numpy.ndindex(dgdu.getShape()):
                        y=dYdu
                        x=dgdu[j]
                        # expand() and coeff() are very expensive so
                        # we set the unwanted factors to zero to extract
                        # the one we need
                        for jj in numpy.ndindex(dgdu.getShape()):
                            if j==jj: continue
                            y=y.subs(dgdu[jj], 0)
                        D=y.subs(x,0) # terms in u and constants
                        C[j]=y.subs(x,1)-D
                    C=Symbol(C)
                else:  #u.getRank()==1
                    Y=self._removeFsFromGrad(val)
                    dYdu=Y.diff(u)
                    dgdu=u.grad().diff(u).transpose(2)
                    I,=shape
                    J,K=u.grad().getShape()
                    C=numpy.empty((I,J,K), dtype=object)
                    D=numpy.empty((I,J), dtype=object)
                    for i,j,k in numpy.ndindex(I,J,K):
                        if dgdu[j,j,k]==0:
                            C[i,j,k]=0
                            D[i,j]=0
                        else:
                            y=dYdu[i,j]
                            x=dgdu[j,j,k]
                            for jj,kk in numpy.ndindex(J,K):
                                if j==jj and k==kk: continue
                                y=y.subs(dgdu[jj,jj,kk], 0)
                            D[i,j]=y.subs(x,0) # terms in u and constants
                            C[i,j,k]=y.subs(x,1)-D[i,j]
                    C=Symbol(C)
                    D=Symbol(D)

                if name=='Y_reduced':
                    self.trace3("Computing C_reduced, D_reduced took %f seconds."%(time()-T0))
                    self._set_coeffs['C_reduced']=C
                    self._set_coeffs['D_reduced']=D
                    self._set_coeffs['Y_reduced']=val
                else:
                    self.trace3("Computing C, D took %f seconds."%(time()-T0))
                    self._set_coeffs['C']=C
                    self._set_coeffs['D']=D
                    self._set_coeffs['Y']=val
            elif name in ("y", "y_reduced", "y_contact", "y_contact_reduced", \
                    "y_dirac"):
                y=val
                if rank != u.getRank():
                    raise IllegalCoefficientValue("%s must have rank %d"%(name,u.getRank()))
                if not hasattr(y, 'diff'):
                    d=numpy.zeros(u.getShape())
                else:
                    d=y.diff(u)
                self._set_coeffs[name]=y
                self._set_coeffs['d'+name[1:]]=d
            elif name=="q":
                if rank != u.getRank():
                    raise IllegalCoefficientValue("q must have rank %d"%u.getRank())
                self._set_coeffs['q']=val
            else:
                raise IllegalCoefficient("Attempt to set unknown coefficient %s"%name)

    def _newtonStep(self, expressions, subs):
        """
        """
        self._unknownpdateLinearPDE(expressions, subs)
        delta_u=self._lpde.getSolution()
        return delta_u

    def _unknownpdateRHS(self, expressions, subs):
        ev=Evaluator()
        names=[]
        for name in expressions:
            if name in self.__COEFFICIENTS:
                ev.addExpression(expressions[name])
                names.append(name)
        if len(names)==0:
            return
        self.trace3("Starting expression evaluation.")
        ttt0=time()
        ev.subs(**subs)
        res=ev.evaluate()
        if len(names)==1: res=[res]
        self.trace3("RHS expressions evaluated in %f seconds."%(time()-ttt0))
        for i in range(len(names)):
            self.trace3("util.Lsup(%s)=%s"%(names[i],util.Lsup(res[i])))
        self._lpde.setValue(**dict(zip(names,res)))

    def _unknownpdateMatrix(self, expressions, subs):
        ev=Evaluator()
        names=[]
        for name in expressions:
            if not name in self.__COEFFICIENTS:
                ev.addExpression(expressions[name])
                names.append(name)
        if len(names)==0:
            return
        self.trace3("Starting expression evaluation.")
        ttt0=time()
        ev.subs(**subs)
        res=ev.evaluate()
        if len(names)==1: res=[res]
        self.trace3("Matrix expressions evaluated in %f seconds."%(time()-ttt0))
        for i in range(len(names)):
            self.trace3("util.Lsup(%s)=%s"%(names[i],util.Lsup(res[i])))
        self._lpde.setValue(**dict(zip(names,res)))

    def _unknownpdateLinearPDE(self, expressions, subs):
        self._unknownpdateMatrix(expressions, subs)
        self._unknownpdateRHS(expressions, subs)

    def _removeFsFromGrad(self, sym):
        """
        Returns sym with all occurrences grad_n(a,b,c) replaced by grad_n(a,b).
        That is, all functionspace parameters are removed.
        This method is used in setValue() in order to get substitutions work
        properly.
        """
        from esys.escript import symfn
        gg=sym.atoms(symfn.grad_n)
        for g in gg:
            if len(g.args)==3:
                r=symfn.grad_n(*g.args[:2])
                sym=sym.subs(g, r)
        return sym

