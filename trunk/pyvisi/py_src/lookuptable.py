"""
@author: John NGUI
"""

import vtk

class LookupTable:
	"""
	Class that defines a lookup table for mapping scalar values into colors.
	"""

	def __init__(self):
		"""
		Initialise the lookup table.
		"""

		self.__vtk_lookup_table = vtk.vtkLookupTable()
		self.__vtk_inverse_lookup_table = vtk.vtkLookupTable()
		self.__build()

	def __build(self):
		"""
		Generates the lookup table.
		"""

		# NOTE: Build have to be executed prior to using SetTableValue (if any).
		self.__vtk_lookup_table.Build()
		self.__vtk_inverse_lookup_table.Build()

	def _setTableValue(self):
		"""
		Setup the lookup table with colors.
		"""

		# NOTE: The color values are inversed because VTK's default lookup
		# table is inversed by itself. SetTableValue have to be executed after
		# the Build.
		for i in range(256):
			self.__vtk_lookup_table.SetTableValue(
					i, self.__vtk_inverse_lookup_table.GetTableValue(255 - i))

	def _setLookupTableToGreyScale(self):
		"""
		Setup the lookup table with grey scale.	
		"""

		self.__setHueRange(0,0)
		self.__setSaturationRange(0,0)
		self.__setValueRange(1,0)
		self.__setNumberOfTableValues(256)
		self.__setRampToSQRT()

	def __setValueRange(self, lower_range, upper_range):
		"""
		Set value range (brighness) for the lookup table (between 0 and 1).

		@type lower_range: Number
		@param lower_range:Lower value range 
		@type upper_range: Number
		@param upper_range: Upper value range
		"""

		self.__vtk_lookup_table.SetValueRange(lower_range, upper_range)

	def __setHueRange(self, lower_range, upper_range):
		"""
		Set hue (color) range for the lookup table (between 0 and 1).

		@type lower_range: Number
		@param lower_range:Lower hue range 
		@type upper_range: Number
		@param upper_range: Upper hue range
		"""

		self.__vtk_lookup_table.SetHueRange(lower_range, upper_range)

	def __setSaturationRange(self, lower_range, upper_range):
		"""
		Set saturation (vibrancy) range for the lookup table (between 0 and 1).

		@type lower_range: Number
		@param lower_range:Lower saturantion range 
		@type upper_range: Number
		@param upper_range: Upper saturation range
		"""

		self.__vtk_lookup_table.SetSaturationRange(lower_range, upper_range)
	
	def __setRampToSQRT(self):
		"""
		Set the table ramp to SQRT. The default ramp is S-curve.	
		"""

		self.__vtk_lookup_table.SetRampToSQRT()

	def __setNumberOfTableValues(self, table_values):
		"""
		Set the number of values (i.e. colors) in the lookup table.	

		@type table_values: Number
		@param table_values: Number of values in the lookup table.
		"""

		self.__vtk_lookup_table.SetNumberOfTableValues(table_values)

	def _getLookupTable(self):
		"""
		@rtype: vtkLookupTable
		@return: Lookup table
		"""

		return self.__vtk_lookup_table


