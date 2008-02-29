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

class Transform:
	"""
	Class that defines the orientation of planes.
	
	@attention: There is a difference between performing rotation first 
	followed by translation, and performing translation first followed 
	by rotation.

	@attention: VTK's coordinate system and translation is NOT 100% precise. 
	Consequently, performing maximum rotation and translation can potentially
	yield incorrect results. For instance, rotating a XY plane along the x-axis 
	90 degrees may NOT produce any results (as it is possible that the XY 
	plane has just fallen outside the visible range). Therefore, rotating the 
	XY plane 89.9 degrees instead, should be a better option in order to 
	produce the correct results.
	"""

	def __init__(self):
		"""
		Initialise the transform object.
		"""

		# NOTE: VTK's coordinates are not 100% precise. The origin is not 
		# exaclty (0,0,0) and the normal is not exactly (0, 0, 1). There is a 
		# slight variance. As a result, a slight alteration has to be done 
		# in order for the plane to be displayed correctly. Otherwise, the 
		# plane may just fall outside the bounding box and nothing 
		# is displayed.  
		self.__OFFSET_VARIANCE = 0.0000000001
		self.__vtk_transform = vtk.vtkTransform()

	def translate(self, x_offset, y_offset, z_offset):
		"""
		Translate the rendered object along the x, y and z-axes.

		@type x_offset: Number
		@param x_offset: Amount to translate along the x-axis
		@type y_offset: Number
		@param y_offset: Amount to translate along the y-axis
		@type z_offset: Number
		@param z_offset: Amount to translate along the z-axis 
		"""

		self.__vtk_transform.Translate(-x_offset, -y_offset, -z_offset)
	
	def rotateX(self, angle):
		"""
		Rotate the plane along the x-axis.

		@type angle: Number
		@param angle: Angle to rotate the plane
		"""

		self.__vtk_transform.RotateX(-angle)

	def rotateY(self, angle):
		"""
		Rotate the plane along the y-axis.

		@type angle: Number
		@param angle: Angle to rotate the plane
		"""

		self.__vtk_transform.RotateY(angle)

	def rotateZ(self, angle):
		"""
		Rotate the plane along the z-axis.

		@type angle: Number
		@param angle: Angle to rotate the plane
		"""

		self.__vtk_transform.RotateZ(angle)

	def setPlaneToXY(self, offset = 0):
		"""
		Set the plane orthogonal to the z-axis.

		@type offset: Number
		@param offset: Amount to translate along the z-axis
		"""
	
		self.translate(0, 0, offset + self.__OFFSET_VARIANCE)

	def setPlaneToYZ(self, offset = 0):
		"""
		Set the plane orthogonal to the x-axis.

		@type offset: Number
		@param offset: Amount to translate along the x-axis
		"""
		
		# NOTE: rotateY must come first before translate. Otherwise, 
		# the output may be incorrect.
		self.rotateY(90) 
		self.translate(offset, 0, 0)

	def setPlaneToXZ(self, offset = 0):
		"""
		Set the plane orthogonal to the y-axis.

		@type offset: Number
		@param offset: Amount to translate along the y-axis
		"""

		# rotateX must come first before translate. Otherwise, it won't work.
		self.rotateX(90)
		self.translate(0, offset, 0)
	
	def _getTransform(self):
		"""
		Return the transform instance.

		@rtype: vtkTransform
		@return: Transform instance that is used to specify the orientation
			of the plane
		"""

		return self.__vtk_transform


###############################################################################


class TransformFilter:
	"""
	Class that defines a transform poly data filter.
	"""

	def __init__(self):
		"""
		Initialise the transoform poly data filter.
		"""

		self.__vtk_transform_filter = vtk.vtkTransformPolyDataFilter()

	def _setupTransformFilter(self, plane_source, transform):
		"""
		Setup the transform filter.

		@type plane_source: vtkPolyData
		@param plane_source: Polygonal data
		@type transform: L{Transform <transform.Transform>} object
		@param transform: Specifies the orientation of the plane source
		"""

		self.__plane_source = plane_source
		self.__transform = transform

		self.__setInput()
		self.__setTransform()

	def __setInput(self):
		"""
		Set the input for the transform poly data filter.
		"""

		self.__vtk_transform_filter.SetInput(self.__plane_source)

	def __setTransform(self):
		"""
		Set the transformation of the plane source.
		"""

		self.__vtk_transform_filter.SetTransform(self.__transform)

	def _getTransformFilterOutput(self):
		"""
		Return the output of the transform poly data filter.
		"""

		return self.__vtk_transform_filter.GetOutput()



