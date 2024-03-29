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
        self.is_white: bool = True if self.id[0] == 'w'  else False
        
    def update_position(self,pos):
        self.position = pos
    
    def get_position(self):
        return self.position
    
    # Gets overided in child classes
    def get_moves(self,board):
        return None
    
    def get_colour(self):
        return self.is_white
    
    def get_id(self):
        return self.id
    
    
class Rook(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)
            
    
    def get_moves(self,board):
        possible_moves = []
        # Casting to make co-ords muttable
        list_pos = list(self.position)
        
        #right,up,left,down
        for i in [1,-1]:
            hit_peice = False
            for row in range(8):
                move_pos = [list_pos[0], list_pos[1] + (i*row)]
                if move_pos == list_pos:
                    continue
                if move_pos[1] > 7 or move_pos[1] < 0 or hit_peice:
                    break
                else:
                    if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                        hit_peice = True
                    elif board[int(move_pos[0])][int(move_pos[1])] != '-':
                        possible_moves.append(tuple(move_pos))
                        hit_peice = True
                    else:
                        possible_moves.append(tuple(move_pos))
                        
            for col in range(7):
                move_pos = [list_pos[0] + (i*col), list_pos[1]]
                if move_pos == list_pos:
                    continue
                if move_pos[0] > 7 or move_pos[0] < 0 or hit_peice:
                    break
                else:
                    if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                        hit_peice = True
                    elif board[int(move_pos[0])][int(move_pos[1])] != '-':
                        possible_moves.append(tuple(move_pos))
                        hit_peice = True
                    else:
                        possible_moves.append(tuple(move_pos))
        return possible_moves
            
            
