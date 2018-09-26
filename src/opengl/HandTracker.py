from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import cv2
from PIL import Image
import numpy as np
#from webcam import Webcam
#from detection import Detection


class HandTracker:

    def __init__(self):
        # self.webcam = Webcam()
        # self.webcam.start()
        #
        # self.detection = Detection()

        self.x_axis = 0.0
        self.z_axis = 0.0
        self.show_cube = True
        self.texture_background = None
        self.texture_cube = None


    def _init_gl(self, Width, Height):
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glDepthFunc(GL_LESS)
        glEnable(GL_DEPTH_TEST)
        glShadeModel(GL_SMOOTH)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, float(Width) / float(Height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

        # enable texture
        glEnable(GL_TEXTURE_2D)
        self.texture_background = glGenTextures(1)
        self.texture_cube = glGenTextures(1)

        # create cube texture
        image = Image.open("devel.jpg")
        ix = image.size[0]
        iy = image.size[1]
        image = image.tobytes("raw", "RGBX", 0, -1)

        glBindTexture(GL_TEXTURE_2D, self.texture_cube)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, image)


    def _draw_scene(self):
        # handle any hand gesture
        self._handle_gesture()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # draw background
        glBindTexture(GL_TEXTURE_2D, self.texture_background)
        glPushMatrix()
        glTranslatef(0.0, 0.0, -11.2)
        self._draw_background()
        glPopMatrix()

        # draw cube if enabled
        if self.show_cube:
            glColor4f(1.0, 1.0, 1.0, 1.0)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE)
            glEnable(GL_BLEND)
            glDisable(GL_DEPTH_TEST)

            glBindTexture(GL_TEXTURE_2D, self.texture_cube)
            glPushMatrix()
            glTranslatef(0.0, 0.0, -7.0)
            glRotatef(self.x_axis, 1.0, 0.0, 0.0)
            glRotatef(0.0, 0.0, 1.0, 0.0)
            glRotatef(self.z_axis, 0.0, 0.0, 1.0)
            self._draw_cube()
            glPopMatrix()

            glDisable(GL_BLEND)
            glEnable(GL_DEPTH_TEST)

            # update rotation values
            self.x_axis = self.x_axis - 0.5
            # self.z_axis = self.z_axis - 0.5

        glutSwapBuffers()


    def _handle_gesture(self):
        # get image from webcam

        # detect hand gesture in image
        is_okay = True
        is_vicky = False

        if is_okay:
            # okay gesture shows cube
            self.show_cube = True
        elif is_vicky:
            # vicky gesture hides cube
            self.show_cube = False

        # convert image to OpenGL texture format
        image = np.zeros([400, 300, 3], np.uint8)
        image = cv2.flip(image, 0)
        gl_image = Image.fromarray(image)
        ix = gl_image.size[0]
        iy = gl_image.size[1]
        gl_image = gl_image.tobytes("raw", "BGRX", 0, -1)

        # create background texture
        glBindTexture(GL_TEXTURE_2D, self.texture_background)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGBA, GL_UNSIGNED_BYTE, gl_image)


    def _draw_background(self):
        # draw background
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 1.0);
        glVertex3f(-4.0, -3.0, 4.0)
        glTexCoord2f(1.0, 1.0);
        glVertex3f(4.0, -3.0, 4.0)
        glTexCoord2f(1.0, 0.0);
        glVertex3f(4.0, 3.0, 4.0)
        glTexCoord2f(0.0, 0.0);
        glVertex3f(-4.0, 3.0, 4.0)
        glEnd()


    def _draw_cube(self):
        # draw cube
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0);
        glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 0.0);
        glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 1.0);
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 1.0);
        glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 0.0);
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0);
        glVertex3f(-1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 1.0);
        glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 0.0);
        glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 1.0);
        glVertex3f(-1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 0.0);
        glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 0.0);
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 1.0);
        glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(1.0, 1.0);
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 1.0);
        glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(0.0, 0.0);
        glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 0.0);
        glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 0.0);
        glVertex3f(1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 1.0);
        glVertex3f(1.0, 1.0, -1.0)
        glTexCoord2f(0.0, 1.0);
        glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 0.0);
        glVertex3f(1.0, -1.0, 1.0)
        glTexCoord2f(0.0, 0.0);
        glVertex3f(-1.0, -1.0, -1.0)
        glTexCoord2f(1.0, 0.0);
        glVertex3f(-1.0, -1.0, 1.0)
        glTexCoord2f(1.0, 1.0);
        glVertex3f(-1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 1.0);
        glVertex3f(-1.0, 1.0, -1.0)
        glEnd()


    def main(self):
        # setup and run OpenGL
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(640, 480)
        glutInitWindowPosition(800, 400)
        glutCreateWindow("OpenGL Hand Tracker")
        glutDisplayFunc(self._draw_scene)
        glutIdleFunc(self._draw_scene)
        self._init_gl(640, 480)
        glutMainLoop()


# run instance of Hand Tracker
handTracker = HandTracker()
handTracker.main()
