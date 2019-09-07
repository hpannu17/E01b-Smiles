#!/usr/bin/env python3

import utils, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800 #window width
SCREEN_HEIGHT = 600 #window height
SCREEN_TITLE = "Smiley Face Example" #window title

class Faces(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Show the mouse cursor
        self.set_mouse_visible(True)

        self.x = SCREEN_WIDTH / 2 #not sure what this is. I changed the number, but still nothing seemed to change
        self.y = SCREEN_HEIGHT / 2 #same as above

        arcade.set_background_color(open_color.white) #the background of the window

    def on_draw(self):
        """ Draw the face """
        arcade.start_render()
        face_x,face_y = (self.x,self.y) #this says that the face will change based on the mouse. there is no set position for the face
        smile_x,smile_y = (face_x + 0,face_y - 10) #the arc used as a smile on the face
        eye1_x,eye1_y = (face_x - 30,face_y + 20) #where the left eye is on the face (at least that is what it is supposed to be)
        eye2_x,eye2_y = (face_x + 30,face_y + 20) #where the right eye is on the face (at least that is what is is supposed to be)
        catch1_x,catch1_y = (face_x - 25,face_y + 25) #where the gray dot is (this one is supposed to be on the left eye)
        catch2_x,catch2_y = (face_x + 35,face_y + 25) #where the gray dot is supposed to be on the right eye

        arcade.draw_circle_filled(face_x, face_y, 100, open_color.yellow_3) #how much of the circle will be filled. if the number exceeds the circle, it will be like the circle is on another circle
        arcade.draw_circle_outline(face_x, face_y, 100, open_color.black,4) #where the outline of the circle will fall. if it is far bigger than the perimeter of the circle, it will be like the circle has no outline and is in another circle
        arcade.draw_ellipse_filled(eye1_x,eye1_y,15,25,open_color.black) #same as above except it is where the black oval for the eye on the face
        arcade.draw_ellipse_filled(eye2_x,eye2_y,15,25,open_color.black) #same as above except it is the other eye (this one is meant to be the right eye)
        arcade.draw_circle_filled(catch1_x,catch1_y,3,open_color.gray_2) #the gray dot on the face and eye (meant to be on the left eye)
        arcade.draw_circle_filled(catch2_x,catch2_y,3,open_color.gray_2) #the gray dot on the face and eye (meant to be on the right)
        arcade.draw_arc_outline(smile_x,smile_y,60,50,open_color.black,190,350,4) #where the smile falls on the face. if it exceeds the face, it will be still attached to it, but the excess will just be outside the face


    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        self.x = x
        self.y = y



window = Faces()
arcade.run()