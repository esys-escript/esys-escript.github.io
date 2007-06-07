"""
@author: John NGUI
"""

class LocalPosition:
	"""
	Class that defines the local positioning coordiante system (2D).
	"""

	def __init__(self, x_coor, y_coor):
		"""
		Initialise the local position.

		@type x_coor: Number
		@param x_coor: x coordinate
		@type y_coor: Number
		@param y_coor: y coordinate
		"""

		self.__x_coor = x_coor
		self.__y_coor = y_coor
		self.__position = [x_coor, y_coor]

	def _getXCoor(self):
		"""
		Return the X coordinate.

		@rtype: Number
		@return: X coordinate
		"""

		return self.__x_coor

	def _getYCoor(self):
		"""
		Return the Y coordinate.

		@rtype: Number
		@return: Y coordinate
		"""

		return self.__y_coor

	def _getLocalPosition(self):
		"""
		Return the local position.

		@rtype: Two column tuple containing numbers
		@return: Tuple with the x and y coordinates
		"""

		return self.__position


###############################################################################


class GlobalPosition:
	"""
	Class that defines the global positioning coordinate system (3D)
	"""
	
	def __init__(self, x_coor, y_coor, z_coor):
		"""
		Initialise the global position.

		@type x_coor: Number
		@param x_coor: x coordinate
		@type y_coor: Number
		@param y_coor: y coordinate
		@type z_coor: Number
		@param z_coor: z coordinate
		"""

		self.__position = [x_coor, y_coor, z_coor]

	def _getGlobalPosition(self):
		"""
		Return the global position.

		@rtype: Three column tuple containing numbers
		@return: Tuple with the x, y and z coordinates
		"""

		return self.__position
