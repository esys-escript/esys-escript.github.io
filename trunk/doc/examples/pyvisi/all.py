
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

"""
Author: John Ngui, john.ngui@uq.edu.au
"""

# Import the necessary modules.
from esys.pyvisi import Scene, DataCollector, MapOnPlaneCut, Camera 
from esys.pyvisi import VelocityOnPlaneCut, StreamLine, EllipsoidOnPlaneCut
from esys.pyvisi import ContourOnPlaneClip, Text2D, LocalPosition
from esys.pyvisi.constant import *
import os

PYVISI_EXAMPLE_MESHES_PATH = "data_meshes"
PYVISI_EXAMPLE_IMAGES_PATH = "data_sample_images"
X_SIZE = 800
Y_SIZE = 800

FILE_3D = "interior_3D.xml"
IMAGE_NAME = "all.jpg"
JPG_RENDERER = Renderer.ONLINE_JPG

# Create a Scene.
s = Scene(renderer = JPG_RENDERER, num_viewport = 1, x_size = X_SIZE, 
        y_size = Y_SIZE)

# Create a DataCollector reading from a XML file.
dc1 = DataCollector(source = Source.XML)
dc1.setFileName(file_name = os.path.join(PYVISI_EXAMPLE_MESHES_PATH, FILE_3D))

# Create a MapOnPlaneCut.
mopc1 = MapOnPlaneCut(scene = s, data_collector = dc1, 
        viewport = Viewport.SOUTH_WEST)
mopc1.setPlaneToXY()

# Create a  VelocityOnPlaneCut.
vopc1 = VelocityOnPlaneCut(scene = s, data_collector = dc1,
        arrow = Arrow.THREE_D, color_mode = ColorMode.SCALAR)
vopc1.setScaleFactor(scale_factor = 0.2)
vopc1.setPlaneToYZ(offset = 2.999)

# Create a StreamLine.
sl1 = StreamLine(scene = s, data_collector = dc1,
        viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR, outline = True,
		color_mode = ColorMode.SCALAR)
sl1.setTubeRadius(radius = 0.02)

# Create an EllipsoidOnPlaneCut.
eopc1 = EllipsoidOnPlaneCut(scene = s, data_collector = dc1, 
        viewport = Viewport.SOUTH_WEST, lut = Lut.COLOR, outline = True)
eopc1.setScaleFactor(scale_factor = 0.1)
eopc1.setPlaneToXZ()
eopc1.rotateX(angle = -40)
eopc1.translate(x_offset = 0, y_offset = 0.2, z_offset = 0)

# Create a ContourOnPlaneClip.
ctropc1 = ContourOnPlaneClip(scene = s, data_collector = dc1, 
        viewport  = Viewport.SOUTH_WEST, lut = Lut.COLOR, outline = True)
ctropc1.setPlaneToXY()
ctropc1.rotateY(angle = 10)
ctropc1.generateContours(contours =  3)

# Create a 2D text.
t1 = Text2D(scene = s, viewport = Viewport.SOUTH_WEST, text = "Pyvisi")
t1.setPosition(LocalPosition(x_coor = 350, y_coor = 730))
t1.setColor(color = Color.BLACK)
t1.setFontSize(size = 30)
t1.boldOn()

# Create a  Camera.
c1 = Camera(scene = s, viewport = Viewport.SOUTH_WEST)
c1.isometricView()

# Render the object.
s.render(image_name = os.path.join(PYVISI_EXAMPLE_IMAGES_PATH, IMAGE_NAME))
