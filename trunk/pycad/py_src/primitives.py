
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
__url__="https://launchpad.net/escript-finley"

"""
Geometrical Primitives

the concept is inspired by gmsh and very much focused on the fact that
the classes are used to wrk with gmsh.

@var __author__: name of author
@var __copyright__: copyrights
@var __license__: licence agreement
@var __url__: url entry point on documentation
@var __version__: version
@var __date__: date of the version
"""

__author__="Lutz Gross, l.gross@uq.edu.au"

try:
   import numpy
   numpyImported=True
except:
   numpyImported=False

import numpy
from transformations import _TYPE, Translation, Dilation, Transformation, DEG
import math 


def resetGlobalPrimitiveIdCounter():
   """
   Initializes the global primitive ID counter.
   """
   global global_primitive_id_counter
   global_primitive_id_counter=1

def setToleranceForColocation(tol=1.e-11):
   """
   Sets the global tolerance for colocation checks to C{tol}.
   """
   global global_tolerance_for_colocation
   global_tolerance_for_colocation=tol

def getToleranceForColocation():
   """
   Returns the global tolerance for colocation checks.
   """
   return global_tolerance_for_colocation

resetGlobalPrimitiveIdCounter()
setToleranceForColocation()


class PrimitiveBase(object):
    """
    Template for a set of primitives.
    """
    def __init__(self):
       """
       Initializes the PrimitiveBase instance object.
       """
       pass

    def __cmp__(self,other):
       """
       Compares object with other by comparing the absolute value of the ID.
       """
       if isinstance(other, PrimitiveBase):
           return cmp(self.getID(),other.getID())
       else:
           return -1

    def getConstructionPoints(self):
        """
        Returns the points used to construct the primitive.
        """
        out=[]
        for i in self.getPrimitives():
           if isinstance(i,Point): out.append(i)
        return out

    def getPrimitives(self):
        """
        Returns a list of primitives used to construct the primitive with no
        double entries.
        """
        out=[]
        for p in self.collectPrimitiveBases():
            if not p  in out: out.append(p)
        return out

    def copy(self):
       """
       Returns a deep copy of the object.
       """
       return self.substitute({})

    def modifyBy(self,transformation):
       """
       Modifies the coordinates by applying a transformation.
       """
       for p in self.getConstructionPoints(): p.modifyBy(transformation)

    def __add__(self,other):
        """
        Returns a new object shifted by C{other}.
        """
        return self.apply(Translation(numpy.array(other,_TYPE)))

    def __sub__(self,other):
        """
        Returns a new object shifted by C{-other}.
        """
        return self.apply(Translation(-numpy.array(other,_TYPE)))

    def __iadd__(self,other):
        """
        Shifts the point inplace by C{other}.
        """
        self.modifyBy(Translation(numpy.array(other,_TYPE)))
        return self

    def __isub__(self,other):
        """
        Shifts the point inplace by C{-other}.
        """
        self.modifyBy(Translation(-numpy.array(other,_TYPE)))
        return self

    def __imul__(self,other):
        """
        Modifies object by applying L{Transformation} C{other}. If C{other}
        is not a L{Transformation} it is first tried to be converted.
        """
        if isinstance(other,int) or isinstance(other,float):
            trafo=Dilation(other)
        elif isinstance(other,numpy.ndarray):
            trafo=Translation(other)
        elif isinstance(other,Transformation):
            trafo=other
        else:
            raise TypeError, "cannot convert argument to a Transformation class object."
        self.modifyBy(trafo)
        return self

    def __rmul__(self,other):
        """
        Applies L{Transformation} C{other} to object. If C{other} is not a
        L{Transformation} it is first tried to be converted.
        """
        if isinstance(other,int) or isinstance(other,float):
            trafo=Dilation(other)
        elif isinstance(other,numpy.ndarray):
            trafo=Translation(other)
        elif isinstance(other,Transformation):
            trafo=other
        else:
            raise TypeError, "cannot convert argument to Transformation class object."
        return self.apply(trafo)


    def setLocalScale(self,factor=1.):
       """
       Sets the local refinement factor.
       """
       for p in self.getConstructionPoints(): p.setLocalScale(factor)

    def apply(self,transformation):
        """
        Returns a new object by applying the transformation.
        """
        out=self.copy()
        out.modifyBy(transformation)
        return out

class Primitive(object):
    """
    Class that represents a general primitive.
    """
    def __init__(self):
       """
       Initializes the Primitive instance object with a unique ID.
       """
       global global_primitive_id_counter
       self.__ID=global_primitive_id_counter
       global_primitive_id_counter+=1

    def getID(self):
       """
       Returns the primitive ID.
       """
       return self.__ID

    def getDirectedID(self):
        """
        Returns the primitive ID where a negative sign means that reversed
        ordering is used.
        """
        return self.getID()

    def __repr__(self):
        return "%s(%s)"%(self.__class__.__name__,self.getID())

    def getUnderlyingPrimitive(self):
        """
        Returns the underlying primitive.
        """
        return self

    def hasSameOrientation(self,other):
        """
        Returns True if C{other} is the same primitive and has the same
        orientation, False otherwise.
        """
        return self == other and isinstance(other,Primitive)

    def __neg__(self):
        """
        Returns a view onto the curve with reversed ordering.

        @note: This method is overwritten by subclasses.
        """
        raise NotImplementedError("__neg__ is not implemented.")

    def substitute(self,sub_dict):
        """
        Returns a copy of self with substitutes for the primitives used to
        construct it given by the dictionary C{sub_dict}. If a substitute for
        the object is given by C{sub_dict} the value is returned, otherwise a
        new instance with substituted arguments is returned.

        @note: This method is overwritten by subclasses.
        """
        raise NotImplementedError("substitute is not implemented.")

    def collectPrimitiveBases(self):
        """
        Returns a list of primitives used to construct the primitive. It may
        contain primitives twice.

        @note: This method is overwritten by subclasses.
        """
        raise NotImplementedError("collectPrimitiveBases is not implemented.")

    def isColocated(self,primitive):
       """
       Rreturns True if the two primitives are located at the same position.

       @note: This method is overwritten by subclasses.
       """
       raise NotImplementedError("isColocated is not implemented.")


