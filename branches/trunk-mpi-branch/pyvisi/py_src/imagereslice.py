#
# $Id$
#
#######################################################
#
#           Copyright 2003-2007 by ACceSS MNRF
#       Copyright 2007 by University of Queensland
#
#                http://esscc.uq.edu.au
#        Primary Business: Queensland, Australia
#  Licensed under the Open Software License version 3.0
#     http://www.opensource.org/licenses/osl-3.0.php
#
#######################################################
#

"""
@var __author__: name of author
@var __copyright__: copyrights
@var __license__: licence agreement
@var __url__: url entry point on documentation
@var __version__: version
@var __date__: date of the version
"""

__author__="John Ngui, john.ngui@uq.edu.au"
__copyright__="""  Copyright (c) 2006 by ACcESS MNRF
                    http://www.access.edu.au
                Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
             http://www.opensource.org/licenses/osl-3.0.php"""
__url__="http://www.iservo.edu.au/esys"
__version__="$Revision$"
__date__="$Date$"


import vtk

class ImageReslice:
	"""
	Class that defines an image reslice used to resize static 
	(no interaction capability) images (i.e. logo).
	"""

	def __init__(self):
		"""
		Initialise the image reslice.
		"""

		self.__vtk_image_reslice = vtk.vtkImageReslice()

	def _setupImageReslice(self, object):
		"""
		Setup the image reslice.

		@type object: vtkImageData
		@param object: Image Data
		"""

		self.__object = object
		self.__setInput()

	def __setInput(self):
		"""
		Set the input for the image reslice.
		"""

		self.__vtk_image_reslice.SetInput(self.__object)		

	def setSize(self, size):
		"""
		Set the size of the image, between 0 and 2. 
		Size 1 (one) displays the image in its original size 
		(which is the default).  

		@type size: Number
		@param size: Size of the static image
		"""

		# By default, with image reslice, the larger the output spacing, the
		# smaller the image. Similarly, the smaller the output spacing, the 
		# larger the image. This behaviour is reversed so that the larger the 
		# size the larger the image. Similarly, the smaller the size, the 
		# smaller the image.
		if(size > 1):
			size = 1 - (size - 1)
			self.__vtk_image_reslice.SetOutputSpacing(size, size, size)
		elif(size < 1):
			size = (1 - size) + 1
			self.__vtk_image_reslice.SetOutputSpacing(size, size, size)

	def _getImageResliceOutput(self):
		"""
		Return the output of the image reslice.

		@rtype: vtkImageData
		@return: Image data
		"""

		return self.__vtk_image_reslice.GetOutput()