import pygame
import inspect

display_width = 1220
display_height = 700
gameDisplay = pygame.display.set_mode([display_width, display_height])

# gets the code line
def lineno():
    return inspect.currentframe().f_back.f_lineno

# take a list of string with numbers in it and return a list of ints
def get_gm_list(game_mode):
    temp_list = []
    number = []
    mode_list = []
    return_list = []
    minor = 0
    major = 2
    num = 0
    list_len = len(game_mode[0])

    for j in range (0, len(game_mode)):
        for i in range (0, len(game_mode[j])):
            if game_mode[j][i].isdigit():
                number.append(str(game_mode[j][i]))

            elif number:
                temp_list.append(number)
                number = []

            if i == len(game_mode[j]) - 1:
                temp_list.append(number)
                number = []

    for i in range(0, len(temp_list)):
        try:
            mode_list.append(int("".join(temp_list[i])))
        except:
            continue


    while num != len(mode_list)//2:
        for i in range (minor, major):
            number.append(mode_list[i])

        return_list.append(number)
        number = []
        num += 1
        minor += 2
        major += 2
    return return_list

def display_text(x, y, color, size = 25, text = None):
    myfont = pygame.font.Font('NotoSans-Regular.ttf', size)
    gameDisplay.get_rect(center=(x, y))
    font_size = myfont.size(text)
    my_text = myfont.render(text, 1, color)
    gameDisplay.blit(my_text, (x, y))

def card_check(card1, card2):
    if (card1.shape == card2.shape) and (card1.shape_color == card2.shape_color):
        return True
    else:
        return False

def save_score(score):
    with open('score.txt', 'a') as score_file:
        score_file = open('score.txt', 'a')
        score_file.write('Score: ' + str(score) + '\n')

# reads the score from the score file and return both the last and highest one
def get_score():
    with open('score.txt', 'r') as score_file:
        temp_list = []
        score_list = []
        number = []
        for line in score_file:
            for i in range(0, len(line)):
                if line[i].isdigit():
                    number.append(line[i])
                elif number:
                    temp_list.append(number)
                    number = []
    for i in range (0, len(temp_list)):
        score_list.append(int("".join(temp_list[i])))
    return (score_list[-1], max(score_list))
