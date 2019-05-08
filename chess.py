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
                self.piece_location[chr(i)][a] = ["", False, [x,y]]
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
        surface = pygame.Surface((self.square_length, self.square_length), pygame.SRCALPHA)
        surface.fill(transparent_green)

        surface1 = pygame.Surface((self.square_length, self.square_length), pygame.SRCALPHA)
        surface1.fill(transparent_blue)

        for val in self.piece_location.values():
            for value in val.values() :
                # name of the piece in the current location
                piece_name = value[0]
                # x, y coordinates of the current piece
                piece_coord_x, piece_coord_y = value[2]

                # change background color of piece if it is selected
                if value[1] and len(value[0]) > 5:
                    moves = self.possible_moves(piece_name, (piece_coord_x, piece_coord_y))

                    # if the piece selected is a black piece
                    if value[0][:5] == "black":
                        self.screen.blit(surface, self.board_locations[piece_coord_x][piece_coord_y])
                        if len(moves) > 0:
                            for move in moves:
                                x_coord = move[0]
                                y_coord = move[1]
                                if x_coord >= 0 and y_coord >= 0 and x_coord < 8 and y_coord < 8:
                                    self.screen.blit(surface, self.board_locations[x_coord][y_coord])
                    # if the piece selected is a white piece
                    elif value[0][:5] == "white":
                        self.screen.blit(surface1, self.board_locations[piece_coord_x][piece_coord_y])
                        if len(moves) > 0:
                            for move in moves:
                                x_coord = move[0]
                                y_coord = move[1]
                                if x_coord >= 0 and y_coord >= 0 and x_coord < 8 and y_coord < 8:
                                    self.screen.blit(surface1, self.board_locations[x_coord][y_coord])

        for val in self.piece_location.values():
            for value in val.values() :
                # name of the piece in the current location
                piece_name = value[0]
                # x, y coordinates of the current piece
                piece_coord_x, piece_coord_y = value[2]
                # check if there is a piece at the square
                if(len(value[0]) > 1):
                    # draw piece on the board
                    self.chess_pieces.draw(self.screen, piece_name, 
                                            self.board_locations[piece_coord_x][piece_coord_y])


    # helper function to find diagonal moves
    def diagonal_moves(self, positions, piece_coord):
        # reset x and y coordinate values
        x, y = piece_coord
        # find top left diagonal spots
        while(True):
            x = x - 1
            y = y - 1
            if(x < 0 or y <= 0):
                break
            else:
                positions.append([x,y])

        # reset x and y coordinate values
        x, y = piece_coord
        # find bottom right diagonal spots
        while(True):
            x = x + 1
            y = y + 1
            if(x > 8 or y > 8):
                break
            else:
                positions.append([x,y])

        # reset x and y coordinate values
        x, y = piece_coord
        # find bottom left diagonal spots
        while(True):
            x = x - 1
            y = y + 1
            if (x < 0 or y > 8):
                break
            else:
                positions.append([x,y])

        # reset x and y coordinate values
        x, y = piece_coord
        # find top right diagonal spots
        while(True):
            x = x + 1
            y = y - 1
            if(x > 8 or y < 0):
                break
            else:
                positions.append([x,y])

        return positions
    

    # helper function to find horizontal and vertical moves
    def linear_moves(self, positions, piece_coord):
        # reset x, y coordniate value
        x, y = piece_coord
        # horizontal moves to the left
        while(x > 0):
            x = x - 1
            positions.append([x,y])

        # reset x, y coordniate value
        x, y = piece_coord
        # horizontal moves to the right
        while(x < 7):
            x = x + 1
            positions.append([x,y])

        # reset x, y coordniate value
        x, y = piece_coord
        # vertical moves upwards
        while(y > 0):
            y = y - 1
            positions.append([x,y])

        # reset x, y coordniate value
        x, y = piece_coord
        # vertical moves downwards
        while(y < 7):
            y = y + 1
            positions.append([x,y])

        return positions


    def possible_moves(self, piece_name, piece_coord):
        # list to store possible moves of the selected piece
        positions = []
        # find the possible locations to put a piece
        if len(piece_name) > 0:
            # 
            x_coord, y_coord = piece_coord
            # calculate moves for bishop
            if piece_name[6:] == "bishop":
                positions = self.diagonal_moves(positions, piece_coord)
            
            # calculate moves for pawn
            elif piece_name[6:] == "pawn":
                # calculate moves for white pawn
                if piece_name[:5] == "black":
                    if y_coord + 1 < 8:
                        positions.append([x_coord, y_coord+1])
                        # black pawns can move two positions ahead for first move
                        if y_coord < 2:
                            positions.append([x_coord, y_coord+2])
                # calculate moves for white pawn
                elif piece_name[:5] == "white":
                    if y_coord - 1 >= 0:
                        positions.append([x_coord, y_coord-1])
                        # black pawns can move two positions ahead for first move
                        if y_coord > 5:
                            positions.append([x_coord, y_coord-2])

            # calculate moves for rook
            elif piece_name[6:] == "rook":
                # find linear moves
                positions = self.linear_moves(positions, piece_coord)

            # calculate moves for knight
            elif piece_name[6:] == "knight":
                # left positions
                if(x_coord - 2) >= 0:
                    if(y_coord - 1) >= 0:
                        positions.append([x_coord-2, y_coord-1])
                    if(y_coord + 1) < 8:
                        positions.append([x_coord-2, y_coord+1])
                # top positions
                if(y_coord - 2) >= 0:
                    if(x_coord - 1) >= 0:
                        positions.append([x_coord-1, y_coord-2])
                    if(x_coord + 1) < 8:
                        positions.append([x_coord+1, y_coord-2])
                # right positions
                if(x_coord + 2) < 8:
                    if(y_coord - 1) >= 0:
                        positions.append([x_coord+2, y_coord-1])
                    if(y_coord + 1) < 8:
                        positions.append([x_coord+2, y_coord+1])
                # bottom positions
                if(y_coord + 2) < 8:
                    if(x_coord - 1) >= 0:
                        positions.append([x_coord-1, y_coord+2])
                    if(x_coord + 1) < 8:
                        positions.append([x_coord+1, y_coord+2])

            # calculate movs for king
            elif piece_name[6:] == "king":
                if(y_coord - 1) >= 0:
                    # top spot
                    positions.append([x_coord, y_coord-1])

                if(y_coord + 1) < 8:
                    # bottom spot
                    positions.append([x_coord, y_coord+1])

                if(x_coord - 1) >= 0:
                    # left spot
                    positions.append([x_coord-1, y_coord])
                    # top left spot
                    if(y_coord - 1) >= 0:
                        positions.append([x_coord-1, y_coord-1])
                    # bottom left spot
                    if(y_coord + 1) < 8:
                        positions.append([x_coord-1, y_coord+1])
                    
                if(x_coord + 1) < 8:
                    # right spot
                    positions.append([x_coord+1, y_coord])
                    # top right spot
                    if(y_coord - 1) >= 0:
                        positions.append([x_coord+1, y_coord-1])
                    # bottom right spot
                    if(y_coord + 1) < 8:
                        positions.append([x_coord+1, y_coord+1])
                
            # calculate movs for queen
            elif piece_name[6:] == "queen":
                # find diagonal positions
                positions = self.diagonal_moves(positions, piece_coord)

                # find linear moves
                positions = self.linear_moves(positions, piece_coord)

        # return list containing possible moves for the selected piece
        return positions


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


# fix bug
# remove positions that have been occupied by other pieces
"""
for item in self.piece_location.values():
    for value in item.values():
        # if the selected piece is for the current player
        #if(value[0][:5] == piece_name[:5]):
        print("to remove", value[2])
        try:
            positions.remove((value[2][0], value[2][1]))
        except:
            pass
#print("after", positions)
"""