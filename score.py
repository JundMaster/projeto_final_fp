def save_score(score):
    with open('score.txt', 'a') as score_file:
        score_file = open('score.txt', 'a')
        score_file.write('Score: ' + str(score) + '\n')
    with open('score.txt', 'r') as score_file:
        temp_list = []
        score_list = []
        j = 0
        number = []
        for line in score_file:
            for i in range(0, len(line)):
                if line[i].isdigit():
                    number.append(line[i])
                elif number:
                    temp_list.append(number)
                    number = []
    score_file.close()
    for i in range (0, len(temp_list)):
        score_list.append(int("".join(temp_list[i])))

def get_score():
    score_file = open('score.txt', 'r')
    temp_list = []
    score_list = []
    j = 0
    number = []
    for line in score_file:
        for i in range(0, len(line)):
            if line[i].isdigit():
                number.append(line[i])
            elif number:
                temp_list.append(number)
                number = []
    score_file.close()
    for i in range (0, len(temp_list)):
        score_list.append(int("".join(temp_list[i])))
    return (score_list[-1], max(score_list))
