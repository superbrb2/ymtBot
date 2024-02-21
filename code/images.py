import pygame

def load_images(images,SQ_HEIGHT,SQ_WIDTH):
    peices = ["bR", "bN", "bB", "bQ", "bK", "wQ", "wK", "wB", "wN", "wR", "bp", "wp"]   
    peice_names = ['R','N','B','Q','K','q','k','b','n','r','P','p']
    for i in range(len(peices)):
        images[peice_names[i]] = pygame.transform.scale(pygame.image.load("img/" + peices[i] + ".png"), (SQ_WIDTH, SQ_HEIGHT))


def draw_init(screen,menu,game_select,DIMENSION,images,SQ_HEIGHT,SQ_WIDTH,image_board):
    if menu == True:
        draw_board(screen,DIMENSION,SQ_HEIGHT,SQ_WIDTH)
        game_select.display_menu(screen)
    else:
        draw_board(screen,DIMENSION,SQ_HEIGHT,SQ_WIDTH)
        draw_peices(screen,DIMENSION,images,SQ_HEIGHT,SQ_WIDTH,image_board)
    

def draw_peices(screen,DIMENSION,images,SQ_HEIGHT,SQ_WIDTH,image_board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = image_board[row][col]
            if piece != '-':
                screen.blit(images[piece], pygame.Rect(col*SQ_WIDTH, row*SQ_HEIGHT, SQ_WIDTH, SQ_HEIGHT))
                
                
def draw_board(screen,DIMENSION,SQ_HEIGHT,SQ_WIDTH):
    colors = [pygame.Color('#DDC9B4'),pygame.Color('#AA815D')]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(col*SQ_WIDTH, row*SQ_HEIGHT, SQ_WIDTH, SQ_HEIGHT))  