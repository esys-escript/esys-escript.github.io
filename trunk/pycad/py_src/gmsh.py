# -*- coding: utf-8 -*-

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

"""
mesh generation using gmsh

:var __author__: name of author
:var __copyright__: copyrights
:var __license__: licence agreement
:var __url__: url entry point on documentation
:var __version__: version
:var __date__: date of the version
"""

__author__="Lutz Gross, l.gross@uq.edu.au"

import design
import tempfile
import os
from primitives import Point, Spline, BezierCurve, BSpline, Line, Arc, CurveLoop, RuledSurface, PlaneSurface, SurfaceLoop, Volume, PropertySet, Ellipse
from esys.escript import getMPIWorldMax, getMPIRankWorld
from transformations import DEG

class Design(design.Design):
    """
    Design for gmsh.
    """
    DELAUNAY="iso"
    NETGEN="netgen"
    TETGEN="tetgen"

    def __init__(self,dim=3,element_size=1.,order=1,keep_files=False):
       """
       Initializes the gmsh design.

       :param dim: spatial dimension
       :param element_size: global element size
       :param order: element order
       :param keep_files: flag to keep work files
       """
       design.Design.__init__(self,dim=dim,element_size=element_size,order=order,keep_files=keep_files)
       self.setScriptFileName()
       self.setMeshFileName()
       self.setOptions()
       self.setFileFormat(self.GMSH)

    def setScriptFileName(self,name=None):
       """
       Sets the filename for the gmsh input script. If no name is given a name
       with extension I{geo} is generated.
       """
       if name == None:
           tmp_f_id=tempfile.mkstemp(suffix=".geo")
           self.__scriptname=tmp_f_id[1]
           os.close(tmp_f_id[0])
       else:
           self.__scriptname=name
           self.setKeepFilesOn()

    def getScriptFileName(self):
       """
       Returns the name of the gmsh script file.
       """
       return self.__scriptname

    def getMeshFileName(self):
       """
       Returns the name of the gmsh mesh file.
       """
       return self.__mshname

    def setOptions(self,algorithm=None,optimize_quality=True,smoothing=1, curvature_based_element_size=False):
        """
        Sets options for the mesh generator.
        """
        if curvature_based_element_size:
              print "information: gmsh does not support curvature based element size anymore. Option ignored."
        if algorithm==None: algorithm=self.DELAUNAY
        self.__algo=algorithm
        self.__optimize_quality=optimize_quality
        self.__smoothing=smoothing

    def __del__(self):
        """
        Cleans up.
        """
        if not self.keepFiles() :
            os.unlink(self.getScriptFileName())
            os.unlink(self.getMeshFileName())

    def getCommandString(self):
        """
        Returns the gmsh command line.
        """
        if self.__optimize_quality:
              opt="-optimize "
        else:
              opt=""

        exe="gmsh -format %s -%s -algo %s -smooth %s %s-v 3 -order %s -o %s %%s" % (
                self.getFileFormat(), 
                self.getDim(), self.__algo, self.__smoothing, opt,
                self.getElementOrder(), self.getMeshFileName())
        return exe
    def getScriptHandler(self):
        """
        Returns a handler to the script file to generate the geometry.
        In the current implementation a script file name is returned.
        """
        if getMPIRankWorld() == 0:
            open(self.getScriptFileName(),"w").write(self.getScriptString())
        return self.getScriptFileName()

    def getMeshHandler(self):
        """
        Returns a handle to a mesh meshing the design. In the current
        implementation a mesh file name in gmsh format is returned.
        """
        cmd = self.getCommandString()%self.getScriptHandler()
        if getMPIRankWorld() == 0:
            ret = os.system(cmd) / 256
        else:
            ret=0
        ret=getMPIWorldMax(ret)
        if ret > 0: raise RuntimeError, "Could not build mesh: %s"%cmd
        return self.getMeshFileName()

        
    def getScriptString(self):
        """
        Returns the gmsh script to generate the mesh.
        """
        h=self.getElementSize()
        out='// generated by esys.pycad\nGeneral.Terminal = 1;\n'
        for prim in self.getAllPrimitives():
           p=prim.getUnderlyingPrimitive()
           if isinstance(p, Point):
               c=p.getCoordinates()
               out+="Point(%s) = {%s , %s, %s , %s };\n"%(p.getID(),c[0],c[1],c[2], p.getLocalScale()*h)

           elif isinstance(p, Spline):
               out+="Spline(%s) = {%s};\n"%(p.getID(),self.__mkArgs(p.getControlPoints()))+self.__mkTransfiniteLine(p)

           elif isinstance(p, BezierCurve):
               out+="Bezier(%s) = {%s};\n"%(p.getID(),self.__mkArgs(p.getControlPoints()))+self.__mkTransfiniteLine(p)

           elif isinstance(p, BSpline):
               out+="BSpline(%s) = {%s};\n"%(p.getID(),self.__mkArgs(p.getControlPoints()))+self.__mkTransfiniteLine(p)

           elif isinstance(p, Line):
               out+="Line(%s) = {%s, %s};\n"%(p.getID(),p.getStartPoint().getDirectedID(),p.getEndPoint().getDirectedID())+self.__mkTransfiniteLine(p)

           elif isinstance(p, Arc):
              out+="Circle(%s) = {%s, %s, %s};\n"%(p.getID(),p.getStartPoint().getDirectedID(),p.getCenterPoint().getDirectedID(),p.getEndPoint().getDirectedID())+self.__mkTransfiniteLine(p)

           elif isinstance(p, Ellipse):
              out+="Ellipse(%s) = {%s, %s, %s, %s};\n"%(p.getID(),p.getStartPoint().getDirectedID(),p.getCenterPoint().getDirectedID(),p.getPointOnMainAxis().getDirectedID(), p.getEndPoint().getDirectedID())+self.__mkTransfiniteLine(p)

           elif isinstance(p, CurveLoop):
               out+="Line Loop(%s) = {%s};\n"%(p.getID(),self.__mkArgs(p.getCurves()))

           elif isinstance(p, RuledSurface):
               out+="Ruled Surface(%s) = {%s};\n"%(p.getID(),p.getBoundaryLoop().getDirectedID())+self.__mkTransfiniteSurface(p)

           elif isinstance(p, PlaneSurface):
               line=self.__mkArgs(p.getHoles())
               if len(line)>0:
                 out+="Plane Surface(%s) = {%s, %s};\n"%(p.getID(),p.getBoundaryLoop().getDirectedID(), line)+self.__mkTransfiniteSurface(p)
               else:
                 out+="Plane Surface(%s) = {%s};\n"%(p.getID(),p.getBoundaryLoop().getDirectedID())+self.__mkTransfiniteSurface(p)

           elif isinstance(p, SurfaceLoop):
               out+="Surface Loop(%s) = {%s};\n"%(p.getID(),self.__mkArgs(p.getSurfaces()))

           elif isinstance(p, Volume):
               line=self.__mkArgs(p.getHoles())
               if len(line)>0:
                 out+="Volume(%s) = {%s, %s};\n"%(p.getID(),p.getSurfaceLoop().getDirectedID(), line)+self.__mkTransfiniteVolume(p)
               else:
                 out+="Volume(%s) = {%s};\n"%(p.getID(),p.getSurfaceLoop().getDirectedID())+self.__mkTransfiniteVolume(p)

           elif isinstance(p, PropertySet):
               if p.getNumItems()>0:
                  dim=p.getDim()
                  line="Physical "
                  if dim==0:
                      line+="Point"
                  elif dim==1:
                      line+="Line"
                  elif dim==2:
                      line+="Surface"
                  else:
                      line+="Volume"
                  out+=line+"(" + str(p.getID()) + ") = {"+self.__mkArgs(p.getItems(),useAbs=True)+"};\n"

           else:
               raise TypeError("unable to pass %s object to gmsh."%str(type(p)))
        return out


    def __mkArgs(self,args, useAbs=False):
        line=""
        for i in args:
            id = i.getDirectedID()
            if useAbs: id=abs(id)
            if len(line)>0:
                line+=", %s"%id
            else:
                line="%s"%id
        return line

    def __mkTransfiniteLine(self,p):
          s=p.getElementDistribution()
          if not s == None:
              if s[2]:
                  out="Transfinite Line{%d} = %d Using Bump %s;\n"%(p.getID(),s[0],s[1])
              else:
                  out="Transfinite Line{%d} = %d Using Progression %s;\n"%(p.getID(),s[0],s[1])
          else:
               out=""
          return out
    def __mkTransfiniteSurface(self,p):
         out=""
         o=p.getRecombination()
         s=p.getTransfiniteMeshing()
         if not s == None:
             out2=""
             if not s[0] == None:
               for q in s[0]:
                  if len(out2)==0:
                      out2="%s"%q.getID()
                  else:
                      out2="%s,%s"%(out2,q.getID())
             if s[1] == None:
                out+="Transfinite Surface{%s} = {%s};\n"%(p.getID(),out2)
             else:
                out+="Transfinite Surface{%s} = {%s} %s;\n"%(p.getID(),out2,s[1])
         if not o == None:
           out+="Recombine Surface {%s} = %s;\n"%(p.getID(),o/DEG)
         return out
    def __mkTransfiniteVolume(self,p):
         out=""
         s=p.getTransfiniteMeshing()
         if not s == None:
             if len(s)>0:
		    out2=""
         	    for q in s[0]:
			if len(out2)==0:
			    out2="%s"%q.getID()
			else:
			     out2="%s,%s"%(out2,q.getID())
		    out+="Transfinite Volume{%s} = {%s};\n"%(p.getID(),out2)
	     else:
		    out+="Transfinite Volume{%s};\n"%(p.getID(),)
         return out
     
