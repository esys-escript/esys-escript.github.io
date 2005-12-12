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

# $Id: axes.py,v 1.12 2005/09/22 04:56:52 paultcochrane Exp $

## @file axes.py

"""
Class and functions associated with a pyvisi Axes object
"""

# generic imports
from pyvisi.renderers.vtk.common import debugMsg

# module specific imports
from pyvisi.renderers.vtk.plot import Plot

__revision__ = '$Revision: 1.12 $'

class Axes(Plot):
    """
    Axes class
    """
    def __init__(self):
        """
        Initialisation of Axes object
        """
        debugMsg("Called Axes.__init__()")
        Plot.__init__(self)

# vim: expandtab shiftwidth=4:
