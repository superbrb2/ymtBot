import pygame
import fen_parser
import math
from peices import *
from typing import Tuple

HEIGHT = 700
WIDTH = 700

DIMENSION = 8
SQ_HEIGHT = HEIGHT / DIMENSION
SQ_WIDTH = WIDTH / DIMENSION

class Board():
    def __init__(self):
        self.piece_count = 32
        
        self.image_board = [
            ['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']    
        ]

        self.white_pawns = [
            Pawn('wp1',(6,0)),
            Pawn('wp2',(6,1)),
            Pawn('wp3',(6,2)),
            Pawn('wp4',(6,3)),
            Pawn('wp5',(6,4)),
            Pawn('wp6',(6,5)),
            Pawn('wp7',(6,6)),
            Pawn('wp8',(6,7)),
        ]
        
        self.black_pawns = [
            Pawn('bp1',(1,0)),
            Pawn('bp2',(1,1)),
            Pawn('bp3',(1,2)),
            Pawn('bp4',(1,3)),
            Pawn('bp5',(1,4)),
            Pawn('bp6',(1,5)),
            Pawn('bp7',(1,6)),
            Pawn('bp8',(1,7)),
        ]
        
        self.white_pieces = [
            Rook('wr1',(7,0)),
            Knight('wn1',(7,1)),
            Bishop('wb1',(7,2)),
            Queen('wq1',(7,3)),
            King('wk1',(4,4)),
            Bishop('wb2',(7,5)),
            Knight('wn2',(7,6)),
            Rook('wr2',(7,7))
        ]
        
        self.black_pieces = [
            Rook('br1',(0,0)),
            Knight('bn1',(0,1)),
            Bishop('bb1',(0,2)),
            Queen('bq1',(0,3)),
            King('bk1',(0,4)),
            Bishop('bb2',(0,5)),
            Knight('bn2',(0,6)),
            Rook('br2',(0,7))
        ]
        
    def check_peices(self):
        current_count = len(self.white_pawns)+len(self.white_pieces)+len(self.black_pawns)+len(self.black_pieces)
        if current_count != self.piece_count:
            return self.piece_count - current_count
        return 0
    
    def find_peice(self,pos) -> Tuple[int,str]:
        for i in range(len(self.black_pieces)):
            if pos[0] == self.black_pieces[i].get_position()[0] and pos[1] == self.black_pieces[i].get_position()[1]:
                list_pos = i
                return list_pos,'bP'
        for i in range(len(self.white_pieces)):    
            if pos[0] == self.white_pieces[i].get_position()[0] and pos[1] == self.white_pieces[i].get_position()[1]:
                list_pos = i
                return list_pos, 'wP'
        for i in range(len(self.black_pawns)):
            if pos[0] == self.black_pawns[i].get_position()[0] and pos[1] == self.black_pawns[i].get_position()[1]:
                list_pos = i
                return list_pos,'bp'
        for i in range(len(self.white_pawns)):
            if pos[0] == self.white_pawns[i].get_position()[0] and pos[1] == self.white_pawns[i].get_position()[1]:
                list_pos = i
                return list_pos,'wp'
                
        return None
    
    def find_peice_colour(self,pos):
        for i in range(len(self.black_pieces)):
            if pos[0] == self.black_pieces[i].get_position()[0] and pos[1] == self.black_pieces[i].get_position()[1]:
                return self.black_pieces[i].get_colour()
        for i in range(len(self.white_pieces)):
            if pos[0] == self.white_pieces[i].get_position()[0] and pos[1] == self.white_pieces[i].get_position()[1]:
                return self.white_pieces[i].get_colour()
        for i in range(len(self.black_pawns)):
            if pos[0] == self.black_pawns[i].get_position()[0] and pos[1] == self.black_pawns[i].get_position()[1]:
                return self.black_pawns[i].get_colour()
        for i in range(len(self.white_pawns)):
            if pos[0] == self.white_pawns[i].get_position()[0] and pos[1] == self.white_pawns[i].get_position()[1]:
                return self.white_pawns[i].get_colour()
        
        '''
        self.peice_board = [
            [Rook('br1',(0,0)),Knight('bn1'),Bishop('bb1'),Queen('bq1'),King('bk1'),Bishop('bb2'),Knight('bn2'),Rook('br2')],
            [Pawn('bp1'),Pawn('bp2'),Pawn('bp3'),Pawn('bp4'),Pawn('bp5'),Pawn('bp6'),Pawn('bp7'),Pawn('bp8')],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            [Pawn('wp1'),Pawn('wp2'),Pawn('wp3'),Pawn('wp4'),Pawn('wp5'),Pawn('wp6'),Pawn('wp7'),Pawn('wp8')],
            [Rook('wr1'),Knight('wn1'),Bishop('wb1'),Queen('wq1'),King('wk1'),Bishop('wb2'),Knight('wn2'),Rook('wr2')]
        ]
        '''

