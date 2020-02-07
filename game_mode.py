import pygame
from Card_class import *
from colors import *
from functions import display_text, card_check, save_score, get_score, lineno


pygame.mixer.pre_init(22050, -16, 2, 4096)
pygame.mixer.quit()
pygame.mixer.init()
flip_sound = pygame.mixer.Sound('flip.wav')
win_sound1 = pygame.mixer.Sound('win_sound1.wav')
win_sound2 = pygame.mixer.Sound('win_sound2.wav')
display_width = 1220
display_height = 700
gameDisplay = pygame.display.set_mode([display_width, display_height])

display_center_x = display_width - display_width/2
display_center_y = display_height - display_height/2


clock = pygame.time.Clock()

def in_game(cards_hor, cards_vert):
    gameDisplay.fill(background_color)
    done = False
    playable = True
    board_width = display_width - display_width/6
    board_height = display_height - display_height/6
    if cards_vert > cards_hor:
        card_width = (board_width/cards_vert) / 2.5
    else:
        card_width = (board_width/cards_hor) / 2.5
    card_dist = card_width/15
    card_height = card_width*1.5

    card_x = 0 
    card_y = 0

    button_width = display_width/10
    button_height = display_height/20
    button_x = card_dist
    button_y = display_height - button_height - card_dist

    timer_set = pygame.USEREVENT + 1
    pygame.time.set_timer(timer_set, 1000)
    

##############################################################
    card_x_1 = card_x                                       
    for i in range(cards_hor): # number of cards on the horizontal
        card_x_1 = card_x_1 + card_width + card_dist
        

    card_x_1 = card_x_1/2  

    card_center_x = display_center_x - card_x_1

    card_y_1 = card_y
    for i in range(cards_vert): # number of cards on the vertical
        card_y_1 = card_y_1 + card_height + card_dist
        

    card_y_1 = card_y_1/2  
    card_center_y = display_center_y - card_y_1
