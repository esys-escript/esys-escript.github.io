# $Id:$

"""
Geometrical Elementries

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
__copyright__="""  Copyright (c) 2006 by ACcESS MNRF
                    http://www.access.edu.au
                Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
             http://www.opensource.org/licenses/osl-3.0.php"""
__url__="http://www.iservo.edu.au/esys/escript"
__version__="$Revision:$"
__date__="$Date:$"

from primitives import Primitive #, PrimitiveStack
from datetime import date
import tempfile
import os

class Design(object):
    """
    template for elementary geometrical object
    """
    def __init__(self,dim=3,scale=1.,element_order=1,keep_tmp_files=False):
       """
       """ 
       self.__items=[]
       self.setScale(scale)
       self.setDim(dim)
       self.setElementOrder(element_order)
       self.setKeepTmpFiles(keep_tmp_files)
    def addPrimitive(self,item):
        self.addPrimitives(item)
    def addPrimitives(self,*items):
       for i in range(len(items)):
          if not isinstance(items[i],Primitive):
             raise TypeError("%s-th argument is not a Primitive object"%i)
       for i in items:
          self.__items.append(i)
    def setKeepTmpFiles(self,flag=None):
        if flag==None: 
           if self.__keep_tmp_files==True:
              self.__keep_tmp_files=False
           else:
              self.__keep_tmp_files=True
        else:
              self.__keep_tmp_files=flag
    def keepTmpFiles(self,scale=1.):
        return self.__keep_tmp_files
    def setScale(self,scale=1.):
        self.__scale=scale
    def getScale(self,scale=1.):
        return self.__scale
    def setDim(self,dim=3):
        self.__dim=dim
    def getDim(self,dim=3):
        return self.__dim
    def setElementOrder(self,order=1):
        self.__order=order
    def getElementOrder(self,order=1):
        return self.__order
    def getPrimitives(self):
        return self.__items
    def getGmshScript(self):
        ps=PrimitiveStack(*tuple(self.getPrimitives()))
        return "// generated by esys.pycad\nscale = %s;\n%s"%(self.getScale(),ps.getGmshCommands())
    def writeGmshScript(self,file):
        file.write(self.getGmshScript())
    def writeGmshMesh(self,filename):
        scriptname=tempfile.mkstemp(suffix=".geo")[1]
        self.writeGmshScript(open(scriptname,"w"))
        exe="gmsh -%s -smooth 2 -optimize -v 0 -order %s -o %s %s"%(self.getDim(),self.getElementOrder(),filename,scriptname)
        os.system(exe)
        if not self.keepTmpFiles(): os.unlink(scriptname)
        return exe
    def writeFinleyMesh(self,filename):
        mshname=tempfile.mkstemp(suffix=".msh")[1]
        exe=self.writeGmshMesh(mshname)
        convertGmshToFinley(open(mshname,"r"),open(filename,"w"),dim=self.getDim())
        if not self.keepTmpFiles(): os.unlink(mshname)
        return exe

def convertGmshToFinley(gmsh_file,finley_file,dim=3):
        line=gmsh_file.readline().split()
        while len(line)>0:
           print line
           line=gmsh_file.readline().split()