class ButtonArray():
    def __init__(self):
        self.input_pos: list = [-1,-1]
        
    def get_position_of_press(self):
        mouse_pos = pygame.mouse.get_pos()
        x = int(math.floor(mouse_pos[0]//SQ_WIDTH))
        y = int(math.floor(mouse_pos[1]//SQ_HEIGHT))
        
        return (y,x)
        
        
    def add_button_press(self):
        new_pos: tuple = self.get_position_of_press()
        
        if self.input_pos[1] != -1:
            self.input_pos = [-1,-1]
        
        if self.input_pos[0] == -1:
            self.input_pos[0] = new_pos
        elif self.input_pos[1] == -1:
            self.input_pos[1] = new_pos
            if self.input_pos[0] == self.input_pos[1]:
                self.input_pos = [-1,-1]
    
    def get_input_pos(self):
        if self.input_pos[1] == -1:
            return [-1,-1]
        return self.input_pos

    def reset_input_pos(self):
        self.input_pos = [-1,-1]
            
            

class gameState():         
    def __init__(self):
        self.board = Board()
        self.button_array = ButtonArray()
        self.fen_position: str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        
        self.white_to_move = True
        self.enpassant_pos: tuple 
        self.castling: str
        
        self.pos_last_move: tuple
        
    def button_press(self):
        self.button_array.add_button_press()
        if self.button_array.get_input_pos()[1] != -1:
            self.pos_last_move = self.button_array.get_input_pos()[1]
            self.move_pieces()
            
    def move_pieces(self):
        piece_data = self.board.find_peice(self.button_array.get_input_pos()[0]) 
        if piece_data != None:
            list_pos, list_reference = piece_data
        else:
            self.button_array.reset_input_pos()
            return
        
        if list_reference == 'wp':
            selected_piece = self.board.white_pawns[list_pos]
        if list_reference == 'bp':
            selected_piece = self.board.black_pawns[list_pos]
        if list_reference == 'wP':
            selected_piece = self.board.white_pieces[list_pos]
        if list_reference == 'bP':
            selected_piece = self.board.black_pieces[list_pos]
        
        # print(selected_piece.get_moves(self.board.image_board))
        if self.button_array.get_input_pos()[1] in selected_piece.get_moves(self.board.image_board):
            
            # Check for collision
            piece_colour = self.board.find_peice_colour(self.button_array.get_input_pos()[1]) 
            if piece_colour == None:
                colour_check = True
            else:
                colour_check = piece_colour != selected_piece.get_colour()
            
            collision_data = self.board.find_peice(self.button_array.get_input_pos()[1])
            if collision_data == None or colour_check:
                
                if colour_check and collision_data != None:
                    list_pos_2nd, list_reference_2nd = collision_data
                        
                    if list_reference_2nd == 'wp':
                        del self.board.white_pawns[list_pos_2nd]
                    if list_reference_2nd == 'bp':
                        del self.board.black_pawns[list_pos_2nd]
                    if list_reference_2nd == 'wP':
                        del self.board.white_pieces[list_pos_2nd]
                    if list_reference_2nd == 'bP':
                        del self.board.black_pieces[list_pos_2nd]
                    
                # move piece on board
                piece_pos = self.button_array.get_input_pos()
                temp = self.board.image_board[int(piece_pos[0][0])][int(piece_pos[0][1])]
                self.board.image_board[int(piece_pos[0][0])][int(piece_pos[0][1])] = '-'
                self.board.image_board[int(piece_pos[1][0])][int(piece_pos[1][1])] = temp
                
                # Change pos of piece
                selected_piece.update_position(self.button_array.get_input_pos()[1])
                
                # Check for first move
                selected_piece.update_first_move()
            
            # Add selected_piece back into object list
            if list_reference == 'wp':
                self.board.white_pawns[list_pos] = selected_piece
            if list_reference == 'bp':
                self.board.black_pawns[list_pos] = selected_piece
            if list_reference == 'wP':
                self.board.white_pieces[list_pos] = selected_piece 
            if list_reference == 'bP':
                self.board.black_pieces[list_pos] = selected_piece
            
        
        self.button_array.reset_input_pos()
    
    def check_board(self):
        self.board.check_peices()
        
    def decode_fen(self):
        fen_to_position = fen_parser.FenToChessPosition(self.fen_position)
        return fen_to_position.parse()
        
        
    def encode_fen(self):
        position_to_fen = fen_parser.ChessPositionToFEN(self.board.image_board)
        self.fen_position = position_to_fen.board_to_fen()
        return self.fen_position


    def get_image_board(self):
        return self.board.image_board
    
    
    
