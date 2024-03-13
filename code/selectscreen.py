import pygame

HEIGHT = 700
WIDTH = 700

DIMENSION = 8
SQ_HEIGHT = HEIGHT / DIMENSION
SQ_WIDTH = WIDTH / DIMENSION

class gameSelect():
    def __init__(self,screen):
        self.option_list = ['2P','AI']
        self.screen = screen
        
        
    def display_menu(self,screen):
        locations = [HEIGHT*0.45,(HEIGHT*5)/7]
        menu_options = ['Player Vs Player','Player Vs Computer']
        font = pygame.font.SysFont('Ariel',75)
        for i in range(2):
            box_rect = pygame.Rect(WIDTH/14,locations[i],(WIDTH*6)/7, HEIGHT/7)
            pygame.draw.rect(screen,'#F7C59F',box_rect)
            self.screen.blit(font.render(menu_options[i],True,(255,255,255)),(round(WIDTH/14)+25,round(locations[i])+25))

        
    def button_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        # First Button position
        if WIDTH/14 <= mouse_pos[0] <= (WIDTH/14)+((WIDTH*6)/7) and HEIGHT*0.45 <= mouse_pos[1] <= (HEIGHT*0.45)+(HEIGHT/7):
            return self.option_list[0]
        # Second Button position
        if WIDTH/14 <= mouse_pos[0] <= (WIDTH/14)+((WIDTH*6)/7) and (HEIGHT*5)/7 <= mouse_pos[1] <= ((HEIGHT*5)/7)+(HEIGHT/7):
            return self.option_list[1]