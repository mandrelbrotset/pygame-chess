import pygame
from pygame.locals import *
import random

from piece import Piece
from utils import Utils

class Chess(object):
    def __init__(self, screen, pieces_src, square_coords):
        # display surface
        self.screen = screen
        # create an object of class to show chess pieces on the board
        self.chess_pieces = Piece(pieces_src, cols=6, rows=2)
        # store coordinates of the chess board squares
        self.board_locations = square_coords

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

        # reset the board
        self.piece_location = {}
        for i in range(97, 105):
            x = 8
            self.piece_location[chr(i)] = {}
            while x>0:
                if(x==8):
                    if(chr(i)=='a' or chr(i)=='h'):
                        self.piece_location[chr(i)][x] = "black_pawn"
                    elif(chr(i)=='b' or chr(i)=='g'):
                        self.piece_location[chr(i)][x] = "black_knight"
                    elif(chr(i)=='c' or chr(i)=='f'):
                        self.piece_location[chr(i)][x] = "black_bishop"
                    elif(chr(i)=='d'):
                        self.piece_location[chr(i)][x] = "black_queen"
                    elif(chr(i)=='e'):
                        self.piece_location[chr(i)][x] = "black_king"
                elif(x==7):
                    self.piece_location[chr(i)][x] = "black_pawn"
                elif(x==2):
                    self.piece_location[chr(i)][x] = "white_pawn"
                elif(x==1):
                    if(chr(i)=='a' or chr(i)=='h'):
                        self.piece_location[chr(i)][x] = "white_pawn"
                    elif(chr(i)=='b' or chr(i)=='g'):
                        self.piece_location[chr(i)][x] = "white_knight"
                    elif(chr(i)=='c' or chr(i)=='f'):
                        self.piece_location[chr(i)][x] = "white_bishop"
                    elif(chr(i)=='d'):
                        self.piece_location[chr(i)][x] = "white_queen"
                    elif(chr(i)=='e'):
                        self.piece_location[chr(i)][x] = "white_king"
                else:
                    self.piece_location[chr(i)][x] = ""
                x = x - 1

        print(self.piece_location)

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
        x = 0
        y = 0
        for val in self.piece_location.values():
            for value in val.values() :
                if(len(value) > 1):
                    self.chess_pieces.draw(self.screen, value, self.board_locations[x][y])
                y = y + 1
            x = x + 1
            if(x>7):
                x = 0
            if(y>7):
                y=0

    def move_piece(self):
        utils = Utils()
        mouse_event = utils.get_mouse_event()



        