class ReversePrimitive(object):
    """
    A view onto a primitive creating a reverse orientation.
    """
    def __init__(self,primitive):
       """
       Instantiates a view onto C{primitive}.
       """
       if not isinstance(primitive, Primitive):
           raise ValueError("argument needs to be a Primitive class object.")
       self.__primitive=primitive

    def getID(self):
       """
       Returns the primitive ID.
       """
       return self.__primitive.getID()

    def getUnderlyingPrimitive(self):
        """
        Returns the underlying primitive.
        """
        return self.__primitive

    def hasSameOrientation(self,other):
        """
        Returns True if C{other} is the same primitive and has the same
        orientation as self.
        """
        return self == other and isinstance(other,ReversePrimitive)

    def __repr__(self):
       return "-%s(%s)"%(self.__primitive.__class__.__name__,self.getID())

    def getDirectedID(self):
        """
        Returns the primitive ID where a negative signs means that reversed
        ordering is used.
        """
        return -self.__primitive.getID()

    def substitute(self,sub_dict):
        """
        Returns a copy of self with substitutes for the primitives used to
        construct it given by the dictionary C{sub_dict}. If a substitute for
        the object is given by C{sub_dict} the value is returned, otherwise a
        new instance with substituted arguments is returned.
        """
        if not sub_dict.has_key(self):
            sub_dict[self]=-self.getUnderlyingPrimitive().substitute(sub_dict)
        return sub_dict[self]

    def __neg__(self):
          """
          Returns a view onto the curve with reversed ordering.
          """
          return self.__primitive

    def collectPrimitiveBases(self):
        """
        Returns a list of primitives used to construct the primitive. It may
        contain primitives twice.
        """
        return self.__primitive.collectPrimitiveBases()

    def isColocated(self,primitive):
       """
       Returns True if the two primitives are located at the same position.

       @note: This method is overwritten by subclasses.
       """
       return self.__primitive.isColocated(primitive)

class Point(Primitive, PrimitiveBase):
    """
    A three-dimensional point.
    """
    def __init__(self,x=0.,y=0.,z=0.,local_scale=1.):
       """
       Creates a point with coordinates C{x}, C{y}, C{z} with the local
       refinement factor C{local_scale}.
       """
       PrimitiveBase.__init__(self)
       Primitive.__init__(self)
       self.setCoordinates(numpy.array([x,y,z],_TYPE))
       self.setLocalScale(local_scale)

    def setLocalScale(self,factor=1.):
       """
       Sets the local refinement factor.
       """
       if factor<=0.:
          raise ValueError("scaling factor must be positive.")
       self.__local_scale=factor

    def getLocalScale(self):
       """
       Returns the local refinement factor.
       """
       return self.__local_scale

    def getCoordinates(self):
       """
       Returns the coodinates of the point as a C{numpy.ndarray} object.
       """
       return self._x

    def setCoordinates(self,x):
       """
       Sets the coodinates of the point from a C{numpy.ndarray} object C{x}.
       """
       if not isinstance(x, numpy.ndarray):
          self._x=numpy.array(x,_TYPE)
       else:
          self._x=x

    def collectPrimitiveBases(self):
       """
       Returns primitives used to construct the primitive.
       """
       return [self]

    def isColocated(self,primitive):
       """
       Returns True if the L{Point} C{primitive} is colocated (has the same
       coordinates) with self. That is, if
       M{|self-primitive| <= tol * max(|self|,|primitive|)}.
       """
       if isinstance(primitive,Point):
          primitive=primitive.getCoordinates()
          c=self.getCoordinates()
          d=c-primitive
          if numpyImported:
            return numpy.dot(d,d)<=getToleranceForColocation()**2*max(numpy.dot(c,c),numpy.dot(primitive,primitive))
          else:
            return numpy.dot(d,d)<=getToleranceForColocation()**2*max(numpy.dot(c,c),numpy.dot(primitive,primitive))
       else:
          return False

    def substitute(self,sub_dict):
        """
        Returns a copy of self with substitutes for the primitives used to
        construct it given by the dictionary C{sub_dict}. If a substitute for
        the object is given by C{sub_dict} the value is returned, otherwise a
        new instance with substituted arguments is returned.
        """
        if not sub_dict.has_key(self):
           c=self.getCoordinates()
           sub_dict[self]=Point(c[0],c[1],c[2],local_scale=self.getLocalScale())
        return sub_dict[self]

    def modifyBy(self,transformation):
        """
        Modifies the coordinates by applying the given transformation.
        """
        self.setCoordinates(transformation(self.getCoordinates()))

    def __neg__(self):
        """
        Returns a view of the object with reverse orientation. As a point has
        no direction the object itself is returned.
        """
        return self

class Manifold1D(PrimitiveBase):
    """
    General one-dimensional manifold in 1D defined by a start and end point.
    """
    def __init__(self):
        """
        Initializes the one-dimensional manifold.
        """
        PrimitiveBase.__init__(self)
        self.resetElementDistribution()

    def getStartPoint(self):
         """
         Returns the start point.
         """
         raise NotImplementedError()

    def getEndPoint(self):
         """
         Returns the end point.
         """
         raise NotImplementedError()

    def getBoundary(self):
        """
        Returns a list of the zero-dimensional manifolds forming the boundary
        of the curve.
        """
        return [ self.getStartPoint(), self.getEndPoint()]

    def setElementDistribution(self,n,progression=1,createBump=False):
        """
        Defines the number of elements on the line. If set it overwrites the local length setting which would be applied.
        The progression factor C{progression} defines the change of element size between naighboured elements. If C{createBump} is set
        progression is applied towards the center of the line.

        @param n: number of elements on the line
        @type n: C{int}
        @param progression: a positive progression factor
        @type progression: positive C{float}
        @param numberteBump: of elements on the line
        @type createBump: C{bool}
        """
        if n<1:
           raise ValueError,"number of elements must be positive."
        if progression<=0:
           raise ValueError,"progression factor must be positive."
        self.__apply_elements=True
        self.__n=n
        self.__progression_factor=progression
        self.__createBump=createBump

    def resetElementDistribution(self):
        """
        removes the a previously set element distribution from the line.
        """
        self.__apply_elements=False

    def getElementDistribution(self):
        """
        Returns the element distribution.

        @return: the tuple of the number of elements, the progression factor and the bump flag. If no element distribution is set C{None} is returned
        @rtype: C{tuple}
        """
        if self.__apply_elements:
           return (self.__n, self.__progression_factor, self.__createBump)
        else:
           return None

