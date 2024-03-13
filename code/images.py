import pygame

HEIGHT = 700
WIDTH = 700

DIMENSION = 8
SQ_HEIGHT = HEIGHT / DIMENSION
SQ_WIDTH = WIDTH / DIMENSION

def load_images(images):
    peices = ["bR", "bN", "bB", "bQ", "bK", "wQ", "wK", "wB", "wN", "wR", "bp", "wp"]   
    peice_names = ['R','N','B','Q','K','q','k','b','n','r','P','p']
    for i in range(len(peices)):
        images[peice_names[i]] = pygame.transform.scale(pygame.image.load("img/" + peices[i] + ".png"), (SQ_WIDTH, SQ_HEIGHT))


def draw_init(screen,menu,game_select,images,image_board):
    if menu == True:
        draw_board(screen)
        game_select.display_menu(screen)
    else:
        draw_board(screen)
        draw_peices(screen,images,image_board)
    

def draw_peices(screen,images,image_board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = image_board[row][col]
            if piece != '-':
                screen.blit(images[piece], pygame.Rect(col*SQ_WIDTH, row*SQ_HEIGHT, SQ_WIDTH, SQ_HEIGHT))
                
                
def draw_board(screen):
    colors = [pygame.Color('#DDC9B4'),pygame.Color('#AA815D')]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(col*SQ_WIDTH, row*SQ_HEIGHT, SQ_WIDTH, SQ_HEIGHT))  