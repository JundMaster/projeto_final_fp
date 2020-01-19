import pygame
from Card_class import *
from game_mode import level1
from colors import *

pygame.init()

display_width = 1220
display_height = 700


gameDisplay = pygame.display.set_mode([display_width, display_height])
gameDisplay.fill(background_color)

clock = pygame.time.Clock()

def game_menu():
    done = False
    while not done:
        # width, height, x, y, color, surface, stroke
        menu_gm1 = Card(display_width/10, display_height/20, display_width/2 - (display_width/10)/2 , display_height/2 + (display_height/20)/2, yellow)
        menu_gm2 = Card(display_width/10, display_height/20, display_width/2 - (display_width/10)/2 , display_height/2 + menu_gm1.height*2, yellow)
        text1 = OptionText(menu_gm1.width, menu_gm1.height, menu_gm1.x, menu_gm1.y, white)
        mouse = pygame.mouse.get_pos()

        # print("mouse: ", str(mouse[0]), ", ", str(mouse[1]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if menu_gm1.collision(mouse) == False:
            menu_gm1.draw_card(yellow, 2)
        else:
            menu_gm1.draw_card(white, 2)

        menu_gm2.draw_card(yellow, 2)
        text1.draw_text("text", text1.x, text1.y)

        if menu_gm1.button(mouse) == 1:
            gameDisplay.fill(background_color)
            level1()
            gameDisplay.fill(background_color)
            

        pygame.display.update()
        clock.tick(60)

game_menu()