class CurveBase(Manifold1D):
    """
    Base class for curves. A Curve is defined by a set of control points.
    """
    def __init__(self):
        """
        Initializes the curve.
        """
        Manifold1D.__init__(self)

    def __len__(self):
        """
        Returns the number of control points.
        """
        return len(self.getControlPoints())

    def getStartPoint(self):
        """
        Returns the start point.
        """
        return self.getControlPoints()[0]

    def getEndPoint(self):
        """
        Returns the end point.
        """
        return self.getControlPoints()[-1]

    def getControlPoints(self):
        """
        Returns a list of the points.
        """
        raise NotImplementedError()

class Curve(CurveBase, Primitive):
    """
    A curve defined through a list of control points.
    """
    def __init__(self,*points):
       """
       Defines a curve from control points given by C{points}.
       """
       if len(points)<2:
           raise ValueError("Curve needs at least two points")
       i=0
       for p in points:
              i+=1
              if not isinstance(p,Point): raise TypeError("%s-th argument is not a Point object."%i)
       self.__points=points
       CurveBase.__init__(self)
       Primitive.__init__(self)

    def getControlPoints(self):
        """
        Returns a list of the points.
        """
        return self.__points

    def __neg__(self):
        """
        Returns a view onto the curve with reversed ordering.
        """
        return ReverseCurve(self)

    def substitute(self,sub_dict):
        """
        Returns a copy of self with substitutes for the primitives used to
        construct it given by the dictionary C{sub_dict}. If a substitute for
        the object is given by C{sub_dict} the value is returned, otherwise a
        new instance with substituted arguments is returned.
        """
        if not sub_dict.has_key(self):
            new_p=[]
            for p in self.getControlPoints(): new_p.append(p.substitute(sub_dict))
            sub_dict[self]=self.__class__(*tuple(new_p))
        return sub_dict[self]

    def collectPrimitiveBases(self):
       """
       Returns the primitives used to construct the curve.
       """
       out=[self]
       for p in self.getControlPoints(): out+=p.collectPrimitiveBases()
       return out

    def isColocated(self,primitive):
       """
       Returns True if curves are at the same position.
       """
       if hasattr(primitive,"getUnderlyingPrimitive"):
         if isinstance(primitive.getUnderlyingPrimitive(),self.__class__):
           if len(primitive) == len(self):
             cp0=self.getControlPoints()
             cp1=primitive.getControlPoints()
             match=True
             for i in range(len(cp0)):
                if not cp0[i].isColocated(cp1[i]):
                   match=False
                   break
             if not match:
                for i in range(len(cp0)):
                   if not cp0[i].isColocated(cp1[len(cp0)-1-i]):
                      return False
             return True
       return False

class ReverseCurve(CurveBase, ReversePrimitive):
    """
    A curve defined through a list of control points.
    """
    def __init__(self,curve):
       """
       Defines a curve from control points.
       """
       if not isinstance(curve, Curve):
           raise TypeError("ReverseCurve needs to be an instance of Curve")
       CurveBase.__init__(self)
       ReversePrimitive.__init__(self,curve)

    def getControlPoints(self):
         """
         Returns a list of the points.
         """
         out=[p for p in self.getUnderlyingPrimitive().getControlPoints()]
         out.reverse()
         return out

class Spline(Curve):
    """
    A spline curve defined through a list of control points.
    """
    pass

class BezierCurve(Curve):
    """
    A Bezier curve.
    """
    pass

class BSpline(Curve):
    """
    A BSpline curve. Control points may be repeated.
    """
    pass

class Line(Curve):
    """
    A line is defined by two points.
    """
    def __init__(self,*points):
        """
        Defines a line with start and end point.
        """
        if len(points)!=2:
           raise TypeError("Line needs two points")
        Curve.__init__(self,*points)

class ArcBase(Manifold1D):
    """
    Base class for arcs.
    """
    def __init__(self):
          """
          Initializes the arc.
          """
          Manifold1D.__init__(self)

    def collectPrimitiveBases(self):
       """
       Returns the primitives used to construct the Arc.
       """
       out=[self]
       out+=self.getStartPoint().collectPrimitiveBases()
       out+=self.getEndPoint().collectPrimitiveBases()
       out+=self.getCenterPoint().collectPrimitiveBases()
       return out

    def getCenterPoint(self):
         """
         Returns the center.
         """
         raise NotImplementedError()

class Arc(ArcBase, Primitive):
    """
    Defines an arc which is strictly smaller than S{pi}.
    """
    def __init__(self,center,start,end):
       """
       Creates an arc defined by the start point, end point and center.
       """
       if not isinstance(center,Point): raise TypeError("center needs to be a Point object.")
       if not isinstance(end,Point): raise TypeError("end needs to be a Point object.")
       if not isinstance(start,Point): raise TypeError("start needs to be a Point object.")
       if center.isColocated(end): raise TypeError("center and start point are colocated.")
       if center.isColocated(start): raise TypeError("center end end point are colocated.")
       if start.isColocated(end): raise TypeError("start and end are colocated.")
       # TODO: check length of circle.
       ArcBase.__init__(self)
       Primitive.__init__(self)
       self.__center=center
       self.__start=start
       self.__end=end

    def __neg__(self):
       """
       Returns a view onto the curve with reversed ordering.
       """
       return ReverseArc(self)

    def getStartPoint(self):
       """
       Returns the start point.
       """
       return self.__start

    def getEndPoint(self):
       """
       Returns the end point.
       """
       return self.__end

    def getCenterPoint(self):
       """
       Returns the center point.
       """
       return self.__center

    def substitute(self,sub_dict):
        """
        Returns a copy of self with substitutes for the primitives used to
        construct it given by the dictionary C{sub_dict}. If a substitute for
        the object is given by C{sub_dict} the value is returned, otherwise a
        new instance with substituted arguments is returned.
        """
        if not sub_dict.has_key(self):
            sub_dict[self]=Arc(self.getCenterPoint().substitute(sub_dict),self.getStartPoint().substitute(sub_dict),self.getEndPoint().substitute(sub_dict))
        return sub_dict[self]

    def isColocated(self,primitive):
       """
       Returns True if curves are at the same position.
       """
       if hasattr(primitive,"getUnderlyingPrimitive"):
          if isinstance(primitive.getUnderlyingPrimitive(),Arc):
            return (self.getCenterPoint().isColocated(primitive.getCenterPoint())) and ( \
                   (self.getEndPoint().isColocated(primitive.getEndPoint()) and self.getStartPoint().isColocated(primitive.getStartPoint()) ) \
                or (self.getEndPoint().isColocated(primitive.getStartPoint()) and self.getStartPoint().isColocated(primitive.getEndPoint()) ) )
       return False

