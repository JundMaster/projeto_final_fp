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

    def draw_flip(self, stroke = 0):
        if self.selected:
            pygame.draw.rect(self.surface, self.random_color, (self.x, self.y, self.width, self.height), stroke)

    
    
    
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