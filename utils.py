import pygame
from pygame.locals import *

class Utils:
    def get_mouse_event(self):
        # store mouse buttons
        mouse_btn = pygame.mouse.get_pressed()
        # create flag to check for left click event
        left_click = False

        # check if left mouse button was pressed
        if mouse_btn[0]:
            # change left click flag
            left_click = True
        
        if left_click:
            # get coordinates of the mouse
            position = pygame.mouse.get_pos()
            
            # return left click status and mouse coordinates
            return position
        else:
            return None