#############################################################


    shape_list = ['square', 'circle', 'triangle']
    shape_color = [cyan, red, blue, green, orange, pink, yellow, blue_green]
     
    score = 0
    possible = []
    for j in shape_color:
        for i in shape_list:
            possible.append((i,j))
 
    game_deck = []
    
    # checks if the list of possible cards has enough elements to create the given amount of cards
    # in case the list isn't long enough, print a error message with possible solutions 
    if (cards_vert * cards_hor)//2 > len(possible):
        print("-"*34, " E R R O R ", "-"*34 )
        print("The game board has too many cards.\nYou may try either creating new colors/shapes or reducing the ammout of cards.")
        print("-"*81)
        pygame.quit()
        exit()

    for i in range (0, (cards_vert * cards_hor)//2):
        game_deck.append(possible[i])
        game_deck.append(possible[i])

    random.shuffle(game_deck)
    y_card = card_center_y
    card_list = []
    num = 0
    """
    This double for loop creates the card list that will be used in the game.
    
    The first card (top, left) is the first to be created and it's part of a special case, since all the other incomming cards
    will be based on its position at the game board.

    Once the first card is created, the loop will look for two different cases:
    
        elif i = 0:
            creates the first card of every row, considering the y position of the previous row
        elif i > 0:
            creates all the cards of the row (except for the first one) leaving a litle gap between them

    Each generated card will be appended to a list named 'card_list' that will be used in the game:

        card_list.append(card)
    
    The variable 'num' represents the total amount of card the board game has and it is intereted in every end of the loop.
    Once 'num' reaches the amount of the card that are suposed to be on the game board, the loop will reach its end:

            if num == cards_vert * cards_hor:
                break

    """
    for j in range (0, cards_vert): # number of cards on the vertical
        for i in range (0, cards_hor): # number of cards on the horizontal
            if i == 0 and j == 0:
                card = Card(card_width, card_height, card_center_x, y_card, card_green)
                card.draw_flip(game_deck[0][0], game_deck[0][1])

            elif i == 0:
                card = Card(card_width, card_height, card_center_x, card_list[-1].y + card_height + card_dist, card_green)
                line = lineno() + 2
                try:
                    card.draw_flip(game_deck[num][0], game_deck[num][1])
                except:
                    print("-"*30," E R R O R " + "-"*30 )
                    print(f'File "game_mode.py", line {line}\n')
                    print(f"'{cards_hor} x {cards_vert}' is not a valid game mode")
                    print("Try making a game mode that will generate a odd number of cards\n" + "-"*72)
                    exit()

            elif i > 0:

                card = Card(card_width, card_height, card_list[-1].x + card_width + card_dist, card_list[-1].y, card_green)
                line = lineno() + 2
                try:
                    card.draw_flip(game_deck[num][0], game_deck[num][1])
                except:
                    print("-"*30," E R R O R " + "-"*30 )
                    print(f'File "game_mode.py", line {line}\n')
                    print(f"'{cards_hor} x {cards_vert}' is not a valid game mode")
                    print("Try making a game mode that will generate a odd number of cards\n" + "-"*72)
                    exit()


            if num == cards_vert * cards_hor:
                break
            num += 1
            card_list.append(card)
    # # # for i in range(0, len(card_list)):
    # # #     print("shape: ", str(card_list[i].shape))
    # # #     print("shape color ", str(card_list[i].shape_color))
    # # #     print("-"*30)
    flipped_cards_num = 0
    flips = 0
    flipped_cards_list = []
    flipped_time = 0
    remove = False
    clickable = True
    while not done:
        gameDisplay.fill(background_color)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif remove == False and event.key == pygame.K_SPACE:
                    remove = True
                elif remove == True and event.key == pygame.K_SPACE:
                    remove = False
                elif event.key == pygame.K_BACKSPACE:
                    done = True
            
            elif event.type == timer_set and flipped_cards_num == 2:
                flipped_time += 1

        ##################### CHECK ACCORDLY TO MOUSE/CARD COLLISION ########################
        for card in card_list:
            if card.selected == False:

                if card.collision(mouse):
                    # in case it is colliding, the card color is set to white
                    card_color = white
                    
                    if click and clickable == True and event.type == pygame.MOUSEBUTTONUP:
                        flipped_cards_num += 1
                        flipped_cards_list.append(card)
                        card.selected = True
                        flip_sound.play()
                        if flipped_cards_num == 2:
                            flips += 1
                            clickable = False
                    
                else:
                    # in case the mouse is not colliding with the card, its color is set to green

                    card_color = card_green
                card.draw_card(card_color,0)
            else:
                if flipped_time >= 2:
                    if card_check(flipped_cards_list[-1], flipped_cards_list[-2]):
                        card_list.remove(flipped_cards_list[-2])
                        card_list.remove(flipped_cards_list[-1])
                        flips = 0
                        score += 100
                        
                    else:
                        flipped_cards_list[-2].selected = False
                        flipped_cards_list[-1].selected = False
                        if flips >= 2:
                            score = score - (20 * (flips - 1))
                    if score <= 0:
                        score = 0
                    
                    clickable = True
                    flipped_time = 0
                    flipped_cards_num = 0



                if card.collision(mouse):
                    outline_flip = white
                else:
                    outline_flip = card.shape_color

                card.draw_card(background_color, 0)
                card.draw_card(outline_flip, 2)
                card.draw_flip(card.shape, card.shape_color)

        # creates the EXIT button
        exit_button = Button(button_width, button_height, 5, display_height - button_height - 5, 'Exit')
        # score_text = Card(button_width, button_height, 5, 5, str('Score: ' + str(score)) )
        congratulations = Button(button_width, button_height, display_width /2 - button_width/2, display_height/2, 'Congratulations')
        if exit_button.collision(mouse):
            button_color = white
        else:
            button_color = yellow
        exit_button.draw_button(button_color, 2)

        exit_button.draw_text(button_color)

        if exit_button.button(mouse):
            done = True
        if done and not card_list:
            save_score(score)
        try:
            previous_score = get_score()[0]
            high_score = get_score()[1]
            
        except:
            previous_score = 0
            high_score = 0
        board = Card(board_width, board_height, (display_width/2  - board_width/2), (display_height/2 - board_height/2))
        # board.draw_card(cyan)
        display_text(display_width - 200, 5, cyan, size = 25, text = str('Last Score: ' + str(previous_score)))
        display_text(display_width - 200, 50, cyan, size = 25, text = str('Best Score: ' + str(high_score)))
        display_text(5, 5, yellow, size = 25, text = str('Score: ' + str(score)))

        if not card_list:
            congratulations.draw_text(cyan, 50)
            if playable:
                if score > high_score:
                    win_sound1.play()
                else:
                    win_sound2.play()
                playable = False
        

 
        
        pygame.display.flip()
        pygame.display.update()
        clock.tick(100)