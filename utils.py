import pygame
from pygame.locals import *
import queue

class Utils:
    def get_mouse_event(self):
        # get coordinates of the mouse
        position = pygame.mouse.get_pos()
        
        # return left click status and mouse coordinates
        return position

    def left_click_event(self):
        # store mouse buttons
        mouse_btn = pygame.mouse.get_pressed()
        # create flag to check for left click event
        left_click = False

        if mouse_btn[0]: #and e.button == 1:
            # change left click flag
            left_click = True

        return left_click