class ReverseArc(ArcBase, ReversePrimitive):
    """
    Defines an arc which is strictly smaller than S{pi}.
    """
    def __init__(self,arc):
       """
       Creates an arc defined by the start point, end point and center.
       """
       if not isinstance(arc, Arc):
           raise TypeError("ReverseCurve needs to be an instance of Arc")
       ArcBase.__init__(self)
       ReversePrimitive.__init__(self,arc)

    def getStartPoint(self):
       """
       Returns the start point.
       """
       return self.getUnderlyingPrimitive().getEndPoint()

    def getEndPoint(self):
       """
       Returns the end point.
       """
       return self.getUnderlyingPrimitive().getStartPoint()

    def getCenterPoint(self):
       """
       Returns the center point.
       """
       return self.getUnderlyingPrimitive().getCenterPoint()

class EllipseBase(Manifold1D):
    """
    Base class for ellipses.
    """
    def __init__(self):
       """
       Initializes the ellipse.
       """
       Manifold1D.__init__(self)

    def collectPrimitiveBases(self):
       """
       Returns the primitives used to construct the ellipse.
       """
       out=[self]
       out+=self.getStartPoint().collectPrimitiveBases()
       out+=self.getEndPoint().collectPrimitiveBases()
       out+=self.getCenterPoint().collectPrimitiveBases()
       out+=self.getPointOnMainAxis().collectPrimitiveBases()
       return out

class Ellipse(EllipseBase, Primitive):
    """
    Defines an ellipse which is strictly smaller than S{pi}.
    """
    def __init__(self,center,point_on_main_axis,start,end):
       """
       Creates an ellipse defined by the start point, end point, the center
       and a point on the main axis.
       """
       if not isinstance(center,Point): raise TypeError("center needs to be a Point object.")
       if not isinstance(end,Point): raise TypeError("end needs to be a Point object.")
       if not isinstance(start,Point): raise TypeError("start needs to be a Point object.")
       if not isinstance(point_on_main_axis,Point): raise TypeError("point on main axis needs to be a Point object.")
       if center.isColocated(end): raise TypeError("center and start point are colocated.")
       if center.isColocated(start): raise TypeError("center end end point are colocated.")
       if center.isColocated(point_on_main_axis): raise TypeError("center and point on main axis are colocated.")
       if start.isColocated(end): raise TypeError("start and end point are colocated.")
       # TODO: check length of circle.
       EllipseBase.__init__(self)
       Primitive.__init__(self)
       self.__center=center
       self.__start=start
       self.__end=end
       self.__point_on_main_axis=point_on_main_axis

    def __neg__(self):
       """
       Returns a view onto the curve with reversed ordering.
       """
       return ReverseEllipse(self)

    def getStartPoint(self):
       """
       Returns the start point.
       """
       return self.__start

    def getEndPoint(self):
       """
       Returns the end point.
       """
       return self.__end

    def getCenterPoint(self):
       """
       Returns the center.
       """
       return self.__center

    def getPointOnMainAxis(self):
       """
       Returns a point on the main axis.
       """
       return self.__point_on_main_axis

    def substitute(self,sub_dict):
        """
        Returns a copy of self with substitutes for the primitives used to
        construct it given by the dictionary C{sub_dict}. If a substitute for
        the object is given by C{sub_dict} the value is returned, otherwise a
        new instance with substituted arguments is returned.
        """
        if not sub_dict.has_key(self):
            sub_dict[self]=Ellipse(self.getCenterPoint().substitute(sub_dict),
                                   self.getPointOnMainAxis().substitute(sub_dict),
                                   self.getStartPoint().substitute(sub_dict),
                                   self.getEndPoint().substitute(sub_dict))
        return sub_dict[self]


    def isColocated(self,primitive):
       """
       Returns True if curves are at the same position.
       """
       if hasattr(primitive,"getUnderlyingPrimitive"):
          if isinstance(primitive.getUnderlyingPrimitive(),Ellipse):
            self_c=self.getCenterPoint().getCoordinates()
            p=self.getPointOnMainAxis().getCoordinates()-self_c
            q=primitive.getPointOnMainAxis().getCoordinates()-self_c
            # are p and q orthogonal or collinear?
            len_p=math.sqrt(p[0]**2+p[1]**2+p[2]**2)
            len_q=math.sqrt(q[0]**2+q[1]**2+q[2]**2)
            p_q= abs(p[0]*q[0]+p[1]*q[1]+p[2]*q[2])
            return ((p_q <= getToleranceForColocation() * len_q * p_q) or \
                    (abs(p_q - len_q * p_q) <= getToleranceForColocation())) and \
                   self.getCenterPoint().isColocated(primitive.getCenterPoint()) and \
                   ( \
                    (self.getEndPoint().isColocated(primitive.getEndPoint()) and \
                     self.getStartPoint().isColocated(primitive.getStartPoint()) ) \
                    or \
                    (self.getEndPoint().isColocated(primitive.getStartPoint()) and \
                     self.getStartPoint().isColocated(primitive.getEndPoint())) \
                   )
       return False

class ReverseEllipse(EllipseBase, ReversePrimitive):
    """
    Defines an ellipse which is strictly smaller than S{pi}.
    """
    def __init__(self,arc):
       """
       Creates an instance of a reverse view to an ellipse.
       """
       if not isinstance(arc, Ellipse):
           raise TypeError("ReverseCurve needs to be an instance of Ellipse")
       EllipseBase.__init__(self)
       ReversePrimitive.__init__(self,arc)

    def getStartPoint(self):
       """
       Returns the start point.
       """
       return self.getUnderlyingPrimitive().getEndPoint()

    def getEndPoint(self):
       """
       Returns the end point.
       """
       return self.getUnderlyingPrimitive().getStartPoint()

    def getCenterPoint(self):
       """
       Returns the center point.
       """
       return self.getUnderlyingPrimitive().getCenterPoint()

    def getPointOnMainAxis(self):
       """
       Returns a point on the main axis.
       """
       return self.getUnderlyingPrimitive().getPointOnMainAxis()


