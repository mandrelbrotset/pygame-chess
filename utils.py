import pygame
from pygame.locals import *

class Utils:
    def get_mouse_event(self):
        # get coordinates of the mouse
        position = pygame.mouse.get_pos()
        # create flag to check for left click event
        left_click = False
        # store mouse buttons
        mouse_btn = pygame.mouse.get_pressed()
        # check if left mouse button was pressed
        if mouse_btn[0]:
            # change left click flag
            left_click = True
        # return left click status and mouse coordinates
        return left_click, position