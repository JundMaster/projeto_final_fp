import pygame
from Card_class import *
from game_mode import level1
from colors import *

pygame.init()

display_width = 1440
display_height = 900


gameDisplay = pygame.display.set_mode([display_width, display_height])
gameDisplay.fill(background_color)

clock = pygame.time.Clock()

def game_menu():
    done = False
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # width, height, x, y, color, surface, stroke
        menu_gm1 = Card(display_width/10, display_height/20, display_width/2 - (display_width/10)/2 , display_height/2 + (display_height/20)/2, yellow, gameDisplay, 2)
        menu_gm2 = Card(display_width/10, display_height/20, display_width/2 - (display_width/10)/2 , display_height/2 + menu_gm1.height*2, yellow, gameDisplay, 2)
        text1 = OptionText(menu_gm1.width, menu_gm1.height, menu_gm1.x, menu_gm1.y, white, gameDisplay, 2)

        menu_gm1.draw_card()
        menu_gm2.draw_card()
        text1.draw_text("text", text1.x, text1.y)

        if menu_gm1.button() == 1:
            gameDisplay.fill(background_color)
            level1()
            gameDisplay.fill(background_color)
            

        pygame.display.update()
        clock.tick(60)

game_menu()