class CurveLoop(Primitive, PrimitiveBase):
    """
    An oriented loop of one-dimensional manifolds (= curves and arcs).

    The loop must be closed and the L{Manifold1D}s should be oriented
    consistently.
    """
    def __init__(self,*curves):
       """
       Creates a polygon from a list of line curves. The curves must form a
       closed loop.
       """
       if len(curves)<2:
            raise ValueError("at least two curves have to be given.")
       for i in range(len(curves)):
           if not isinstance(curves[i],Manifold1D):
              raise TypeError("%s-th argument is not a Manifold1D object."%i)
       # for the curves a loop:
       used=[ False for i in curves]
       self.__curves=list(curves)
       Primitive.__init__(self)
       PrimitiveBase.__init__(self)

    def getCurves(self):
       """
       Returns the curves defining the CurveLoop.
       """
       return self.__curves

    def __neg__(self):
       """
       Returns a view onto the curve with reversed ordering.
       """
       return ReverseCurveLoop(self)

    def __len__(self):
       """
       Returns the number of curves in the CurveLoop.
       """
       return len(self.getCurves())

    def collectPrimitiveBases(self):
       """
       Returns primitives used to construct the CurveLoop.
       """
       out=[self]
       for c in self.getCurves(): out+=c.collectPrimitiveBases()
       return out

    def substitute(self,sub_dict):
        """
        Returns a copy of self with substitutes for the primitives used to
        construct it given by the dictionary C{sub_dict}. If a substitute for
        the object is given by C{sub_dict} the value is returned, otherwise a
        new instance with substituted arguments is returned.
        """
        if not sub_dict.has_key(self):
            new_c=[]
            for c in self.getCurves(): new_c.append(c.substitute(sub_dict))
            sub_dict[self]=CurveLoop(*tuple(new_c))
        return sub_dict[self]

    def isColocated(self,primitive):
       """
       Returns True if each curve is colocated with a curve in C{primitive}.
       """
       if hasattr(primitive,"getUnderlyingPrimitive"):
          if isinstance(primitive.getUnderlyingPrimitive(),CurveLoop):
             if len(primitive) == len(self):
                cp0=self.getCurves()
                cp1=primitive.getCurves()
                for c0 in cp0:
                    colocated = False
                    for c1 in cp1:
                         colocated = colocated or c0.isColocated(c1)
                    if not colocated: return False
                return True
       return False

class ReverseCurveLoop(ReversePrimitive, PrimitiveBase):
    """
    An oriented loop of one-dimensional manifolds (= curves and arcs).

    The loop must be closed and the one-dimensional manifolds should be
    oriented consistently.
    """
    def __init__(self,curve_loop):
       """
       Creates a polygon from a list of line curves. The curves must form a
       closed loop.
       """
       if not isinstance(curve_loop, CurveLoop):
           raise TypeError("arguments need to be an instance of CurveLoop.")
       ReversePrimitive.__init__(self, curve_loop)
       PrimitiveBase.__init__(self)

    def getCurves(self):
       """
       Returns the curves defining the CurveLoop.
       """
       return [ -c for c in  self.getUnderlyingPrimitive().getCurves() ]

    def __len__(self):
        return len(self.getUnderlyingPrimitive())

#=
class Manifold2D(PrimitiveBase):
    """
    General two-dimensional manifold.
 
    @var LEFT: left element orientation when meshing with transifinite meshing
    @var RIGHT: right element orientation when meshing with transifinite meshing
    @var ALTERNATE: alternate element orientation when meshing with transifinite meshing
    """
    LEFT="Left"
    RIGHT="Right"
    ALTERNATE="Alternate"
    def __init__(self):
       """
       Creates a two-dimensional manifold.
       """
       PrimitiveBase.__init__(self)
       self.setRecombination(None)
       self.resetTransfiniteMeshing()

    def getBoundary(self):
        """
        Returns a list of the one-dimensional manifolds forming the boundary
        of the surface (including holes).
        """
        raise NotImplementedError()

    def hasHole(self):
        """
        Returns True if a hole is present.
        """
        raise NotImplementedError()

    def getPoints(self):
        """
        returns a list of points used to define the boundary
        
        @return: list of points used to define the boundary
        @rtype: C{list} of  L{Point}s
        """
        out=[]
        boundary=self.getBoundary()
        for l in boundary:
            for p in l.getBoundary():
               if not p in out: out.append(p)
        return out

    def setRecombination(self, max_deviation=45*DEG):
        """
        Recombines triangular meshes on the surface into mixed triangular/quadrangular meshes.
        C{max_deviation} specifies the maximum derivation of the largest angle in the quadrangle 
        from the right angle. Use C{max_deviation}==C{None} to switch off recombination.

        @param max_deviation: maximum derivation of the largest angle in the quadrangle from the right angle. 
        @type max_deviation: C{float} or C{None}.
        """
        if not max_deviation==None:
            if max_deviation<=0:
               raise ValueError, "max_deviation must be positive."
            if max_deviation/DEG>=90:
               raise ValueError, "max_deviation must be smaller than 90 DEG"
        self.__recombination_angle=max_deviation

    def getRecombination(self):
        """
        returns max deviation from right angle in the recombination algorithm 

        @return: max deviation from right angle in the recombination algorithm. If recombination is switched off, C{None} is returned.
        @rtype: C{float} or C{None}
        """
        return self.__recombination_angle

    def setTransfiniteMeshing(self,orientation="Left"):
        """
        applies 2D transfinite meshing to the surface. 

        @param orientation: sets the orientation of the triangles. It is only used if recombination is not used.
        @type orientation: L{Manifold2D.LEFT}, L{Manifold2D.RIGHT}, L{Manifold2D.ALTERNATE}
        @note: Transfinite meshing can not be applied if holes are present.
        """
        if not orientation in [ Manifold2D.LEFT, Manifold2D.RIGHT, Manifold2D.ALTERNATE]:
              raise ValueError,"invalid orientation %s."%orientation
        if self.hasHole():
             raise ValueError,"transfinite meshing cannot be appled to surfaces with a hole."
        b=self.getBoundary()
        if len(b)>4 or len(b)<3:
             raise ValueError,"transfinite meshing permits 3 or 4 boundary lines only."
        for l in b: 
            if l.getElementDistribution() == None: raise  ValueError,"transfinite meshing requires element distribution on all boundary lines."
        start=b[0]
        opposite=None
        top=None
        bottom=None
        for l in b[1:]:
             if l.getEndPoint() == start.getStartPoint():
                 bottom=l
             elif l.getStartPoint() == start.getEndPoint(): 
                 top=l
             else:
                 opposite=l
        if top==None or bottom == None: 
             raise ValueError,"transfinite meshing cannot be applied to boundary is not closed. Most likely the orientation of some boundray segments is wrong."
        if opposite == None:  # three sides only
             if not top.getElementDistribution() == bottom.getElementDistribution(): start, top, bottom= bottom, start, top
        if not top.getElementDistribution() == bottom.getElementDistribution():
             raise ValueError,"transfinite meshing requires oposite faces to be have the same element distribution."
        if not opposite == None:
            if not start.getElementDistribution() == opposite.getElementDistribution():
                raise ValueError,"transfinite meshing requires oposite faces to be have the same element distribution."
        if opposite == None:
            if bottom.getEndPoint ==  top.getStartPoint():
                raise ValueError,"cannot identify corner proints for transfinite meshing."
            else:
                points=[ bottom.getStartPoint(), bottom.getEndPoint(), top.getStartPoint() ]
        else:
            points=[ bottom.getStartPoint(), bottom.getEndPoint(), top.getStartPoint(), top.getEndPoint() ]
        self.__points=points
        self.__orientation=orientation
        self.__transfinitemeshing=True

    def resetTransfiniteMeshing(self):
        """
        removes the transfinite meshing from the surface
        """
        self.__transfinitemeshing=False

    def getTransfiniteMeshing(self):
        """
        returns the transfinite meshing setings. If transfinite meshing is not set, C{None} is returned.
        
        @return: a tuple of the tuple of points used to define the transfinite meshing and the orientation. If no points are set the points tuple is returned as C{None}. If no ransfinite meshing is not set, C{None} is returned.
        @rtype: C{tuple} of a C{tuple} of L{Point}s (or C{None}) and the orientation which is one of the values  L{Manifold2D.LEFT}, L{Manifold2D.RIGHT}, L{Manifold2D.ALTERNATE}
        """
        if self.__transfinitemeshing:
            return (self.__points, self.__orientation)
        else:
            return None
           
