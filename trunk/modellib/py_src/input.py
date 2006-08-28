# $Id$

__copyright__="""  Copyright (c) 2006 by ACcESS MNRF
                    http://www.access.edu.au
                Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
             http://www.opensource.org/licenses/osl-3.0.php"""

from esys.escript import *
from esys.escript.modelframe import Model,ParameterSet
from math import log

class Sequencer(Model):
    """
    Runs through time until t_end is reached. 

    @ivar t_end: model is terminated when t_end is passed, default 1 (in).
    @type t_end: C{float}
    @ivar dt_max: maximum time step size, default L{Model.UNDEF_DT} (in)
    @type dt_max: C{float}
    @ivar t: current time stamp (in/out). By default it is initialized with zero.
    @type t: C{float}

    """
    def __init__(self,debug=False):
        """
        """
        super(Sequencer,self).__init__(debug=debug)
        self.declareParameter(t=0.,
                              t_end=1.,
                              dt_max=Model.UNDEF_DT)

    def doInitialization(self):
        """ 
        initialize time integration
        """
        self.__t_old = self.t

    def doStepPreprocessing(self, dt):
        self.t = self.__t_old+dt

    def doStepPostprocessing(self, dt):
        self.__t_old = self.t

    def finalize(self):
        """
        returns true when L{t} has reached L{t_end}
        """
        return self.t >= self.t_end

    def getSafeTimeStepSize(self, dt):
        """
        returns L{dt_max}
        """
        return self.dt_max

class GaussianProfile(ParameterSet):
    """
    Generates a Gaussian profile at center x_c, width width and height A 
    over a domain

    @ivar domain: domain
    @ivar x_c: center of the Gaussian profile (default [0.,0.,0.])
    @ivar A: (in) height of the profile. A maybe a vector. (default 1.)
    @ivar width: (in) width of the profile (default 0.1)
    @ivar r: (in) radius of the circle (default = 0)

    In the case that the spatial dimension is two, The third component of 
    x_c is dropped.
    """
    def __init__(self,debug=False):
        ParameterSet.__init__(self,debug=debug)
        self.declareParameter(domain=None, 
                              x_c=numarray.zeros([3]),
                              A=1.,
                              width=0.1,
                              r=0)

    def out(self):
        """
        Generate the Gaussian profile

        Link against this method to get the output of this model.
        """
        x = self.domain.getX()
        dim = self.domain.getDim()
        l = length(x-self.x_c[:dim])
        m = whereNegative(l-self.r)

        return (m+(1.-m)*exp(-log(2.)*(l/self.width)**2))*self.A

class InterpolateOverBox(ParameterSet):
    """
    Returns values at each time. The values are defined through given values 
    at time node. For two dimensional domains back values are ignored.

    @ivar domain: domain
    @ivar value_left_bottom_front: (in) value at left,bottom,front corner
    @ivar value_right_bottom_front: (in) value at right, bottom, front corner
    @ivar value_left_top_front: (in) value at left,top,front corner
    @ivar value_right_top_front: (in) value at right,top,front corner
    @ivar value_left_bottom_back: (in) value at  left,bottom,back corner
    @ivar value_right_bottom_back: (in) value at right,bottom,back corner
    @ivar value_left_top_back: (in) value at left,top,back  corner
    @ivar value_right_top_back: (in) value at right,top,back corner
    """

    def __init__(self, debug=False):
        ParameterSet.__init__(self, debug=debug)
        self.declareParameter(domain=None, 
                              value_left_bottom_front=0.,
                              value_right_bottom_front=0.,
                              value_left_top_front=0.,
                              value_right_top_front=0.,
                              value_left_bottom_back=0.,
                              value_right_bottom_back=0.,
                              value_left_top_back=0.,
                              value_right_top_back=0.)


    def out(self):
        """
        values at domain locations by bilinear interpolation of the given values.

        Link against this method to get the output of this model.
        """
        x = self.domain.getX()
        if self.domain.getDim() == 2:
            x0,x1=x[0],x[1]
            left_bottom_front0,right_top_back0=inf(x0),sup(x0)
            left_bottom_front1,right_top_back1=inf(x1),sup(x1)
            f_right = (x0 - left_bottom_front0)/(right_top_back0 -left_bottom_front0)
            f_left = 1. - f_right
            f_top = (x1 - left_bottom_front1)/(right_top_back1 - left_bottom_front1)
            f_bottom = 1. - f_top
            out = f_left * f_bottom * self.value_left_bottom_front \
                + f_right * f_bottom * self.value_right_bottom_front \
                + f_left * f_top * self.value_left_top_front \
                + f_right * f_top * self.value_right_top_front
        else:
            x0,x1,x2=x[0],x[1],x[2]
            left_bottom_front0,right_top_back0=inf(x0),sup(x0)
            left_bottom_front1,right_top_back1=inf(x1),sup(x1)
            left_bottom_front2,right_top_back2=inf(x2),sup(x2)
            f_right = (x0 - left_bottom_front0)/(right_top_back0 - left_bottom_front0)
            f_left = 1. - f_right
            f_top = (x1 - left_bottom_front1)/(right_top_back1 - left_bottom_front1)
            f_bottom = 1. - f_top
            f_back = (x2 - left_bottom_front1)/(right_top_back2 - left_bottom_front2)
            f_front = 1. - f_back
            out = f_left * f_bottom * f_front * self.value_left_bottom_front\
                + f_right * f_bottom * f_front * self.value_right_bottom_front\
                + f_left * f_top * f_front * self.value_left_top_front\
                + f_right * f_top * f_front * self.value_right_top_front\
                + f_left * f_bottom * f_back * self.value_left_bottom_back\
                + f_right * f_bottom * f_back * self.value_right_bottom_back\
                + f_left * f_top * f_back * self.value_left_top_back\
                + f_right * f_top * f_back * self.value_right_top_back
        return out


