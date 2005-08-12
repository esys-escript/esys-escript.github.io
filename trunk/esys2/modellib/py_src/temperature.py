# $Id$

from escript.escript import *
from escript.modelframe import Model,IterationDivergenceError
from escript.linearPDEs import AdvectivePDE,LinearPDE
import numarray


class TemperatureAdvection(Model):
       """

         The conservation of internal heat energy is given by

         \f[
             \rho c_p ( T_{,t}+v_{j}T_{,j} )-(\kappa T_{,i})_{,i}=Q,
         \f]
         \f[
                 n_i\kappa T_{,i}=0
         \f]

          it is assummed that \f[ \rho c_p \f] is constant in time.

          solved by Taylor Galerkin method

       """
       def __init__(self,debug=False):
           Model.__init__(self,debug=debug)
           self.declareParameter(domain=None, \
                                 temperature=1., \
                                 velocity=numarray.zeros([3]),
                                 density=1., \
                                 heat_capacity=1., \
                                 thermal_permabilty=1., \
                                 # reference_temperature=0., \
                                 # radiation_coefficient=0., \
                                 thermal_source=0., \
                                 fixed_temperature=0.,
                                 location_fixed_temperature=Data(),
                                 safety_factor=0.1)

       def doInitialization(self):
           self.__pde=LinearPDE(self.domain)
           self.__pde.setSymmetryOn()
           # self.__pde.setReducedOrderOn()
           # self.__pde.setLumpingOn()
           self.__pde.setValue(D=self.heat_capacity*self.density)

       def getSafeTimeStepSize(self,dt):
           """returns new step size"""
           h=self.domain.getSize()
           return self.safety_factor*inf(h**2/(h*abs(self.heat_capacity*self.density)*length(self.velocity)+self.thermal_permabilty))

       def G(self,T,alpha):
           """tangential operator for taylor galerikin"""
           g=grad(T)
           self.__pde.setValue(X=-self.thermal_permabilty*g, \
                               Y=self.thermal_source-self.__rhocp*inner(self.velocity,g), \
                               r=(self.__fixed_T-self.temperature)*alpha,\
                               q=self.location_fixed_temperature)
           return self.__pde.getSolution()
           

       def doStepPostprocessing(self,dt):
           """perform taylor galerkin step"""
           T=self.temperature
	   self.__rhocp=self.heat_capacity*self.density
           self.__fixed_T=self.fixed_temperature
           self.temperature=dt*self.G(dt/2*self.G(T,1./dt)+T,1./dt)+T
           self.trace("Temperature range is %e %e"%(inf(self.temperature),sup(self.temperature)))
