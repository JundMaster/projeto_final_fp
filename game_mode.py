import pygame
from Card_class import *
from colors import *

display_width = 1220
display_height = 700
gameDisplay = pygame.display.set_mode([display_width, display_height])

# card_width1 = display_width/13 + 20
# card_height1 = display_height/5 + 20

# card_width = card_width1 - 20
# card_height = card_height1 - 20


# card_x = 0
# card_y = 0
# card_dist = 10

display_center_x = display_width - display_width/2
display_center_y = display_height - display_height/2

def card_check(card1, card2):
    if (card1.shape == card2.shape) and (card1.shape_color == card2.shape_color):
        return True
    else:
        return False

clock = pygame.time.Clock()

def in_game(cards_hor, cards_vert):
    gameDisplay.fill(background_color)
    done = False

    board_width = display_width - display_width/4
    board_height = display_height - display_height/4
    
    card_width = (board_width/cards_vert) / 2.5
    card_dist = card_width/15
    card_height = card_width*1.5
    card_x = 0 
    card_y = 0
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
    shape_color = [something, red, blue, green, cyan, pink, yellow]
     
    score = 0
    pudim_list = []
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
    
    The first card (top, left) is the first to be created and it's part of a special case, since all the other incomming card
    will be based on its position at the game board.

    Once the first card is created, the loop will check for two different cases:
    
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
                card = Card(card_width, card_height, card_center_x, y_card, green)
                card.draw_flip(game_deck[0][0], game_deck[0][1])

            elif i == 0:
                card = Card(card_width, card_height, card_center_x, card_list[-1].y + card_height + card_dist, green)
                card.draw_flip(game_deck[num][0], game_deck[num][1])

            elif i > 0:
                card = Card(card_width, card_height, card_list[-1].x + card_width + card_dist, card_list[-1].y, green)
                card.draw_flip(game_deck[num][0], game_deck[num][1])
            if num == cards_vert * cards_hor:
                break
            num += 1
            card_list.append(card)
    # for i in range(0, len(card_list)):
    #     print("shape: ", str(card_list[i].shape))
    #     print("shape color ", str(card_list[i].shape_color))
    #     print("-"*30)
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
                done = True
            # elif event.type == timer_set:
            #     clickable += 1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                elif remove == False and event.key == pygame.K_SPACE:
                    remove = True
                elif remove == True and event.key == pygame.K_SPACE:
                    remove = False
            
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
                        if flipped_cards_num == 2:
                            clickable = False
                    
                else:
                    # in case the mouse is not colliding with the card, its color is set to green

                    card_color = green
                card.draw_card(card_color,0)
            else:
                if flipped_time >= 2:
                    if card_check(flipped_cards_list[-1], flipped_cards_list[-2]):
                        card_list.remove(flipped_cards_list[-2])
                        card_list.remove(flipped_cards_list[-1])
                        
                    else:
                        flipped_cards_list[-2].selected = False
                        flipped_cards_list[-1].selected = False
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

        if not card_list:
            print("YOU WON THE GAME, BRO!")
            done = True 

        


 
        
        pygame.display.flip()
        pygame.display.update()
        clock.tick(100)
