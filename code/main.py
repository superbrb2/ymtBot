import pygame
import selectscreen
import two_player
import AIengine
import engine

from images import *

HEIGHT = 704
WIDTH = 704

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
        
        # Checks for menu button press
        if event.type == pygame.MOUSEBUTTONDOWN and menu == True:   
            game_mode = game_select.button_pressed()
            if game_mode != None:
                menu = False
                
        if menu == False:
            if game_mode == '2P':
                two_player.begin(screen,images,game_state,event)
            else:
                AIengine.begin(screen,images,game_state,event)
                    
        else:
            draw_menu(screen,game_select)
    
    clock.tick(30)
    pygame.display.flip()
            
                    
pygame.quit()