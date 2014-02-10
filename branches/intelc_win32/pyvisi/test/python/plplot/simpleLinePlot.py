# $Id: simpleLinePlot.py,v 1.1 2005/05/05 01:57:24 paultcochrane Exp $

"""
Example of plotting lines with pyvisi

This is the original code used to develop the plplot renderer module

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


# set up some data to plot
from Numeric import *

x = arange(10, typecode=Float)
y = x**2

import plplot

plplot.plsdev("xwin")
plplot.plinit()
plplot.plenv(min(x), max(x), min(y), max(y), 0, 1)
plplot.pllab("x", "x**2", "Example 2D plot")
plplot.plline(x, y)
plplot.plend()

# to save as well, have to set everything up again, and replot
# save as png
plplot.plsdev("png")
plplot.plsfnam("simplePlotExample.png")
plplot.plinit()
plplot.plenv(min(x), max(x), min(y), max(y), 0, 1)
plplot.pllab("x", "x**2", "Example 2D plot")
plplot.plline(x, y)
plplot.plend()

# save as postscript
plplot.plsdev("psc")
plplot.plsfnam("simplePlotExample.ps")
plplot.plinit()
plplot.plenv(min(x), max(x), min(y), max(y), 0, 1)
plplot.pllab("x", "x**2", "Example 2D plot")
plplot.plline(x, y)
plplot.plend()