class RuledSurface(Primitive, Manifold2D):
    """
    A ruled surface, i.e. a surface that can be interpolated using transfinite
    interpolation.
    """
    def __init__(self,loop):
       """
       Creates a ruled surface with boundary C{loop}.

       @param loop: L{CurveLoop} defining the boundary of the surface.
       """
       if not isinstance(loop.getUnderlyingPrimitive(),CurveLoop):
           raise TypeError("argument loop needs to be a CurveLoop object.")
       if len(loop)<2:
           raise ValueError("the loop must contain at least two Curves.")
       if len(loop)>4:
           raise ValueError("the loop must contain at most four Curves.")
       Primitive.__init__(self)
       Manifold2D.__init__(self)
       self.__loop=loop

    def hasHole(self):
        """
        Returns True if a hole is present.
        """
        return False

    def __neg__(self):
        """
        Returns a view onto the suface with reversed ordering.
        """
        return ReverseRuledSurface(self)

    def getBoundaryLoop(self):
        """
        Returns the loop defining the outer boundary.
        """
        return self.__loop

    def getBoundary(self):
        """
        Returns a list of the one-dimensional manifolds forming the boundary
        of the Surface (including holes).
        """
        return self.getBoundaryLoop().getCurves()

    def substitute(self,sub_dict):
        """
        Returns a copy of self with substitutes for the primitives used to
        construct it given by the dictionary C{sub_dict}. If a substitute for
        the object is given by C{sub_dict} the value is returned, otherwise a
        new instance with substituted arguments is returned.
        """
        if not sub_dict.has_key(self):
            sub_dict[self]=RuledSurface(self.getBoundaryLoop().substitute(sub_dict))
        return sub_dict[self]

    def isColocated(self,primitive):
       """
       Returns True if each curve is colocated with a curve in C{primitive}.
       """
       if hasattr(primitive,"getUnderlyingPrimitive"):
          if isinstance(primitive.getUnderlyingPrimitive(),RuledSurface):
             return self.getBoundaryLoop().isColocated(primitive.getBoundaryLoop())
       return False

    def collectPrimitiveBases(self):
        """
        Returns primitives used to construct the Surface.
        """
        return [self] + self.getBoundaryLoop().collectPrimitiveBases()

def createRuledSurface(*curves):
      """
      An easier way to create a L{RuledSurface} from given curves.
      """
      return RuledSurface(CurveLoop(*curves))


class ReverseRuledSurface(ReversePrimitive, Manifold2D):
    """
    Creates a view onto a L{RuledSurface} but with reverse orientation.
    """
    def __init__(self,surface):
       """
       Creates a polygon from a list of line curves. The curves must form a
       closed loop.
       """
       if not isinstance(surface, RuledSurface):
           raise TypeError("arguments need to be an instance of CurveLoop.")
       ReversePrimitive.__init__(self, surface)
       Manifold2D.__init__(self)

    def getBoundaryLoop(self):
       """
       Returns the CurveLoop defining the ReverseRuledSurface.
       """
       return -self.getUnderlyingPrimitive().getBoundaryLoop()

    def getBoundary(self):
       """
       Returns a list of the one-dimensional manifolds forming the boundary
       of the Surface (including holes).
       """
       return self.getBoundaryLoop().getCurves()

    def hasHole(self):
        """
        Returns True if a hole is present.
        """
        return False

