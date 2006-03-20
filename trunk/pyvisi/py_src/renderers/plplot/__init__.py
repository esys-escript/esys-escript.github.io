# Copyright (C) 2004-2005 Paul Cochrane
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

# $Id: __init__.py,v 1.4 2005/11/30 07:11:47 paultcochrane Exp $

## @file __init__.py

"""
Initialisation of the plplot renderer module
"""
    
from common import _rendererName, _rendererVersion, _rendererRevision
print "This is the \"%s\" renderer module version %s-%s"%(_rendererName, _rendererVersion, _rendererRevision)

__author__ = 'Paul Cochrane'
__version__ = _rendererVersion
__revision__ = _rendererRevision

from item import Item
from scene import Scene
from renderer import Renderer
from axes import Axes
from camera import Camera
from image import Image, JpegImage, PbmImage, PdfImage, PngImage, PnmImage, PsImage, TiffImage
from plane import Plane

# plotting stuff
from plot import Plot
from arrow_plot import ArrowPlot
from contour_plot import ContourPlot
from line_plot import LinePlot
from surface_plot import SurfacePlot

from text import Text

# vim: expandtab shiftwidth=4:
