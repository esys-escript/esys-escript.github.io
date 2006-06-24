# $Id$
"""
Test writing data object to various file formats 

by Lutz Gross, ACcESS, University of Queensland, Australia, 2005.
"""

__copyright__="""  Copyright (c) 2006 by ACcESS MNRF
                    http://www.access.edu.au
                Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
             http://www.opensource.org/licenses/osl-3.0.php"""
from esys.escript import *
from esys.finley import Rectangle,Brick


ne=1
work_dir="."

def  writeInFormat(fs,format,filetype):
        d=fs.getDim()
        x=length(fs.getX())
        # generate scalar data:
        filename="%s/scalar.%s.%s"%(work_dir,filetype,format)
        print "file ",filename," is generated"
        try:
           eval("x.save%s(\"%s\")"%(format.upper(),filename))
        except StandardError, msg:
           print "%% failed because of ",msg
        # generate vector data:
        print "file ",filename," is generated"
        filename="%s/vector.%s.%s"%(work_dir,filetype,format)
        if d==2:
           m=[1.,2.]
        else:
           m=[1.,2.,3.]
        try:
           eval("(x*m).save%s(\"%s\")"%(format.upper(),filename))
        except StandardError, msg:
           print "%% failed because of ",msg
        # generate tensor data:
        filename="%s/tensor.%s.%s"%(work_dir,filetype,format)
        print "file ",filename," is generated"
        if d==2:
           m=[[11.,12.],[21.,22.]]
        else:
           m=[[11.,12.,13.],[21.,22.,23.],[31.,32.,33.]]
        try:
           eval("(x*m).save%s(\"%s\")"%(format.upper(),filename))
        except StandardError, msg:
           print "%% failed because of ",msg

for format in ["vtk","dx"]:
   for d in [2,3]:
      for order in [1,2]:
        if (d == 2):
            mesh = Rectangle(ne, ne,order,l0=order*ne,l1=order*ne)
        elif (d == 3):
            mesh = Brick(ne,ne,ne,order,l0=order*ne,l1=order*ne,l2=order*ne)
        for fs in ["ContinuousFunction","Function","FunctionOnBoundary","Solution","ReducedSolution","FunctionOnContact"]:
              filetype="%s.o%d.d%d"%(fs,order,d)
              writeInFormat(eval("%s(mesh)"%fs),format,filetype)

