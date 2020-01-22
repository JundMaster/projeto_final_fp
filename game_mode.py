import pygame
from Card_class import *
from colors import *

display_width = 1220
display_height = 700
gameDisplay = pygame.display.set_mode([display_width, display_height])

card_width1 = display_width/13 + 20
card_height1 = display_height/5 + 20

card_width = card_width1 - 20
card_height = card_height1 - 20


card_x = 0
card_y = 0
card_dist = 10

display_center_x = display_width - display_width/2
display_center_y = display_height - display_height/2


# card_x_1 = card_x
# for i in range(10): # number of cards on the horizontal
#     card_x_1 = card_x_1 + card_width + card_dist
#     i += 1

# card_x_1 = card_x_1/2  

# card_center_x = display_center_x - card_x_1

# card_y_1 = card_y
# for i in range(3): # number of cards on the vertical
#     card_y_1 = card_y_1 + card_height + card_dist
#     i += 1

# card_y_1 = card_y_1/2  
# card_center_y = display_center_y - card_y_1

def card_check(card1, card2):
    if (card1.shape == card2.shape) and (card1.shape_color == card2.shape_color):
        return True
    else:
        return False

clock = pygame.time.Clock()

def in_game(cards_hor, cards_vert):
    gameDisplay.fill(background_color)
    done = False
    fliped_cards_num = 0
    flips = 0
    fliped_cards_list = []  

##############################################################
    card_x_1 = card_x                                       
    for i in range(cards_hor): # number of cards on the horizontal
        card_x_1 = card_x_1 + card_width + card_dist
        i += 1

    card_x_1 = card_x_1/2  

    card_center_x = display_center_x - card_x_1

    card_y_1 = card_y
    for i in range(cards_vert): # number of cards on the vertical
        card_y_1 = card_y_1 + card_height + card_dist
        i += 1

    card_y_1 = card_y_1/2  
    card_center_y = display_center_y - card_y_1
#############################################################


    shape_list = ['square','circle', 'circle', 'square']
    shape_color = [red, blue, red, blue]
    random.shuffle(shape_list)
    random.shuffle(shape_color)
    score = 0
    pudim_list = []
    possible = []
    for i in shape_list:
        for j in shape_color:
            possible.append((i,j))
    random.shuffle(possible)

    game_deck = []

    for i in range (0, len(possible)):
        game_deck.append(possible[i])
        game_deck.append(possible[i])
        
    y_card = card_center_y

    for i in range (0, cards_vert): # number of cards on the vertical
        for i in range (0, cards_hor): # number of cards on the horizontal
            if i == 0:
                card = Card(card_width, card_height, card_center_x, y_card, green)
                card.draw_flip(game_deck[0][0], game_deck[0][1])
            elif i < 20:
                card = Card(card_width, card_height, pudim_list[i-1].x + card_width + card_dist, y_card, green)
                card.draw_flip(game_deck[i-1][0], game_deck[i-1][1])
            
            pudim_list.append(card)
        y_card += card_height + card_dist

    card_list = []
    for i in range (0, len(pudim_list)):
        card_list.append(pudim_list[i])
    # card_list = [pudim_list[0], pudim_list[1], pudim_list[2], pudim_list[3], pudim_list[4]]
    while not done:

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()  
            for card in card_list:
                if card.selected == False:
                    clicked = True
                    if card.collision(mouse):
                        card.draw_card(white, 0)
                        
                        if click:
                            if fliped_cards_num == 2:
                                fliped_cards_num = 0 
                                

                            card.selected = True
                            fliped_cards_list.append(card)
                            fliped_cards_num += 1
                        
                            if fliped_cards_num == 2:
                                flips += 1
                                print(str(fliped_cards_list[0].shape))
                                # checks if the fliped cards match and removes them from card_list
                                if card_check(fliped_cards_list[-1], fliped_cards_list[-2]):
                                    
                                    # paint a background colored card over the removed cards
                                    fliped_cards_list[-1].draw_card(background_color, 0)
                                    fliped_cards_list[-1].draw_card(background_color, 2)
                                    fliped_cards_list[-2].draw_card(background_color, 0)
                                    fliped_cards_list[-2].draw_card(background_color, 2)
                                    card_list.remove(fliped_cards_list[-1])
                                    card_list.remove(fliped_cards_list[-2])

                                    # gameDisplay.fill(background_color)
                                    score += 100
                                    flips = 0
                                else:
                                    for i in range (1, flips+1):
                                        if i == 1:
                                            continue
                                        else:
                                            score -= 20*(flips-1)
                                            if score < 0:
                                                score = 0
                                            break


                                print("score: ", str(score))
               
                    else:
                        card.draw_card(background_color, 2)
                        card.draw_card(green, 0) 
                    if not card_list:
                        print("you won")
                else: 
                    clicked = False
                    if fliped_cards_num == 2:
                        # pygame.time.wait(2000)
                        card.selected = False
                        continue
                    # checks if the mouse is colliding with the fliped card and defines it's outline color    
                    if card.collision(mouse):
                        outline_color = white
                    else:
                        outline_color = card.shape_color

                    card.draw_card(background_color, 0)
                    card.draw_card(outline_color, 2)
                    card.draw_flip(card.shape, card.shape_color)

                    
                    # print("seconds: ", str(seconds))
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
        