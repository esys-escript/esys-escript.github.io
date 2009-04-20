
########################################################
#
# Copyright (c) 2003-2008 by University of Queensland
# Earth Systems Science Computational Center (ESSCC)
# http://www.uq.edu.au/esscc
#
# Primary Business: Queensland, Australia
# Licensed under the Open Software License version 3.0
# http://www.opensource.org/licenses/osl-3.0.php
#
########################################################

__copyright__="""Copyright (c) 2003-2008 by University of Queensland
Earth Systems Science Computational Center (ESSCC)
http://www.uq.edu.au/esscc
Primary Business: Queensland, Australia"""
__license__="""Licensed under the Open Software License version 3.0
http://www.opensource.org/licenses/osl-3.0.php"""
__url__="https://launchpad.net/escript-finley"

from esys.pyvisi import DataCollector, Scene, Map
from esys.pyvisi.constant import *
import unittest, os, sys
from stat import ST_SIZE
from esys.escript import getMPISizeWorld

try:
	PYVISI_WORKDIR=os.environ['PYVISI_WORKDIR']
except KeyError:
	PYVISI_WORKDIR='.'
try:
	PYVISI_TEST_DATA_ROOT=os.environ['PYVISI_TEST_DATA_ROOT']
except KeyError:
	PYVISI_TEST_DATA_ROOT='.'

PYVISI_TEST_MESHES_PATH = os.path.join(PYVISI_TEST_DATA_ROOT, "data_meshes")
PYVISI_TEST_MAP_IMAGES_PATH = os.path.join(PYVISI_WORKDIR, \
		"data_sample_images", "map")

MIN_IMAGE_SIZE = 100
FILE_2D = "interior_2D.xml"
FILE_3D = "interior_3D.xml"
FILE_2D_ROTATION = "without_st.0700.xml"
FILE_SECOND_ORDER_3D = "temp-000585.vtu"
X_SIZE = 400
Y_SIZE = 400

JPG_RENDERER = Renderer.OFFLINE_JPG
SCALAR_FIELD_CELL_DATA = "temperature_cell"
VECTOR_FIELD_CELL_DATA = "velocity_cell"
TENSOR_FIELD_CELL_DATA = "stress_cell"

class TestMap:
	def render(self, file):
		self.scene.render(image_name = \
				os.path.join(PYVISI_TEST_MAP_IMAGES_PATH, file))

		self.failUnless(os.stat(os.path.join(PYVISI_TEST_MAP_IMAGES_PATH, \
				file))[ST_SIZE] > MIN_IMAGE_SIZE)

class TestMapOneViewport(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)
	
		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_2D))
		
		self.map = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def testOneViewport(self):
		self.render("TestMapOneViewport.jpg")	

class TestMapFourViewports(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 4,
				x_size = X_SIZE, y_size = Y_SIZE)
	
		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_2D))
		
		self.map1 = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

		self.map2 = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.NORTH_WEST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

		self.map3 = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.NORTH_EAST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

		self.map4 = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_EAST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map1
		del self.map2
		del self.map3
		del self.map4

	def testSetOpacity(self):
		self.map1.setOpacity(0.2)
		self.map2.setOpacity(0.4)
		self.map3.setOpacity(0.6)
		self.map4.setOpacity(0.8)
		self.render("TestMapFourViewports_testSetOpacity.jpg")	

	def testSetColor(self):
		self.map1.setColor(Color.GREY)
		self.map3.setColor(Color.YELLOW)
		self.render("TestMapFourViewports_testSetColor.jpg")

	def testSetRepresentationToWireframe(self):
		self.map2.setRepresentationToWireframe()
		self.map4.setRepresentationToWireframe()
		self.render("TestMapFourViewports_testSetRepresentationToWireframe.jpg")

class TestMap2DCellDataWithCellToPointConversion(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)
	
		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_2D))
		self.data_collector.setActiveScalar(SCALAR_FIELD_CELL_DATA)
		
		self.map = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = True, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def test2DCellDataWithCellToPointConversion(self):
		self.render("TestMap2DCellDataWithCellToPointConversion.jpg")

class TestMap2DCellDataWithoutCellToPointConversion(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)

		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_2D))
		self.data_collector.setActiveScalar(SCALAR_FIELD_CELL_DATA)
		
		self.map = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def test2DCellDataWithoutCellToPointConversion(self):
		self.render("TestMap2DCellDataWithoutCellToPointConversion.jpg")

