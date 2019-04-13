import os
import pygame
from pygame.locals import *
from piece import Piece
import random

class Chess:
    def __init__(self):
        # screen dimensions
        screen_width = 640
        screen_height = 750
        # flag to know if game menu has been showed
        self.menu_showed = False
        # flag to set game loop
        self.running = True
        # base folder for program resources
        self.resources = "res"
 
        # initialize game window
        pygame.display.init()
        # initialize font for text
        pygame.font.init()

        # create game window
        self.screen = pygame.display.set_mode([screen_width, screen_height])
        # background color
        bg_color = (255, 255, 255)
        # set background color
        self.screen.fill(bg_color)

        # title of window
        window_title = "Chess"
        # set window caption
        pygame.display.set_caption(window_title)

        # get location of game icon
        icon_src = os.path.join(self.resources, "chess_icon.png")
        # load game icon
        icon = pygame.image.load(icon_src)
        # set game icon
        pygame.display.set_icon(icon)
        # update display
        pygame.display.flip()
        # set game clock
        self.clock = pygame.time.Clock()

    def start_game(self):
        """Function containing main game loop"""
        # game loop
        while self.running:
            self.clock.tick(60)
            # poll events
            for event in pygame.event.get():
                # get keys pressed
                key_pressed = pygame.key.get_pressed()
                # check if the game has been closed by the user
                if event.type == pygame.QUIT or key_pressed[K_ESCAPE]:
                    # set flag to break out of the game loop
                    self.running = False
                # if key_pressed[K_SPACE]:
                #     self.reset()
            
            # if self.menu_showed == False:
            #     self.menu()
            # else:
            #     self.game()

            # mechanics of the game
            self.game()
            # update display
            pygame.display.flip()
            # update events
            pygame.event.pump()

        # call method to stop pygame
        pygame.quit()

    
    def menu(self):
        """method to show game menu"""
        # black color
        black_color = (0, 0, 0)
        # coordinates for "Play" button
        start_btn = pygame.Rect(270, 300, 100, 50)
        # show play button
        pygame.draw.rect(self.screen, black_color, start_btn)

        # white color
        white_color = (255, 255, 255)
        # create fonts for texts
        big_font = pygame.font.SysFont("comicsansms", 50)
        small_font = pygame.font.SysFont("comicsansms", 20)
        # create text to be shown on the game menu
        welcome_text = big_font.render("Chess", False, black_color)
        created_by = small_font.render("Created by Sheriff", True, black_color)
        start_btn_label = small_font.render("Play", True, white_color)
        
        # show welcome text
        self.screen.blit(welcome_text, 
                      ((self.screen.get_width() - welcome_text.get_width()) // 2, 
                      150))
        # show credit text
        self.screen.blit(created_by, 
                      ((self.screen.get_width() - created_by.get_width()) // 2, 
                      self.screen.get_height() - created_by.get_height() - 100))
        # show text on the Play button
        self.screen.blit(start_btn_label, 
                      ((start_btn.x + (start_btn.width - start_btn_label.get_width()) // 2, 
                      start_btn.y + (start_btn.height - start_btn_label.get_height()) // 2)))

        # get pressed keys
        key_pressed = pygame.key.get_pressed()
        # call function to get mouse event
        ret, mouse_coords = self.mouse_event()

        # check if "Play" button was clicked
        if start_btn.collidepoint(mouse_coords[0], mouse_coords[1]):
            # change button behavior as it is hovered
            pygame.draw.rect(self.screen, white_color, start_btn, 3)
            # check if left mouse button was clicked
            if ret:
                # change menu flag
                self.menu_showed = True
        # check if enter or return key was pressed
        elif key_pressed[K_RETURN]:
            self.menu_showed = True

    def game(self):
        # background color
        color = (0,0,0)
        # set backgound color
        self.screen.fill(color)
        
        # chess board offset
        board_offset_x = 0
        board_offset_y = 50
        self.board_dimensions = (board_offset_x, board_offset_y)
        
        # get location of chess board image
        board_src = os.path.join(self.resources, "board.png")
        # load the chess board image 
        board_img = pygame.image.load(board_src).convert()
        # show the chess board
        self.screen.blit(board_img, self.board_dimensions)

        # get the width of a chess board square
        width = board_img.get_rect().width // 8
        # get the height of a chess baord square
        height = board_img.get_rect().height // 8
        # initialize list that stores all places to put chess pieces on the board
        self.board_locations = []

        # getting errors here
        for x in range(0, 8):
            self.board_locations.append([])
            for y in range(0, 8):
                self.board_locations[x].append([board_offset_x+(x*width), board_offset_y+(y*height)])
        
        # get location of image containing the chess pieces
        pieces_src = os.path.join(self.resources, "pieces.png")
        # create an object of class to show chess pieces on the board
        chess_pieces = Piece(pieces_src, cols=6, rows=2)

        # show chess pieces on the board
        for i in range(0, 8):
            for j in range(0, 8):
                # pick a random chess piece
                y = random.randint(0, 6)
                # call method to draw a chess piece on the board
                chess_pieces.draw(self.screen, y, self.board_locations[i][j])

        # put white on 
        # coords = self.board_locations[i][j]
        # x = pygame.Rect(coords[0], coords[1], 81, 81)
        # pygame.draw.rect(self.screen, (255,255,255), x, 0)

    def mouse_event(self):
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