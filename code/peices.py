import pygame

class peice():
    def __init__(self):
        self.first_move: bool = True
        self.is_white: bool 
        self.position: tuple = self.get_position()
        
    
    def get_position(self):
        return 
    
     
    def peice_captured(self):
        pass
    
    
    def move_peice(self,move):
        if move in self.get_moves():
            pass
        else:
            pass
    
    
class Rook(peice):
    def __init__(self,id):
        super().__init__()
        self.is_white = True if id[0] == 'w' else False
            
    
    def get_moves(self):
        possible_moves = []
        # up,right,down,left
        for i in range(4):
            for j in range(7):
                pass
        return possible_moves
            
            
class Bishop(peice,id):
    def __init__(self,color):
        super().__init__()
        self.is_white = color
    
    def get_moves(self):
        # Vectors inside array
        return []
            
            
class Knight(peice,id):
    def __init__(self,color):
        super().__init__()
        self.is_white = color
    
    def get_moves(self):
        # Vectors inside array
        return []
            
            
class Queen(peice,id):
    def __init__(self,color):
        super().__init__()
        self.is_white = color
    
    def get_moves(self):
        # Vectors inside array
        return []
            
            
class King(peice,id):
    def __init__(self,color):
        super().__init__()
        self.is_white = color
    
    def get_moves(self):
        # Vectors inside array
        return []
            
            
class Pawn (peice,id):
    def __init__(self,color):
        super().__init__()
        self.is_white = color
    
    def get_moves(self):
        # Vectors inside array
        return []
            
            

    
def load_images(images,SQ_HEIGHT,SQ_WIDTH):
    peices = ["bR", "bN", "bB", "bQ", "bK", "wQ", "wK", "wB", "wN", "wR", "bp", "wp"]   
    peice_names = ['R','N','B','Q','K','q','k','b','n','r','P','p']
    for i in range(len(peices)):
        images[peice_names[i]] = pygame.transform.scale(pygame.image.load("img/" + peices[i] + ".png"), (SQ_WIDTH, SQ_HEIGHT))


def draw_init(screen,menu,game_select,game_state,DIMENSION,images,SQ_HEIGHT,SQ_WIDTH):
    if menu == True:
        draw_board(screen,DIMENSION,SQ_HEIGHT,SQ_WIDTH)
        game_select.display_menu(screen)
    else:
        draw_board(screen,DIMENSION,SQ_HEIGHT,SQ_WIDTH)
        draw_peices(screen,game_state,DIMENSION,images,SQ_HEIGHT,SQ_WIDTH)
    

def draw_peices(screen,game_state,DIMENSION,images,SQ_HEIGHT,SQ_WIDTH):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = game_state.board[row][col]
            if piece != '-':
                screen.blit(images[piece], pygame.Rect(col*SQ_WIDTH, row*SQ_HEIGHT, SQ_WIDTH, SQ_HEIGHT))
                
                
def draw_board(screen,DIMENSION,SQ_HEIGHT,SQ_WIDTH):
    colors = [pygame.Color('#DDC9B4'),pygame.Color('#AA815D')]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(col*SQ_WIDTH, row*SQ_HEIGHT, SQ_WIDTH, SQ_HEIGHT))  