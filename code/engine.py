import pygame
import fen_parser
from peices import *

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
            King('wk1',(7,4)),
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
    
    def find_peice(self,pos):
        for i in range(7):
            if pos == self.black_pieces[i].get_position():
                return (str(i) + 'bP')
            elif pos == self.white_pieces[i].get_position():
                return (str(i) + 'wP')
            elif pos == self.black_pawns[i].get_position():
                return (str(i) + 'bp')
            elif pos == self.white_pawns[i].get_position():
                return (str(i) + 'wp')
                
                
        
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
        x = mouse_pos[0]//SQ_WIDTH
        y = mouse_pos[1]//SQ_HEIGHT
        
        return (x,y)
        
        
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
        piece_reference = self.board.find_peice(self.button_array.get_input_pos()[0])
        print(self.button_array.get_input_pos())
        # TODO: Check for peice with same pos
        
    
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
    
    
    
