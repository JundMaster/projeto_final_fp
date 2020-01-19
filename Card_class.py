import pygame
import random
from colors import *

pygame.init()
display_width = 1220
display_height = 700
gameDisplay = pygame.display.set_mode([display_width, display_height])



white = [255, 255, 255]
class Card:

    def __init__(self, width, height, x, y, color):
        self.width = width
        self.height = height
        self.x = x 
        self.y = y
        self.color = color
        self.random_color = random.choice([red, blue, pink])
        self.surface = gameDisplay
        self.clickable = True
        self.clicked = False
        self.being_clicked = False
        self.selected = False
        self.card_outline = red
        self.mouse_click = pygame.mouse.get_pressed()[0]
    
    # def collision(self, mouse_position):
    #     if (self.x + self.width > mouse_position[0] > self.x and self.y + self.height > mouse_position[1] > self.y):
    #         print("colides")
    def collision(self, mouse):
        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            return True
        else:
            return False

    def draw_card(self, color, stroke):
            pygame.draw.rect(self.surface, color, (self.x, self.y, self.width, self.height), stroke)

    def draw_flip(self, shape, shape_color, stroke = 2):
        self.shape = shape
        self.shape_color = shape_color
        ########################### RECTANGLE SHAPE ########################
        # Defines the size of the rectangle
        self.rect_size = self.height / 3
        # Defines the center (x,y) of the rectangle
        self.Xc_rect = (self.x + self.width/2) - (self.x + self.rect_size/2)
        self.Yc_rect = (self.y + self.height/2) - (self.y + self.rect_size/2)
        self.rect_x = self.x + self.Xc_rect
        self.rect_y = self.y + self.Yc_rect
        ####################################################################
        ########################### CIRCLE SHAPE ###########################
        self.circle_radius = int(self.width/2 - self.width/4)
        self.circle_x = int(self.x  + self.width/2)
        self.circle_y =  int(self.y + self.height/2)
        ####################################################################
        ########################### CIRCLE SHAPE ###########################



        if self.selected:
            if shape == 'square':
                pygame.draw.rect(self.surface, self.shape_color, (self.rect_x, self.rect_y, self.rect_size, self.rect_size), 2)
            
            elif shape == 'circle':
                pygame.draw.circle(self.surface, self.shape_color, (self.circle_x,self.circle_y ), self.circle_radius, 2)


    
    
    
    def button(self, mouse):
        if self.collision(mouse) == True and self.mouse_click == 1:
            return 1
        else:
            return 0

class OptionText(Card):

    def draw_text(self, text, x_center, y_center):
        myfont = pygame.font.Font('NotoSans-Regular.ttf', 25)
        text1 = myfont.render(text, 1, white)
        gameDisplay.blit(text1, (x_center, y_center))