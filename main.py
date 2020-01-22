import pygame
from Card_class import *
from game_mode import in_game
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
        # setting the dimensions and position of the buttons
        button_width = display_width/10
        button_height = display_height/20
        button_x = display_width/2 - (display_width/10)/2
        button_y = display_height/2 + (display_height/20)/6 # location of the first button on Y axis
        # sets the distance between the buttons except for the last one, the 'EXIT' button

        dist_modifier = 1.2
        
        # list with each button text
        game_mode = ['4 x 3', '4 x 4', '5 x 4', '6 x 4', '6 x 5', '6 x 6','EXIT']
        # empty list that will contain each button with it respective text
        button_set = []
        # the loop appends the buttons to the button_set 
        for i in range (0, len(game_mode)):
            # creates the first button
            if i == 0:
                button_set.append(Card(button_width, button_height, button_x, button_y, game_mode[0]))
            # creates the rest of the buttons, except for the last one
            elif i > 0 and i < len(game_mode) - 1:
                button_set.append(Card(button_width, button_height, button_x, button_set[i - 1].y + button_set[i - 1].height*dist_modifier , game_mode[i]))
           
            # creates the 'EXIT' button, wich is the last one, only if the button text contains 'exit' writen in any way
            elif i == len(game_mode) - 1 and (game_mode[i].replace(" ", "")).lower() == 'exit':
                button_set.append(Card(button_width, button_height, button_x, button_set[i - 1].y + button_set[i - 1].height*dist_modifier*1.5 , game_mode[i]))

            # if the last button doen't contain 'exit' in it, a regular game mode button will be created
            else:
                button_set.append(Card(button_width, button_height, button_x, button_set[i - 1].y + button_set[i - 1].height*dist_modifier , game_mode[i]))
              
            if button_set[i].y + button_set[i].height>= display_height:
                print("------------------------------ E R R O R ------------------------------\nThe ammout of buttons excedes the display height")
                print("Try either repositioning the button set or creating less buttons\n-----------------------------------------------------------------------")
                pygame.quit()
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
                else:
                    button_color = yellow
                # draws button text based on the game_mode list elements    
                button.draw_text(button_color)
                button.draw_card(button_color, 2)

        # check which button was clicked and goed to the corresponding game level
        gm_len = len(game_mode)
        for i in range (0, gm_len):
            if button_set[i].button(mouse) == 1:
                if (game_mode[i].replace(" ", "")).lower() == 'exit' :
                    # print("'",str(game_mode[i][0]),"'",' or ',"'",str(game_mode[i][-1]),"'",' is not a valid game mode paramater.')
                    # print(game_mode[i])
                    pygame.quit()
                    exit()
                elif game_mode[i][0].isdigit() and game_mode[i][-1].isdigit():
                    in_game(int(game_mode[i][0]),int(game_mode[i][-1]))
                else:
                    print("------------------------------ E R R O R ------------------------------")
                    print("'",str(game_mode[i]),"' is not a valid game mode.")
                    print("-----------------------------------------------------------------------")
                    pygame.quit()
                    exit()
                gameDisplay.fill(background_color)

        pygame.display.update()
        clock.tick(60)

game_menu()