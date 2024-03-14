import pygame

HEIGHT = 700
WIDTH = 700

DIMENSION = 8
SQ_HEIGHT = HEIGHT / DIMENSION
SQ_WIDTH = WIDTH / DIMENSION

class peice():
    def __init__(self,id,pos):
        self.first_move: bool = True
        self.position: tuple = pos
        self.id: str = id
        self.is_white: bool = True if self.id in 'PRNBQK'  else False
        
    def update_position(self,pos):
        self.position = pos
    
    def get_position(self):
        return self.position
    
    # Gets overided in child classes
    def get_moves(self):
        return None

    
    
class Rook(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        self.is_white = True if id[0] == 'w' else False
            
    
    def get_moves(self):
        possible_moves = []
        # up,right,down,left
        for row in range(7):
            pass
        for col in range(7):
            pass
        return possible_moves
            
            
class Bishop(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        
    
    def get_moves(self):
        # Vectors inside array
        return []
            
            
class Knight(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        
    
    def get_moves(self):
        # Vectors inside array
        return []
            
            
class Queen(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        
    
    def get_moves(self):
        # Vectors inside array
        return []
            
            
class King(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        
    
    def get_moves(self):
        # Vectors inside array
        return []
            
            
class Pawn(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)

    
    def get_moves(self):
        # Vectors inside array
        return []
            
            
