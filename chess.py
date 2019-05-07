import pygame
from pygame.locals import *
import random

from piece import Piece
from utils import Utils

class Chess(object):
    def __init__(self, screen, pieces_src, square_coords, square_length):
        # display surface
        self.screen = screen
        # create an object of class to show chess pieces on the board
        self.chess_pieces = Piece(pieces_src, cols=6, rows=2)
        # store coordinates of the chess board squares
        self.board_locations = square_coords
        # length of the side of a chess board square
        self.square_length = square_length

        self.turn = {"player_one": 0,
                     "player_two": 0}
        
        self.pieces = {
            "white_pawn":   5,
            "white_knight": 3,
            "white_bishop": 2,
            "white_rook":   4,
            "white_king":   0,
            "white_queen":  1,
            "black_pawn":   11,
            "black_knight": 9,
            "black_bishop": 8,
            "black_rook":   10,
            "black_king":   6,
            "black_queen":  7
        }

        self.reset()
    
    def reset(self):
        x = random.randint(0, 1)
        if(x == 1):
            self.turn["player_one"] = 1
        elif(x == 0):
            self.turn["player_two"] = 1

        # two dimensonal dictionary containing details about each board location
        self.piece_location = {}
        x = 0
        for i in range(97, 105):
            a = 8
            y = 0
            self.piece_location[chr(i)] = {}
            while a>0:
                # [piece name, currently selected, board coordinates]
                self.piece_location[chr(i)][a] = ["", False, (x,y)]
                a = a - 1
                y = y + 1
            x = x + 1

        # reset the board
        for i in range(97, 105):
            x = 8
            while x>0:
                if(x==8):
                    if(chr(i)=='a' or chr(i)=='h'):
                        self.piece_location[chr(i)][x][0] = "black_rook"
                    elif(chr(i)=='b' or chr(i)=='g'):
                        self.piece_location[chr(i)][x][0] = "black_knight"
                    elif(chr(i)=='c' or chr(i)=='f'):
                        self.piece_location[chr(i)][x][0] = "black_bishop"
                    elif(chr(i)=='d'):
                        self.piece_location[chr(i)][x][0] = "black_queen"
                    elif(chr(i)=='e'):
                        self.piece_location[chr(i)][x][0] = "black_king"
                elif(x==7):
                    self.piece_location[chr(i)][x][0] = "black_pawn"
                elif(x==2):
                    self.piece_location[chr(i)][x][0] = "white_pawn"
                elif(x==1):
                    if(chr(i)=='a' or chr(i)=='h'):
                        self.piece_location[chr(i)][x][0] = "white_rook"
                    elif(chr(i)=='b' or chr(i)=='g'):
                        self.piece_location[chr(i)][x][0] = "white_knight"
                    elif(chr(i)=='c' or chr(i)=='f'):
                        self.piece_location[chr(i)][x][0] = "white_bishop"
                    elif(chr(i)=='d'):
                        self.piece_location[chr(i)][x][0] = "white_queen"
                    elif(chr(i)=='e'):
                        self.piece_location[chr(i)][x][0] = "white_king"
                x = x - 1
        #print(self.piece_location)

    def play_turn(self):
        # put white on 
        coords = self.board_locations[2][5]
        # x = pygame.Rect(coords[0], coords[1], 81, 81)
        # pygame.draw.rect(self.screen, (255,255,255), x, 0)

        transparent_green = (0,194,39,170)
        transparent_blue = (28,21,212,170)

        s = pygame.Surface((81,81), pygame.SRCALPHA)   # per-pixel alpha
        #s.fill(transparent_red)                         # notice the alpha value in the color
        s.fill(transparent_green)
        #self.screen.blit(s, (coords[0], coords[1]))

        s.fill(transparent_blue)
        coords = self.board_locations[5][5]
        #self.screen.blit(s, (coords[0], coords[1]))

    def draw_pieces(self):
        transparent_green = (0,194,39,170)
        transparent_blue = (28,21,212,170)

        # create a transparent surface
        surface = pygame.Surface((81,81), pygame.SRCALPHA)
        surface.fill(transparent_green)

        surface1 = pygame.Surface((81,81), pygame.SRCALPHA)
        surface1.fill(transparent_blue)

        #self.screen.blit(s, (coords[0], coords[1]))

        for val in self.piece_location.values():
            for value in val.values() :
                if(len(value[0]) > 1):
                    piece_name = value[0]
                    piece_coord_x = value[2][0]
                    piece_coord_y = value[2][1]

                    # 
                    if value[1] and len(value[0]) > 5:
                        if value[0][:5] == "black":
                            self.screen.blit(surface, self.board_locations[piece_coord_x][piece_coord_y])
                        elif value[0][:5] == "white":
                            self.screen.blit(surface1, self.board_locations[piece_coord_x][piece_coord_y])

                    self.chess_pieces.draw(self.screen, piece_name, 
                                            self.board_locations[piece_coord_x][piece_coord_y])

    def possible_moves(self):
        pass

    def move_piece(self):
        utils = Utils()
        ret, mouse_event = utils.get_mouse_event()

        if ret:
            for i in range(len(self.board_locations)):
                for j in range(len(self.board_locations)):
                    rect = pygame.Rect(self.board_locations[i][j][0], self.board_locations[i][j][1], 
                            self.square_length, self.square_length)
                    collision = rect.collidepoint(mouse_event[0], mouse_event[1])
                    if collision:
                        selected = [rect.x, rect.y]
                        print(selected)
                        for k in range(len(self.board_locations)):
                            try:
                                l = None
                                l = self.board_locations[k].index(selected)
                                print(k, l)
                                if l != None:
                                    # reset color of all selected pieces
                                    for val in self.piece_location.values():
                                        for value in val.values() :
                                            # [piece name, currently selected, board coordinates]
                                            value[1] = False

                                    # change color of the selected piece and show possible moves
                                    columnChar = chr(97 + k)
                                    rowNo = 8 - l
                                    print(columnChar, rowNo)
                                    self.piece_location[columnChar][rowNo][1] = True
                            except:
                                pass