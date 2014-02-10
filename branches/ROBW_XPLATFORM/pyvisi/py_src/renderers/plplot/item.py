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

# $Id: item.py,v 1.5 2005/03/14 05:31:08 paultcochrane Exp $

## @file item.py

"""
Brief introduction to what the file contains/does
"""

from common import debugMsg

from esys.pyvisi.item import Item as BaseItem

__revision__ = '$Revision: 1.5 $'

class Item(BaseItem):
    """
    This is the base class for items within a scene
    """

    def __init__(self):
        """
        Initialisation
        """
        debugMsg("Called Item.__init__()")
        BaseItem.__init__(self)
    
# vim: expandtab shiftwidth=4: