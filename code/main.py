import pygame
import engine
import selectscreen
import two_player
import AIengine

HEIGHT = 700
WIDTH = 700
DIMENSION = 8
SQ_HEIGHT = HEIGHT / DIMENSION
SQ_WIDTH = WIDTH / DIMENSION
menu = True
images = {}

pygame.init()


screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
screen.fill(pygame.Color('white'))
pygame.display.set_caption('Chess')

# https://www.chess.com/terms/fen-chess#:~:text=It%20starts%20describing%20the%20content,and%20go%20to%20the%20eighth.
fen_position = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1' # Splice string into an array and parse for each row

game_state = engine.gameState()
game_select = selectscreen.gameSelect(screen,WIDTH,HEIGHT)


def load_images():
    peices = ["bR", "bN", "bB", "bQ", "bK", "wQ", "wK", "wB", "wN", "wR", "bp", "wp"]   
    for peice in peices:
        images[peice] = pygame.transform.scale(pygame.image.load("img/" + peice + ".png"), (SQ_WIDTH, SQ_HEIGHT))

def draw_init(screen,game_state):
    if menu == True:
        draw_board(screen)
        game_select.display_menu(screen)
    else:
        draw_board(screen)
        draw_peices(screen,game_state)
    

def draw_peices(screen,game_state):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = game_state.board[row][col]
            if piece != '--':
                screen.blit(images[piece], pygame.Rect(col*SQ_WIDTH, row*SQ_HEIGHT, SQ_WIDTH, SQ_HEIGHT))
                
                
def draw_board(screen):
    colors = [pygame.Color('#DDC9B4'),pygame.Color('#AA815D')]
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            color = colors[((row + col) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(col*SQ_WIDTH, row*SQ_HEIGHT, SQ_WIDTH, SQ_HEIGHT))  



load_images()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Checks for menu button press
        if event.type == pygame.MOUSEBUTTONDOWN and menu == True:
            if game_select.button_pressed() == '2P':
                menu = False
                two_player.begin()
                
            if game_select.button_pressed() == 'AI':
                menu = False
                AIengine.begin()
                 
    draw_init(screen,game_state)
    
    clock.tick(60)
    pygame.display.flip()
            
                    
pygame.quit()