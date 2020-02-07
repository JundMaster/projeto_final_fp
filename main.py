import pygame
import inspect
from Card_class import *
from game_mode import in_game
from colors import *
from functions import get_gm_list, lineno

pygame.init()
display_width = 1220
display_height = 700
gameDisplay = pygame.display.set_mode([display_width, display_height])
gameDisplay.fill(background_color)
clock = pygame.time.Clock()
collision_list = []

shuffle_image = pygame.image.load('shuffle.png')
image_width = shuffle_image.get_width()
image_height = shuffle_image.get_height()
# collision_sound = pygame.mixer.Sound('collision.wav')

def game_menu():
    temp_list = []
    number = []
    done = False
    while not done:

        # setting the dimensions and position of the buttons
        button_width = display_width/10
        button_height = display_height/20
        button_x = display_width/2 - (display_width/10)/2
        button_y = display_height/2 + (display_height/20)/6 # location of the first button on Y axis
        # sets the distance between the buttons except for the last one, the 'EXIT' button
        dist_modifier = 1.2

        gameDisplay.blit(shuffle_image, (display_width/2 - image_width/2, button_y - image_height))
        
        # list with each button text
        game_mode = ['4 x 3', '4 x 4', '5 x 4', '6 x 5', '6 x 6','Exit']
        gm_list = get_gm_list(game_mode)
        # print(gm_list)
        # empty list that will contain each button with it respective text
        button_set = []
        # the loop appends the buttons to the button_set ss
        for i in range (0, len(game_mode)):
            # creates the first button
            if i == 0:
                button_set.append(Button(button_width, button_height, button_x, button_y, game_mode[0]))
            # creates the rest of the buttons, except for the last one
            elif i > 0 and i < len(game_mode) - 1:
                button_set.append(Button(button_width, button_height, button_x, button_set[i - 1].y + button_set[i - 1].height*dist_modifier , game_mode[i]))
           
            # creates the 'EXIT' button, wich is the last one, only if the button text contains 'exit' writen in any way
            elif i == len(game_mode) - 1 and (game_mode[i].replace(" ", "")).lower() == 'exit':
                button_set.append(Button(button_width, button_height, button_x, button_set[i - 1].y + button_set[i - 1].height*dist_modifier*1.5 , game_mode[i]))

            # if the last button doen't contain 'exit' in it, a regular game mode button will be created
            else:
                button_set.append(Button(button_width, button_height, button_x, button_set[i - 1].y + button_set[i - 1].height*dist_modifier , game_mode[i]))
              
            if button_set[i].y + button_set[i].height>= display_height:
                print("-"*30 + " E R R O R " + "-"*30 + "\nThe amount of buttons exceeds the display height")
                print("Try either repositioning the button set or creating less buttons\n" + "-"*72)
                exit()
        # gets the position of the mouse
        mouse = pygame.mouse.get_pos()
        # gets the MB1 (mouse left button)click
        click = pygame.mouse.get_pressed()[0]

        # checks the exit conditions for the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True       
            # Draw the whole button set (text included)
            
            for button in button_set:
                if button.collision(mouse) == True:
                    button_color = white
                    collision_list.append(button)
                else:
                    button_color = yellow
                # draws button text based on the game_mode list elements    
                button.draw_text(button_color)
                button.draw_button(button_color, 2)
                
        # check which button was clicked and goed to the corresponding game level
        gm_len = len(game_mode)

        for i in range (0, gm_len):
            if button_set[i].button(mouse) == True:
                if event.type == pygame.MOUSEBUTTONUP:
                    if (game_mode[i].replace(" ", "")).lower() == 'exit' :
                        exit()

                    else:
                        try:
                            line = lineno() + 1
                            in_game(gm_list[i][0], gm_list[i][1])
                        except:
                            print("-"*30," E R R O R " + "-"*30 )
                            print(f'File "main.py", line {line}')
                            # print("'" + str(game_mode[i]) + "' is not a valid game mode.\n")
                            print(f"'{game_mode[i]}' is not a valid game mode.\n")
                            print("Try creating a game mode with the format '4 x 3'.")
                            print("The game mode you add to the list MUST be a string.")
                            print("-"*72)
                            pygame.quit()
                            exit()
                    gameDisplay.fill(background_color)

        pygame.display.update()
        clock.tick(60)

game_menu()