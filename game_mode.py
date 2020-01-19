import pygame
from Card_class import *
from colors import *

display_width = 1220
display_height = 700
gameDisplay = pygame.display.set_mode([display_width, display_height])

card_width1 = display_width/13 + 20
card_height1 = display_height/5 + 20

card_width = card_width1 + 10
card_height = card_height1 + 10


card_x = 0
card_y = 0
card_dist = 10

display_center_x = display_width - display_width/2
display_center_y = display_height - display_height/2


card_x_1 = card_x
for i in range(3):
    card_x_1 = card_x_1 + card_width + card_dist
    i += 1

card_x_1 = card_x_1/2  

card_center_x = display_center_x - card_x_1



card_y_1 = card_y
for i in range(3):
    card_y_1 = card_y_1 + card_height + card_dist
    i += 1

card_y_1 = card_y_1/2  
card_center_y = display_center_y - card_y_1

def card_check(card1, card2):
    if (card1.shape == card2.shape) and (card1.shape_color == card2.shape_color):
        return True
    else:
        return False

clock = pygame.time.Clock()
def level1():
    done = False
    fliped_cards_num = 0
    flips = 0
    fliped_cards_list = []
    shape_list = ['square','square', 'square', 'square']
    shape_color = [red, blue, red, blue]
    random.shuffle(shape_list)
    random.shuffle(shape_color)

    card1 = Card(card_width, card_height, card_center_x, card_center_y, green)
    card1.draw_flip(shape_list[0], shape_color[0])
    #-------
    card2 = Card(card_width, card_height, card1.x + card_width + card_dist, card_center_y, green)
    card2.draw_flip(shape_list[1], shape_color[1])
    #-------
    card3 = Card(card_width, card_height, card2.x + card_width + card_dist, card_center_y, green)
    card3.draw_flip(shape_list[2], shape_color[2])
    #-------
    card4 = Card(card_width, card_height, card3.x + card_width + card_dist, card_center_y, green)
    card4.draw_flip(shape_list[3], shape_color[3])
    #-------
    card_list = [card1, card2, card3, card4]
   
    while not done:

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for card in card_list:
                if card.selected == False:
                    
                    if card.collision(mouse):
                        card.draw_card(white, 0)
                        
                        if click:
                            if fliped_cards_num == 3:
                                fliped_cards_num = 0
                                

                            card.selected = True
                            fliped_cards_list.append(card)
                            fliped_cards_num += 1
                        
                            if fliped_cards_num == 2:
                                flips += 1
                                print(str(fliped_cards_list[0].shape))
                                if card_check(fliped_cards_list[-1], fliped_cards_list[-2]):
                                    print("they match")
               
                    else:   
                        card.draw_card(green, 0) 
                
                else:   
                    if fliped_cards_num == 2:
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
                    # if card.collision(mouse):
                    #     card.draw_card(yellow,0)
                
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
        