class TestMap3DPointData(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)

		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_3D))
		
		self.map = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def test3DPointData(self):
		self.render("TestMap3DPointData.jpg")

class TestMap3DCellDataWithCellToPointConversion(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)

		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_3D))
		self.data_collector.setActiveScalar(SCALAR_FIELD_CELL_DATA)
		
		self.map = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = True, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def test3DCellDataWithCellToPointConversion(self):
		self.render("TestMap3DCellDataWithCellToPointConversion.jpg")

class TestMap3DCellDataWithoutCellToPointConversion(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)

		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_3D))
		self.data_collector.setActiveScalar(SCALAR_FIELD_CELL_DATA)
		
		self.map = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def test3DCellDataWithoutCellToPointConversion(self):
		self.render("TestMap3DCellDataWithoutCellToPointConversion.jpg")

class TestMap3DSecondOrder(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)

		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_SECOND_ORDER_3D))
		
		self.map = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def test3DSecondOrder(self):
		self.render("TestMap3DSecondOrder.jpg")


class TestMapGreyScaleLut(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)

		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_2D))
		self.data_collector.setActiveScalar(SCALAR_FIELD_CELL_DATA)
		
		self.map = Map(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.GREY_SCALE,
				cell_to_point = False, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def testGreyScaleLut(self):
		self.render("TestMapGreyScaleLut.jpg")


###############################################################################


from esys.pyvisi import MapOnPlaneCut

class TestMapOnPlaneCut(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)
	
		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_3D))
		
		self.map = MapOnPlaneCut(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def testTranslate(self):
		self.map.setPlaneToXZ()
		self.map.translate(0, 0.3, 0)
		self.render("TestMapOnPlaneCut_testTranslate.jpg")
	
	def testRotate(self):
		self.map.setPlaneToXY()
		self.map.rotateX(20)
		self.map.rotateY(20)
		self.render("TestMapOnPlaneCut_testRotate.jpg")	


###############################################################################


from esys.pyvisi import MapOnPlaneClip

class TestMapOnPlaneClip(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)
	
		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_3D))
		
		self.map = MapOnPlaneClip(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def testSetInsideOutOff(self):
		self.map.setPlaneToYZ()
		self.map.rotateZ(20)
		self.map.setInsideOutOff()
		self.render("TestMapOnPlaneClip_testSetInsideOutOff.jpg")


###############################################################################
		

from esys.pyvisi import MapOnScalarClip

class TestMapOnScalarClip(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)
	
		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_3D))
		
		self.map = MapOnScalarClip(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = False, outline = True)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def testSetClipValue(self):
		self.map.setClipValue(0)
		self.render("TestMapOnScalarClip_testSetClipValue.jpg")
		

###############################################################################


from esys.pyvisi import MapOnScalarClipWithRotation

class TestMapOnScalarClipWithRotation(unittest.TestCase, TestMap):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
				x_size = X_SIZE, y_size = Y_SIZE)
	
		self.data_collector = DataCollector(source = Source.XML)
		self.data_collector.setFileName(file_name = \
				os.path.join(PYVISI_TEST_MESHES_PATH, FILE_2D_ROTATION))
		
		self.map = MapOnScalarClipWithRotation(scene = self.scene, 
				data_collector = self.data_collector,
				viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR,
				cell_to_point = False)

	def tearDown(self):
		del self.scene
		del self.data_collector
		del self.map

	def testSetAngle(self):
		self.map.setAngle(200)
		self.render("TestMapOnScalarClipWithRotation_testSetAngle.jpg")


###############################################################################


if __name__ == '__main__':
    if getMPISizeWorld() == 1: 
	suite = unittest.TestSuite()
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMapOneViewport))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMapFourViewports))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMap2DCellDataWithCellToPointConversion))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMap2DCellDataWithoutCellToPointConversion))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMap3DPointData))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMap3DCellDataWithCellToPointConversion))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMap3DCellDataWithoutCellToPointConversion))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMapGreyScaleLut))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMapOnPlaneCut))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMapOnPlaneClip))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMapOnScalarClip))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMapOnScalarClipWithRotation))
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMap3DSecondOrder))
	s=unittest.TextTestRunner(verbosity=2).run(suite)
        if not s.wasSuccessful(): sys.exit(1)
    else:
        print "run_map.py is not executed as more than one processor is used."

