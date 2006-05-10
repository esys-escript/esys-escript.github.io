"""
Initialisation of the pyvisi utilities

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

from esys.pyvisi.common import _pyvisiVersion, _pyvisiRevision
print "This is PyVisi version %s-%s" % (_pyvisiVersion, _pyvisiRevision)

__author__ = 'Paul Cochrane'
__version__ = _pyvisiVersion
__revision__ = _pyvisiRevision

# vim: expandtab shiftwidth=4:
