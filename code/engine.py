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
        
    def decode_fen(self,fen):
        fp = fen_parser.FenParser(fen)
        print(fp.parse())
    
    def encode_fen(self):
        pass