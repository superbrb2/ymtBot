import pygame
import selectscreen
import two_player
import AIengine
import engine

from images import *

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
screen.fill((221, 201, 180))
pygame.display.set_caption('Chess')


game_select = selectscreen.gameSelect(screen)
game_state = engine.gameState()


load_images(images)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and menu == False:
            game_state.button_press()
        
        # Checks for menu button press
        if event.type == pygame.MOUSEBUTTONDOWN and menu == True:
            if game_select.button_pressed() == '2P':
                menu = False
                two_player.begin()
                
            if game_select.button_pressed() == 'AI':
                menu = False
                AIengine.begin()
    draw_init(screen,menu,game_select,images,game_state.board.image_board)
    
    clock.tick(60)
    pygame.display.flip()
            
                    
pygame.quit()