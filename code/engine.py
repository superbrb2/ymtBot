import fen_parser
from peices import *

class Board():
    def __init__(self):
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

class gameState():         
    def __init__(self):
        self.board = Board()
        self.fen_position: str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        
        self.white_to_move = True
        self.enpassant_pos: tuple 
        self.castling: str
    
    def decode_fen(self):
        fen_to_position = fen_parser.FenToChessPosition(self.fen_position)
        return fen_to_position.parse()
        
        
    def encode_fen(self):
        position_to_fen = fen_parser.ChessPositionToFEN(self.board.image_board)
        self.fen_position = position_to_fen.board_to_fen()
        return self.fen_position
                
        return None
    
    def get_image_board(self):
        return self.board.image_board
    
    
    
