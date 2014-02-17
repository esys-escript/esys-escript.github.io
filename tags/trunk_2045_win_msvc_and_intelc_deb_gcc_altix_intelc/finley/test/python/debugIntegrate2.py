
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

from esys.escript import *
from esys.escript.linearPDEs import *
from esysi import finley

def makeParallelFaultSystem2D(xne=1,yne=1,xl=1.,yfaults=[0.,1.],integrationOrder=0,p1=0,p2=0):
 """
 generates a 2D rectangular domain and a system of parallel faults at yfaults 
   
 input data :
 xne - the number of elements over the horizontal edge of the rectangular mesh
 xl  - length of the horizontal edge of the domain
 yfault[y0,...yi,...y1] where y0 and y1 are the extremity of the block and yi the fault position in the (Oy) direction
   output data :
        a mesh with horizontal discontinuities at yi positions
 """

 #yne=xne*1./(xl+1.e-15)
 
 mshs=[]
 for i in range(len(yfaults)-1):
     yl=yfaults[i+1]-yfaults[i]
     msh=finley.Rectangle(xne,yne,1,xl,yl,p1,p2,useElementsOnFace=True)
     msh1=msh
     #print "mesh done"
     msh1.setX(msh.getX()+[0.,yfaults[i]])
     #print "Xnew"
     mshs.append(msh1)
     #print "apres append"
     #results=finley.joinFaces(mshs)
     mesh_joint=finley.JoinFaces(mshs)
     #print "apres faces jointes"
 return mesh_joint

def main():

    xne=10
    yne=20
    xl=10
    yl=10
    yfaults=[0.,5.,10.]
    numberfaults=1

    mesh=makeParallelFaultSystem2D(xne,yne,xl,yfaults,0,0,0)
    
    v=Vector(10.,ContinuousFunction(mesh))
    
    on_elem_v=interpolate(v,Function(mesh))
   
    value_integratedEL_vec=integrate(on_elem_v)

    print "vector--------"
    print "value interpolation",value_integratedEL_vec
    print "--------"
 
main()