class Bishop(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        
    
    def get_moves(self,board):
        possible_moves = []
        # Casting to make co-ords muttable
        list_pos = list(self.position)
        # NE,SE,SW,NW
        for i in [1,-1]:
            for j in [1,-1]:
                hit_piece = False
                for k in range(8):
                    move_pos = [list_pos[0] + (i*k), list_pos[1] + (j*k)]
                    if move_pos == list_pos:
                        continue
                    if move_pos[0] > 7 or move_pos[0] < 0 or move_pos[1] > 7 or move_pos[1] < 0 or hit_piece:
                        break
                    else:
                        if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                            hit_piece = True
                        elif board[int(move_pos[0])][int(move_pos[1])] != '-':
                            possible_moves.append(tuple(move_pos))
                            hit_piece = True
                        else:
                            possible_moves.append(tuple(move_pos))
                            
        return possible_moves
            
            
class Knight(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        
    
    def get_moves(self,board):
        possible_moves = []
        # Casting to make co-ords muttable
        list_pos = list(self.position)
        
        for i in [[1,1],[-1,1],[-1,-1],[1,-1]]:
            for j in [[1,2],[2,1]]:
                hit_piece = False
                move_pos = [list_pos[0] + (i[0]*j[0]),list_pos[1] + (i[1]*j[1])]
                
                if move_pos == list_pos:
                    continue
                if move_pos[0] > 7 or move_pos[0] < 0 or move_pos[1] > 7 or move_pos[1] < 0 or hit_piece:
                    continue
                else:
                    if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                        hit_piece = True
                    elif board[int(move_pos[0])][int(move_pos[1])] != '-':
                        possible_moves.append(tuple(move_pos))
                        hit_piece = True
                    else:
                        possible_moves.append(tuple(move_pos))
        return possible_moves
            
            
class Queen(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        
    
    def get_moves(self,board):
        possible_moves = []
        # Casting to make co-ords muttable
        list_pos = list(self.position)
        # NE,SE,SW,NW
        for i in [1,-1]:
            for j in [1,-1]:
                hit_piece = False
                for k in range(8):
                    move_pos = [list_pos[0] + (i*k), list_pos[1] + (j*k)]
                    if move_pos == list_pos:
                        continue
                    if move_pos[0] > 7 or move_pos[0] < 0 or move_pos[1] > 7 or move_pos[1] < 0 or hit_piece:
                        break
                    else:
                        if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                            hit_piece = True
                        elif board[int(move_pos[0])][int(move_pos[1])] != '-':
                            possible_moves.append(tuple(move_pos))
                            hit_piece = True
                        else:
                            possible_moves.append(tuple(move_pos))
        
        #right,up,left,down           
        for i in [1,-1]:
            hit_peice = False
            for row in range(8):
                move_pos = [list_pos[0], list_pos[1] + (i*row)]
                if move_pos == list_pos:
                    continue
                if move_pos[1] > 7 or move_pos[1] < 0 or hit_peice:
                    break
                else:
                    if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                        hit_peice = True
                    elif board[int(move_pos[0])][int(move_pos[1])] != '-':
                        possible_moves.append(tuple(move_pos))
                        hit_peice = True
                    else:
                        possible_moves.append(tuple(move_pos))
                        
            for col in range(7):
                move_pos = [list_pos[0] + (i*col), list_pos[1]]
                if move_pos == list_pos:
                    continue
                if move_pos[0] > 7 or move_pos[0] < 0 or hit_peice:
                    break
                else:
                    if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                        hit_peice = True
                    elif board[int(move_pos[0])][int(move_pos[1])] != '-':
                        possible_moves.append(tuple(move_pos))
                        hit_peice = True
                    else:
                        possible_moves.append(tuple(move_pos))
                            
        return possible_moves
            
            
class King(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        
    
    def get_moves(self,board):
        # TODO: Don't move into check!!!
        possible_moves = []
        
        list_pos = list(self.position)
        for i in [[1,1],[1,0],[1,-1],[-1,1],[-1,0],[-1,-1],[0,1],[0,-1]]:
            move_pos = [list_pos[0] + i[0],list_pos[1] + i[1]]
            hit_piece = False
            if move_pos[0] > 7 or move_pos[0] < 0 or move_pos[1] > 7 or move_pos[1] < 0 or hit_piece:
                continue
            else:
                if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                    hit_piece = True
                elif board[int(move_pos[0])][int(move_pos[1])] != '-':
                    possible_moves.append(tuple(move_pos))
                    hit_piece = True
                else:
                    possible_moves.append(tuple(move_pos))
        return possible_moves
        
            
            
class Pawn(peice):
    def __init__(self,id,pos):
        super().__init__(id,pos)

    
    def get_moves(self,board):
        # TODO: Promotion
        possible_moves = []
        
        list_pos = list(self.position)
        if self.is_white:
            if self.first_move:
                for i in range(2):
                    move_pos = [list_pos[0]-i,list_pos[1]]
                    if board[int(move_pos[0])][int(move_pos[1])] != '-':
                        break
                    else:
                        possible_moves.append(tuple(move_pos))
            
            else:
                move_pos = [list_pos[0] - 1,list_pos[1]]
                if board[int(move_pos[0])][int(move_pos[1])] == '-':
                    possible_moves.append(tuple(move_pos))
            
            for i in [[-1,-1],[-1,1]]:
                move_pos = [list_pos[0] + i[0], list_pos[1] + i[1]]
                if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                    possible_moves.append(move_pos)
        
        else:
            if self.first_move:
                for i in range(2):
                    move_pos = [list_pos[0]+i,list_pos[1]]
                    if board[int(move_pos[0])][int(move_pos[1])] != '-':
                        break
                    else:
                        possible_moves.append(tuple(move_pos))
            
            else:
                move_pos = [list_pos[0] + 1,list_pos[1]]
                if board[int(move_pos[0])][int(move_pos[1])] == '-':
                    possible_moves.append(tuple(move_pos))
            
            for i in [[1,-1],[1,1]]:
                move_pos = [list_pos[0] + i[0], list_pos[1] + i[1]]
                if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                    possible_moves.append(tuple(move_pos))  
                    
                
                            
        return possible_moves
            
            
