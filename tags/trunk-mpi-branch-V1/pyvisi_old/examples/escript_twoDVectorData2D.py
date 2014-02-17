#!/usr/bin/env python


# $Id: escript_twoDVectorData2D.py,v 1.3 2006/01/05 00:13:50 paultcochrane Exp $
"""
@var __author__: name of author
@var __license__: licence agreement
@var __copyright__: copyrights
@var __url__: url entry point on documentation
@var __version__: version
@var __date__: date of the version
"""

__copyright__="""  Copyright (c) 2006 by ACcESS MNRF
                    http://www.access.edu.au
                Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
             http://www.opensource.org/licenses/osl-3.0.php"""
__author__="Paul Cochrane"
__url__="http://www.iservo.edu.au/esys"
__version__="$Revision$"
__date__="$Date$"

from esys.escript import *
from esys import bruce

import numarray

from esys.pyvisi import *
from esys.pyvisi.renderers.vtk import *

tensorDomain = bruce.Rectangle(9,9,10,10)
tensorFunctionSpace=escript.ContinuousFunction(tensorDomain)

vectorData2D = numarray.array([1.0,2.0])

# plotting 2D vectors in a 2D array
twoDVectorData2D = Data(vectorData2D, tensorFunctionSpace, True)
scene = Scene()
plot = ArrowPlot(scene)
plot.setData(twoDVectorData2D)
if online: scene.render(pause=True)

scene.save(fname="escript_twoDVectorData2D_arrowPlot.png", format="png")

# vim: expandtab shiftwidth=4: