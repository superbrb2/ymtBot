import fen_parser

class gameState():
    def __init__(self):
        self.board = [
            ['r','n','b','q','k','b','n','r'],
            ['p','p','p','p','p','p','p','p'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['-','-','-','-','-','-','-','-'],
            ['P','P','P','P','P','P','P','P'],
            ['R','N','B','Q','K','B','N','R']    
        ]
        
        self.white_to_move = True
        self.enpassant_pos: tuple 
        self.castling: str
        
        
                
    def decode_fen(self,fen):
        fen_to_position = fen_parser.FenToChessPosition(fen)
        print(fen_to_position.parse())
    
    def encode_fen(self):
        position_to_fen = fen_parser.ChessPositionToFEN(self.board,self.white_to_move,self.enpassant_pos,self.castling)
        print(position_to_fen.board_to_fen())