#==============================
class PlaneSurface(Primitive, Manifold2D):
    """
    A plane surface with holes.
    """
    def __init__(self,loop,holes=[]):
       """
       Creates a plane surface with holes.

       @param loop: L{CurveLoop} defining the boundary of the surface
       @param holes: list of L{CurveLoop}s defining holes in the surface
       @note: A CurveLoop defining a hole should not have any lines in common
              with the exterior CurveLoop.
       @note: A CurveLoop defining a hole should not have any lines in common
              with another CurveLoop defining a hole in the same surface.
       """
       if not isinstance(loop.getUnderlyingPrimitive(),CurveLoop):
           raise TypeError("argument loop needs to be a CurveLoop object.")
       for i in range(len(holes)):
            if not isinstance(holes[i].getUnderlyingPrimitive(), CurveLoop):
                 raise TypeError("%i-th hole needs to be a CurveLoop object.")
       #TODO: check if lines and holes are in a plane
       #TODO: are holes really holes?
       Primitive.__init__(self)
       Manifold2D.__init__(self)
       self.__loop=loop
       self.__holes=holes

    def hasHole(self):
        """
        Returns True if a hole is present.
        """
        return len(self.getHoles())>0

    def getHoles(self):
       """
       Returns the holes.
       """
       return self.__holes

    def getBoundaryLoop(self):
        """
        Returns the loop defining the boundary.
        """
        return self.__loop

    def substitute(self,sub_dict):
        """
        Returns a copy of self with substitutes for the primitives used to
        construct it given by the dictionary C{sub_dict}. If a substitute for
        the object is given by C{sub_dict} the value is returned, otherwise a
        new instance with substituted arguments is returned.
        """
        if not sub_dict.has_key(self):
            sub_dict[self]=PlaneSurface(self.getBoundaryLoop().substitute(sub_dict),[ h.substitute(sub_dict) for h in self.getHoles()])
        return sub_dict[self]

    def isColocated(self,primitive):
       """
       Returns True if each curve is colocated with a curve in C{primitive}.
       """
       if hasattr(primitive,"getUnderlyingPrimitive"):
          if isinstance(primitive.getUnderlyingPrimitive(),PlaneSurface):
             if self.getBoundaryLoop().isColocated(primitive.getBoundaryLoop()):
                hs0=self.getHoles()
                hs1=primitive.getHoles()
                if len(hs0) == len(hs1):
                    for h0 in hs0:
                       colocated = False
                       for h1 in hs1:
                         colocated = colocated or h0.isColocated(h1)
                       if not colocated: return False
                    return True
       return False

    def collectPrimitiveBases(self):
        """
        Returns primitives used to construct the Surface.
        """
        out=[self] + self.getBoundaryLoop().collectPrimitiveBases()
        for i in self.getHoles(): out+=i.collectPrimitiveBases()
        return out

    def __neg__(self):
        """
        Returns a view onto the curve with reversed ordering.
        """
        return ReversePlaneSurface(self)

    def getBoundary(self):
        """
        Returns a list of the one-dimensional manifolds forming the boundary
        of the Surface (including holes).
        """
        out = []+ self.getBoundaryLoop().getCurves()
        for h in self.getHoles(): out+=h.getCurves()
        return out

class ReversePlaneSurface(ReversePrimitive, Manifold2D):
    """
    Creates a view onto a L{PlaneSurface} but with reverse orientation.
    """
    def __init__(self,surface):
       """
       Creates a polygon from a L{PlaneSurface}.
       """
       if not isinstance(surface, PlaneSurface):
           raise TypeError("arguments need to be an instance of PlaneSurface.")
       ReversePrimitive.__init__(self, surface)
       Manifold2D.__init__(self)

    def getBoundaryLoop(self):
       """
       Returns the CurveLoop defining the ReversePlaneSurface.
       """
       return -self.getUnderlyingPrimitive().getBoundaryLoop()

    def getHoles(self):
        """
        Returns the holes.
        """
        return [ -h for h in self.getUnderlyingPrimitive().getHoles() ]

    def getBoundary(self):
        """
        Returns a list of the one-dimensional manifolds forming the boundary
        of the Surface (including holes).
        """
        out = [] + self.getBoundaryLoop().getCurves()
        for h in self.getHoles(): out+=h.getCurves()
        return out

    def hasHole(self):
        """
        Returns True if a hole is present.
        """
        return len(self.getHoles())>0

#=========================================================================
class SurfaceLoop(Primitive, PrimitiveBase):
    """
    A loop of 2D primitives which defines the shell of a volume.

    The loop must represent a closed shell, and the primitives should be
    oriented consistently.
    """
    def __init__(self,*surfaces):
       """
       Creates a surface loop.
       """
       if len(surfaces)<2:
            raise ValueError("at least two surfaces have to be given.")
       for i in range(len(surfaces)):
           if not isinstance(surfaces[i].getUnderlyingPrimitive(),Manifold2D):
              raise TypeError("%s-th argument is not a Manifold2D object."%i)
       self.__surfaces=list(surfaces)
       Primitive.__init__(self)
       PrimitiveBase.__init__(self)

    def __len__(self):
       """
       Returns the number of curves in the SurfaceLoop.
       """
       return len(self.__surfaces)

    def __neg__(self):
       """
       Returns a view onto the curve with reversed ordering.
       """
       return ReverseSurfaceLoop(self)

    def getSurfaces(self):
       """
       Returns the surfaces defining the SurfaceLoop.
       """
       return self.__surfaces

    def collectPrimitiveBases(self):
       """
       Returns primitives used to construct the SurfaceLoop.
       """
       out=[self]
       for c in self.getSurfaces(): out+=c.collectPrimitiveBases()
       return out

    def substitute(self,sub_dict):
        """
        Returns a copy of self with substitutes for the primitives used to
        construct it given by the dictionary C{sub_dict}. If a substitute for
        the object is given by C{sub_dict} the value is returned, otherwise a
        new instance with substituted arguments is returned.
        """
        if not sub_dict.has_key(self):
            new_s=[]
            for s in self.getSurfaces(): new_s.append(s.substitute(sub_dict))
            sub_dict[self]=SurfaceLoop(*tuple(new_s))
        return sub_dict[self]

    def isColocated(self,primitive):
       """
       Returns True if each surface is colocated with a curve in C{primitive}
       and vice versa.
       """
       if hasattr(primitive,"getUnderlyingPrimitive"):
         if isinstance(primitive.getUnderlyingPrimitive(),SurfaceLoop):
            if len(primitive) == len(self):
                sp0=self.getSurfaces()
                sp1=primitive.getSurfaces()
                for s0 in sp0:
                    colocated = False
                    for s1 in sp1:
                         colocated = colocated or s0.isColocated(s1)
                    if not colocated: return False
                return True
       return False

