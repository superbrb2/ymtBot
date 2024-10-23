from operator import xor

HEIGHT = 700
WIDTH = 700

DIMENSION = 8
SQ_HEIGHT = HEIGHT / DIMENSION
SQ_WIDTH = WIDTH / DIMENSION

class piece():
    def __init__(self,id,pos):
        self.first_move: bool = True
        self.position: tuple = pos
        self.id: str = id
        self.is_white: bool = True if self.id[0] == 'w'  else False
        print(self.is_white,id)
        
    def update_position(self,pos):
        self.position = pos
        
    def update_first_move(self):
        if self.first_move:
            self.first_move = False
    
    def get_position(self):
        return self.position
    
    # Gets overided in child classes
    def get_moves(self,board):
        return None
    
    def get_colour(self):
        return self.is_white
    
    def get_id(self):
        return self.id
    
    
    
    
class Rook(piece):
    def __init__(self,id,pos):
        super().__init__(id,pos)
            
    
    def get_moves(self,board):
        possible_moves = []
        # Casting to make co-ords muttable
        list_pos = list(self.position)
        
        #right,up,left,down
        for i in [1,-1]:
            hit_piece = False
            for row in range(8):
                move_pos = [list_pos[0], list_pos[1] + (i*row)]
                if move_pos == list_pos:
                    continue
                if move_pos[1] > 7 or move_pos[1] < 0 or hit_piece:
                    break
                else:
                    if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                        hit_piece = True
                    elif board[int(move_pos[0])][int(move_pos[1])] != '-':
                        possible_moves.append(tuple(move_pos))
                        hit_piece = True
                    else:
                        possible_moves.append(tuple(move_pos))
            
            hit_piece = False     
            for col in range(7):
                move_pos = [list_pos[0] + (i*col), list_pos[1]]
                if move_pos == list_pos:
                    continue
                if move_pos[0] > 7 or move_pos[0] < 0 or hit_piece:
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
            
            
class Bishop(piece):
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
            
            
class Knight(piece):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        
    
    def get_moves(self,board):
        possible_moves = []
        # Casting to make co-ords muttable
        list_pos = list(self.position)
        
        for i in [[1,1],[-1,1],[-1,-1],[1,-1]]:
            for j in [[1,2],[2,1]]:
                move_pos = [list_pos[0] + (i[0]*j[0]),list_pos[1] + (i[1]*j[1])]
                
                if move_pos[0] > 7 or move_pos[0] < 0 or move_pos[1] > 7 or move_pos[1] < 0:
                    continue
                print(self.is_white,board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK',move_pos)
                
                if (board[int(move_pos[0])][int(move_pos[1])] == '-'):
                    possible_moves.append(tuple(move_pos))
                    
                if self.is_white != (board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                    possible_moves.append(tuple(move_pos))
        print(possible_moves)
        return possible_moves
            
            
class Queen(piece):
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
            hit_piece = False
            for row in range(7):
                move_pos = [list_pos[0], list_pos[1] + (i*row)]
                if move_pos == list_pos:
                    continue
                if move_pos[1] > 7 or move_pos[1] < 0 or hit_piece:
                    break
                else:
                    if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                        hit_piece = True
                    elif board[int(move_pos[0])][int(move_pos[1])] != '-':
                        possible_moves.append(tuple(move_pos))
                        hit_piece = True
                    else:
                        possible_moves.append(tuple(move_pos))
            
            hit_piece = False
            for col in range(7):                    
                move_pos = [list_pos[0] + (i*col), list_pos[1]]
                if move_pos == list_pos:
                    continue
                if move_pos[0] > 7 or move_pos[0] < 0 or hit_piece:
                    break
                else:
                    print('bq, db', board[int(move_pos[0])][int(move_pos[1])] != '-', (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'),move_pos)
                    if board[int(move_pos[0])][int(move_pos[1])] != '-' and (self.is_white != board[int(move_pos[0])][int(move_pos[1])] in 'PRNBQK'):
                        hit_piece = True
                    elif board[int(move_pos[0])][int(move_pos[1])] != '-':
                        possible_moves.append(tuple(move_pos))
                        hit_piece = True
                    else:
                        possible_moves.append(tuple(move_pos))
                        
        return possible_moves
        '''
        arr = []
        for i in possible_moves:
            if self.is_white != (board[i[0]][i[1]] in list('KQRBKP')):
                arr.append(i)
        return arr
        '''
            
            
class King(piece):
    def __init__(self,id,pos):
        super().__init__(id,pos)
        self.K_castle = True
        self.Q_castle = True
    
    def update_K_castling(self):
        self.K_castle = False
        
    def update_Q_castling(self):
        self.Q_castle = False
    
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
                    
        # Castling
        # TODO castling
        if self.is_white:
            if self.first_move and board[7][6] == '-' and board[7][5] == '-' and self.K_castle:
                pass
            if self.first_move and board[0][6] == '-' and board[0][5] == '-' and self.K_castle:
                pass
        return possible_moves
        
            
            
class Pawn(piece):
    def __init__(self,id,pos):
        super().__init__(id,pos)

    
    def get_moves(self,board):
        # TODO: Promotion
        possible_moves = []
        
        list_pos = list(self.position)
        
        if self.is_white:
            if self.first_move:
                for i in range(2):
                    move_pos = [int(list_pos[0]-(i+1)),int(list_pos[1])]
                    if board[move_pos[0]][move_pos[1]] == '-':
                        possible_moves.append(tuple(move_pos))
                    else:
                        break
            else:
                move_pos = [int(list_pos[0]-1),int(list_pos[1])]
                if board[move_pos[0]][move_pos[1]] == '-':
                    possible_moves.append(tuple(move_pos))
                    
            for i in [-1,1]:
                move_pos = [int(list_pos[0]-1),int(list_pos[1]+i)]
                try:
                    if board[move_pos[0]][move_pos[1]] != '-' and (self.is_white ^ bool(board[move_pos[0]][move_pos[1]] in 'PRNBQK')):
                        possible_moves.append(tuple(move_pos))
                except IndexError as err:
                    print(err)
                    

        else:
            if self.first_move:
                for i in range(2):
                    move_pos = [int(list_pos[0]+(i+1)),int(list_pos[1])]
                    if board[move_pos[0]][move_pos[1]] == '-':
                        possible_moves.append(tuple(move_pos))
                    else:
                        break
            
            else:
                move_pos = [int(list_pos[0]+1),int(list_pos[1])]
                if board[move_pos[0]][move_pos[1]] == '-':
                    possible_moves.append(tuple(move_pos))
                    
            for i in [-1,1]:
                move_pos = [int(list_pos[0]+1),int(list_pos[1]+i)]
                try:
                    if board[move_pos[0]][move_pos[1]] != '-' and (self.is_white ^ bool(board[move_pos[0]][move_pos[1]] in 'PRNBQK')):
                        possible_moves.append(tuple(move_pos))
                except IndexError as err:
                    print(err)
                    
        return possible_moves
    