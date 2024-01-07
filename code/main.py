import pygame
from drawing import *

HEIGHT = 800
WIDTH = 800
DIMENSION = 8
SQ_HEIGHT = HEIGHT / DIMENSION
SQ_WIDTH = WIDTH / DIMENSION

pygame.init()


screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
screen.fill(pygame.Color('white'))
pygame.display.set_caption('Chess')


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_board(screen,SQ_WIDTH,SQ_HEIGHT,DIMENSION)
    
    clock.tick(60)
    pygame.display.flip()
            
                    
pygame.quit()