class ReverseSurfaceLoop(ReversePrimitive, PrimitiveBase):
    """
    A view of a SurfaceLoop with reverse orientation.

    The loop must represent a closed shell and the primitives should be
    oriented consistently.
    """
    def __init__(self,surface_loop):
       """
       Creates a polygon from a list of line surfaces. The curves must form
       a closed loop.
       """
       if not isinstance(surface_loop, SurfaceLoop):
           raise TypeError("arguments need to be an instance of SurfaceLoop.")
       ReversePrimitive.__init__(self, surface_loop)
       PrimitiveBase.__init__(self)

    def getSurfaces(self):
       """
       Returns the surfaces defining the SurfaceLoop.
       """
       return [ -s for s in  self.getUnderlyingPrimitive().getSurfaces() ]

    def __len__(self):
        return len(self.getUnderlyingPrimitive())

#==============================
class Manifold3D(PrimitiveBase):
    """
    General three-dimensional manifold.
    """
    def __init__(self):
       """
       Creates a three-dimensional manifold.
       """
       PrimitiveBase.__init__(self)

    def getBoundary(self):
        """
        Returns a list of the one-dimensional manifolds forming the boundary
        of the volume (including holes).
        """
        raise NotImplementedError()

class Volume(Manifold3D, Primitive):
    """
    A volume with holes.
    """
    def __init__(self,loop,holes=[]):
       """
       Creates a volume with holes.

       @param loop: L{SurfaceLoop} defining the boundary of the surface
       @param holes: list of L{SurfaceLoop} defining holes in the surface
       @note: A SurfaceLoop defining a hole should not have any surfaces in
              common with the exterior SurfaceLoop.
       @note: A SurfaceLoop defining a hole should not have any surfaces in
              common with another SurfaceLoop defining a hole in the same
              volume.
       """
       if not isinstance(loop.getUnderlyingPrimitive(), SurfaceLoop):
           raise TypeError("argument loop needs to be a SurfaceLoop object.")
       for i in range(len(holes)):
            if not isinstance(holes[i].getUnderlyingPrimitive(), SurfaceLoop):
                 raise TypeError("%i th hole needs to be a SurfaceLoop object.")
       Primitive.__init__(self)
       Manifold3D.__init__(self)
       self.__loop=loop
       self.__holes=holes

    def getHoles(self):
       """
       Returns the holes in the volume.
       """
       return self.__holes

    def getSurfaceLoop(self):
       """
       Returns the loop forming the surface.
       """
       return self.__loop

    def substitute(self,sub_dict):
        """
        Returns a copy of self with substitutes for the primitives used to
        construct it given by the dictionary C{sub_dict}. If a substitute for
        the object is given by C{sub_dict} the value is returned, otherwise a
        new instance with substituted arguments is returned.
        """
        if not sub_dict.has_key(self):
            sub_dict[self]=Volume(self.getSurfaceLoop().substitute(sub_dict),[ h.substitute(sub_dict) for h in self.getHoles()])
        return sub_dict[self]

    def isColocated(self,primitive):
       """
       Returns True if each curve is colocated with a curve in C{primitive}.
       """
       if hasattr(primitive,"getUnderlyingPrimitive"):
          if isinstance(primitive.getUnderlyingPrimitive(),Volume):
             if self.getSurfaceLoop().isColocated(primitive.getSurfaceLoop()):
                hs0=self.getHoles()
                hs1=primitive.getHoles()
                if len(hs0) == len(hs1):
                    for h0 in hs0:
                       colocated = False
                       for h1 in hs1:
                         colocated = colocated or h0.isColocated(h1)
                       if not colocated: return False
                    return True
       return False

    def collectPrimitiveBases(self):
        """
        Returns primitives used to construct the surface.
        """
        out=[self] + self.getSurfaceLoop().collectPrimitiveBases()
        for i in self.getHoles(): out+=i.collectPrimitiveBases()
        return out

    def getBoundary(self):
        """
        Returns a list of the one-dimensional manifolds forming the boundary
        of the Surface (including holes).
        """
        out = []+ self.getSurfaceLoop().getSurfaces()
        for h in self.getHoles(): out+=h.getSurfaces()
        return out

class PropertySet(Primitive, PrimitiveBase):
    """
    Defines a group of L{Primitive}s which can be accessed through a name.
    """
    def __init__(self,name,*items):
       Primitive.__init__(self)
       self.__dim=None
       self.clearItems()
       self.addItem(*items)
       self.setName(name)

    def getDim(self):
       """
       Returns the dimensionality of the items.
       """
       if self.__dim == None:
           items=self.getItems()
           if len(items)>0:
                if isinstance(items[0] ,Manifold1D):
                     self.__dim=1
                elif isinstance(items[0] ,Manifold2D):
                     self.__dim=2
                elif isinstance(items[0] ,Manifold3D):
                    self.__dim=3
                else:
                    self.__dim=0
       return self.__dim

    def __repr__(self):
       """
       Returns a string representation.
       """
       return "%s(%s)"%(self.getName(),self.getID())

    def getManifoldClass(self):
        """
        Returns the manifold class expected from items.
        """
        d=self.getDim()
        if d == None:
           raise ValueError("undefined spatial diemnsion.")
        else:
           if d==0:
              return Point
           elif d==1:
              return Manifold1D
           elif d==2:
              return Manifold2D
           else:
              return Manifold3D

    def getName(self):
        """
        Returns the name of the set.
        """
        return self.__name

    def setName(self,name):
        """
        Sets the name.
        """
        self.__name=str(name)

    def addItems(self,*items):
        """
        Adds items. An item my be any L{Primitive} but no L{PropertySet}.
        """
        self.addItem(*items)

    def addItem(self,*items):
        """
        Adds items. An item my be any L{Primitive} but no L{PropertySet}.
        """
        for i in items:
            if not i in self.__items:
               if len(self.__items)>0:
                  m=self.getManifoldClass()
                  if not isinstance(i, m):
                     raise TypeError("argument %s is not a %s class object."%(i, m.__name__))
               self.__items.append(i)

    def getNumItems(self):
        """
        Returns the number of items in the property set.
        """
        return len(self.__items)

    def getItems(self):
        """
        Returns the list of items.
        """
        return self.__items

    def clearItems(self):
        """
        Clears the list of items.
        """
        self.__items=[]

    def collectPrimitiveBases(self):
        """
        Returns primitives used to construct the PropertySet.
        """
        out=[self]
        for i in self.getItems(): out+=i.collectPrimitiveBases()
        return out

    def getTag(self):
        """
        Returns the tag used for this property set.
        """
        return self.getID()