class InterpolatedTimeProfile(ParameterSet):
       """

       Returns values at each time. The values are defined through given 
       values at time node.
            
       value[i] defines the value at time nodes[i]. Between nodes linear 
       interpolation is used.

       For time t<nodes[0], value[0] is used and for t>nodes[l], values[l] 
       is used where l=len(nodes)-1.
 
       @ivar t: (in) current time
       @ivar node: (in) list of time nodes
       @ivar values: (in) list of values at time nodes
       """

       def __init__(self,debug=False):
           ParameterSet.__init__(self,debug=debug)
           self.declareParameter(t=0., \
                                 nodes=[0.,1.],\
                                 values=[1.,1.])
       def out(self):
           """
           current value
  
           Link against this method to get the output of this model.
           """
           l = len(self.nodes) - 1
           t = self.t
           if t <= self.nodes[0]:
               return self.values[0]
           else:
               for i in range(1,l):
                  if t < self.nodes[i]:
                      m = (self.values[i-1] - self.values[i])/\
                            (self.nodes[i-1] - self.nodes[i])
                      return m*(t-self.nodes[i-1]) + self.values[i-1]
               return self.values[l]

class LinearCombination(Model):
    """
    Returns a linear combination of the f0*v0+f1*v1+f2*v2+f3*v3+f4*v4
            
    @ivar f0: numerical object or None, default=None (in)
    @ivar v0: numerical object or None, default=None (in)
    @ivar f1: numerical object or None, default=None (in)
    @ivar v1: numerical object or None, default=None (in)
    @ivar f2: numerical object or None, default=None (in)
    @ivar v2: numerical object or None, default=None (in)
    @ivar f3: numerical object or None, default=None (in)
    @ivar v3: numerical object or None, default=None (in)
    @ivar f4: numerical object or None, default=None (in)
    @ivar v4: numerical object or None, default=None (in)
    """
    def __init__(self,debug=False):
        Model.__init__(self,debug=debug)
        self.declareParameter(f0=None, \
                              v0=None, \
                              f1=None, \
                              v1=None, \
                              f2=None, \
                              v2=None, \
                              f3=None, \
                              v3=None, \
                              f4=None, \
                              v4=None)

    def out(self):
        """
        returns f0*v0+f1*v1+f2*v2+f3*v3+f4*v4.
        Link against this method to get the output of this model.
        """
        if not self.f0 == None and not self.v0 == None:
            fv0 = self.f0*self.v0
        else:
            fv0 = None

        if not self.f1 == None and not self.v1 == None:
            fv1 = self.f1*self.v1
        else:
            fv1 = None

        if not self.f2 == None and not self.v2 == None:
            fv2 = f2*v2
        else:
            fv2 = None

        if not self.f3 == None and not self.v3 == None:
            fv3 = self.f3*self.v3
        else:
            fv3 = None

        if not self.f4 == None and not self.v4 == None:
            fv4 = self.f4*self.v4
        else:
            fv4 = None

        if fv0 == None: 
             out = 0.
        else:
             out = fv0
        if not fv1 == None: 
            out += fv1
        if not fv2 == None: 
            out += fv2
        if not fv3 == None: 
            out += fv3
        return out

# vim: expandtab shiftwidth=4:
