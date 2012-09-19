# -*- coding: utf-8 -*-

########################################################
#
# Copyright (c) 2003-2012 by University of Queensland
# Earth Systems Science Computational Center (ESSCC)
# http://www.uq.edu.au/esscc
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
########################################################

__copyright__="""Copyright (c) 2003-2012 by University of Queensland
Earth Systems Science Computational Center (ESSCC)
http://www.uq.edu.au/esscc
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"

"""
some mesh handling

:var __author__: name of author
:var __licence__: licence agreement
:var __url__: url entry point on documentation
:var __version__: version
:var __date__: date of the version
"""

__author__="Lutz Gross, l.gross@uq.edu.au"

from esys.pycad.gmsh import Design as GMSHDesign
from .finleycpp import ReadGmsh, ReadMesh, LoadMesh

def MakeDomain(design,integrationOrder=-1, reducedIntegrationOrder=-1, optimizeLabeling=True, useMacroElements=False):
    """
    Creates a Finley `Domain` from a `esys.pycad.design.Design` object.
    Currently only gmsh is supported.

    :param design: the geometry
    :type design: `esys.pycad.design.Design`
    :param integrationOrder: integration order. If -1 the default is used.
    :type integrationOrder: ``int``
    :param reducedIntegrationOrder: reduced integration order. If -1 the
                                    default is used.
    :type reducedIntegrationOrder: ``int``
    :param optimizeLabeling: if set the labeling of the mesh nodes is optimized
    :type optimizeLabeling: ``bool``
    :param useMacroElements: uses macro elements.
    :type useMacroElements: ``bool``
    :return: the Finley domain defined by the design
    :rtype: `Domain`
    """
    if isinstance(design, GMSHDesign):
        if useMacroElements: design.setElementOrder(2)
        ff=design.getFileFormat()
        design.setFileFormat(design.GMSH)
        mshname=design.getMeshHandler()
        dom = ReadGmsh(mshname,
                       design.getDim(),
                       integrationOrder,
                       reducedIntegrationOrder,
                       optimizeLabeling,
                       useMacroElements)
        design.setFileFormat(ff)
    else:
        raise TypeError("Finley does not support %s designs."%design.__class__.__name__)
    # fill in the tag map
    design.getTagMap().passToDomain(dom)
    return dom

def GetMeshFromFile(filename, **kwargs):
    """
    Reads a mesh from a file, determines the reader to use based on the file
    extension. All cases require a filename and gmsh files require a number
    of dimensions (it doesn't hurt to pass this in all the time). Other
    keyword args come from the underlying reader functions.
    """
    spl=filename.split('.')
    ext=spl[len(spl)-1]
    # extract possible params
    integrationOrder=-1
    if kwargs.has_key("integrationOrder"):
        integrationOrder=kwargs["integrationOrder"]
    reducedIntegrationOrder=-1
    if kwargs.has_key("reducedIntegrationOrder"):
        integrationOrder=kwargs["reducedIntegrationOrder"]
    optimize=True  
    if kwargs.has_key("optimize"):
        integrationOrder=kwargs["optimize"]
    useMacroElements=False
    if kwargs.has_key("useMacroElements"):
        integrationOrder=kwargs["useMacroElements"]
    if ext=="fly":
        return ReadMesh(filename, integrationOrder, reducedIntegrationOrder, optimize)
    elif ext=="msh":
        if not kwargs.has_key("numDim"):
	    raise ValueError("The numDim argument is required in order to read .msh files.")
        return ReadGmsh(filename, kwargs['numDim'], integrationOrder, reducedIntegrationOrder, optimize, useMacroElements)
    else:
#        return LoadMesh(filename)
        raise ValueError("Unsupported extension .%s"%ext)
