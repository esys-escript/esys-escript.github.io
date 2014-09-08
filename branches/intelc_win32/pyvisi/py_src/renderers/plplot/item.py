"""
Brief introduction to what the file contains/does

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


from common import debugMsg

from esys.pyvisi.item import Item as BaseItem

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