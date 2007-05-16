from esys.pyvisi import Scene, Text2D, LocalPosition
from esys.pyvisi.constant import *
import unittest, os
from stat import ST_SIZE

PYVISI_TEST_TEXT_IMAGES_PATH = "data_sample_images/text/"
MIN_IMAGE_SIZE = 100

X_SIZE = 400
Y_SIZE = 400

JPG_RENDERER = Renderer.OFFLINE_JPG

class TestText2D(unittest.TestCase):
	def setUp(self):
		self.scene = \
				Scene(renderer = JPG_RENDERER, num_viewport = 1,
						x_size = X_SIZE, y_size = Y_SIZE)

		self.text2D = Text2D(scene = self.scene, text = "Testing ...",
				viewport = Viewport.SOUTH_WEST)

	def tearDown(self):
		self.scene
		self.text2D

	def render(self, file):
		self.scene.render(image_name = \
				PYVISI_TEST_TEXT_IMAGES_PATH + file)

		self.failUnless(os.stat(PYVISI_TEST_TEXT_IMAGES_PATH + \
				file)[ST_SIZE] > MIN_IMAGE_SIZE)


	def testText(self):
		self.text2D.setFontSize(35)
		self.text2D.setFontToArial()
		self.text2D.boldOn()
		self.text2D.shadowOn()
		self.text2D.setColor(Color.BLUE)
		self.text2D.setPosition(LocalPosition(90, 90))
		self.render("TestText2D.jpg")

			

##############################################################################


if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestText2D))
	unittest.TextTestRunner(verbosity=2).run(suite)

