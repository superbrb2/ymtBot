import pygame

class gameSelect():
    def __init__(self,screen,WIDTH,HEIGHT):
        self.option_list = ['2P','AI']
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.screen = screen
        
        
    def display_menu(self,screen):
        locations = [self.HEIGHT*0.45,(self.HEIGHT*5)/7]
        for i in range(2):
            box_rect = pygame.Rect((self.WIDTH)/14,locations[i],(self.WIDTH*6)/7, self.HEIGHT/7)
            pygame.draw.rect(screen,'#F7C59F',box_rect)

        
    def hide_menu(self):
        pass
    
    def get_option(self):
        pass