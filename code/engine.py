import fen_parser
from peices import *

class gameState():
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
        
        self.peice_board = [
            [Rook('br1'),Knight('bn1'),Bishop('bb1'),Queen('bq1'),King('bk1'),Bishop('bb2'),Knight('bn2'),Rook('br2')],
            [Pawn('bp1'),Pawn('bp2'),Pawn('bp3'),Pawn('bp4'),Pawn('bp5'),Pawn('bp6'),Pawn('bp7'),Pawn('bp8')],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            [Pawn('wp1'),Pawn('wp2'),Pawn('wp3'),Pawn('wp4'),Pawn('wp5'),Pawn('wp6'),Pawn('wp7'),Pawn('wp8')],
            [Rook('wr1'),Knight('wn1'),Bishop('wb1'),Queen('wq1'),King('wk1'),Bishop('wb2'),Knight('wn2'),Rook('wr2')]
        ]
        
        self.fen_position: str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        
        self.white_to_move = True
        self.enpassant_pos: tuple 
        self.castling: str
        
                  
    def decode_fen(self):
        fen_to_position = fen_parser.FenToChessPosition(self.fen_position)
        self.fen_position = fen_to_position.parse()
        return self.fen_position
        
        
    def encode_fen(self):
        position_to_fen = fen_parser.ChessPositionToFEN(self.board,self.white_to_move,self.enpassant_pos,self.castling)
        self.fen_position = position_to_fen.board_to_fen()
        return self.fen_position
    
    def get_peice_position(self,id):
        for row in range(8):
            for col in range(8):
                if self.peice_board[row][col].get_id() == id:
                    return (col,row)
                
        return None
    
    
    def test(self):
        print(self.peice_board[0][7].get_position)
        
game_state = gameState()