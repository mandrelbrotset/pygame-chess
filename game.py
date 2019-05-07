import os
import pygame
from pygame.locals import *
from piece import Piece
from chess import Chess
from utils import Utils

class Game:
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
        # chess board offset
        self.board_offset_x = 0
        self.board_offset_y = 50
        self.board_dimensions = (self.board_offset_x, self.board_offset_y)
        
        # get location of chess board image
        board_src = os.path.join(self.resources, "board.png")
        # load the chess board image 
        self.board_img = pygame.image.load(board_src).convert()

        # get the width of a chess board square
        square_length = self.board_img.get_rect().width // 8

        # initialize list that stores all places to put chess pieces on the board
        self.board_locations = []

        # getting errors here
        for x in range(0, 8):
            self.board_locations.append([])
            for y in range(0, 8):
                self.board_locations[x].append([self.board_offset_x+(x*square_length), 
                                                self.board_offset_y+(y*square_length)])

        #for i in self.board_locations:
        #    print(i)

        # get location of image containing the chess pieces
        pieces_src = os.path.join(self.resources, "pieces.png")
        # create class object that handles the gameplay logic
        self.chess = Chess(self.screen, pieces_src, self.board_locations, square_length)

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
                elif key_pressed[K_SPACE]:
                    self.chess.reset()
            
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
        # 
        util = Utils()
        # call function to get mouse event
        ret, mouse_coords = util.get_mouse_event()

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
        
        # show the chess board
        self.screen.blit(self.board_img, self.board_dimensions)

        # call self.chess. something
        self.chess.play_turn()
        # draw pieces on the chess board
        self.chess.draw_pieces()
        # 
        self.chess.move_piece()