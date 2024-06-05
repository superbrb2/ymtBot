import pygame
import engine
from images import draw_game



def begin(screen,images,game_state,event):
  
    if event.type == pygame.MOUSEBUTTONDOWN:
        game_state.button_press()
        
    draw_game(screen,images,game_state.board.image_board)
    