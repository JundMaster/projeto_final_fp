# Projeto Final - Shuffle
---
## Descrição do projeto
“Shuffle” é um jogo de memória, em que o jogador tem de encontrar os pares de cartas virando apenas duas de cada vez. Caso as cartas viradas formem um par, o jogador recebe 100 pontos e as cartas são eliminadas do tabuleiro.
![alt text](/README_images/cards_match.png)
![alt text](/README_images/cards_match1.png)
Caso as cartas não formem um par, ambas serão viradas para baixo novamente e o número de tentativas falhadas é incrementado.
A penalização que o jogador sofrerá na sua pontuação é definido com base no número de tentativas falhadas.
```
penalização = P
tentativas falhadas = TF
P = TF * 20
```
Nenhuma penalização é dada caso o jogador ainda esteja na sua primeira tentativa falhada e o contador de tentativas é reiniciado a cada acerto.
A pontuação nunca é inferior a 0.
#### Best Score & Last Score
Cada vez que o jogador "limpa" o tabuleiro por completo o programa registra a sua pontuação num ficheiro: *score.txt*.
Posteriormente é feita uma comparação entre todas as pontuações registradas no ficheiro e a maior delas é tida como *best score*.</p>
A pontuação obtida na última vez em que se jogou e o tabuleiro foi "limpo" é tida como *last score*.
Uma música é tocada a cada vez que o jogador consegue limpar o tabuleiro.
Caso a pontuação feita supere o *best score* toca uma música, caso não aconteça, toca outra.
## Estruturação do código
O código está distribuído entre 5 ficheiros .py principais:
* [main.py](https://github.com/JundMaster/projeto_final_fp/blob/master/main.py)
* [game_mode.py](https://github.com/JundMaster/projeto_final_fp/blob/master/game_mode.py)
* [classes.py](https://github.com/JundMaster/projeto_final_fp/blob/master/classes.py)
* [functions.py](https://github.com/JundMaster/projeto_final_fp/blob/master/functions.py)

O restante dos arquivos diz respeito a sons, imagens e fontes usadas no jogo.

### [main.py](https://github.com/JundMaster/projeto_final_fp/blob/master/main.py)
Este é o ficheiro principal do jogo. É aquele que deve ser corrido para que o jogo seja aberto.</p>
O [main.py](https://github.com/JundMaster/projeto_final_fp/blob/master/main.py) contém a função *game_menu()* que, assim como o nome indica, apresenta o menu principal ao jogador.
![alt text](/README_images/game_menu.png)
Mas para além de mostrar na tela o menu principal, esta função realiza todos os processos necessários para a execução das tarefas que são atribuídas a cada botão presente na tela.
##### Botões:
Para criar os botões que o jogo vai aprensentar, basta acrescentar o texto referente ao *game mode* pretendido na lista game_mode:
<br/><br/>
```python
game_mode = ['4 x 3', '4 x 4', '5 x 4', '6 x 5', '6 x 6','Exit']
```
*Esta lista deve conter SOMENTE strings.*</p>
Uma vez que esta lista está criada, é invocada a função *get_gm_list()* que vai converter toda essa lista de strings, para uma lista de inteiros:
```python
gm_list = [[4, 3], [4, 4], [5, 4], [6, 5], [6, 6]]
```
*Esta função vai explicada mais à frente.*</p>
Sendo esta uma lista de inteiros, o conteúdo do botão 'Exit é ignorado e deixado de fora desta lista.</p>
A função chega então a um loop, que irá criar realmente os botões.</p>
```py
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
        
        # if the buttons excede the display dimensions it will rise an error with a possible solution
        if button_set[i].y + button_set[i].height>= display_height:
            print("-"*30 + " E R R O R " + "-"*30 + "\nThe amount of buttons exceeds the display height")
            print("Try either repositioning the button set or creating less buttons\n" + "-"*72)
```
Como a posição do primeiro botão é fixa, há que ter cuidado na criação de novos botões, pois eles podem exceder as medidas da tela de jogo. E se for este o caso, será impressa na command line a seguinte mensagem de erro:
```
------------------------------ E R R O R ------------------------------
The amount of buttons exceeds the display height
Try either repositioning the button set or creating less buttons
------------------------------------------------------------------------
```
Cada botão é uma instância da classe *Button* (também será melhor explicada adiante).</p>
Sendo um *Button* cada um dos botões deve receber os seguintes parâmetros:
* largura;
* altura;
* posição x;
* posição y;
* texto do *game mode*;
Ao entrar no loop, são criados os botões com base nas strings contidas na lista *game_mode* e os *Button*'s são realmente colocados na lista *button_set*:
```python
button_set.append(Button(button_width, button_height, button_x, button_y, game_mode[<index>]))
```
<sub>*A lista *button_set* contém, REALMENTE, os botões. Não é apenas uma lista de strings ou inteiros.*</sub>
<sub>As strings passadas na lista *game_mode* serão, exatamente, os textos dos botões. 
</sub><br/>
Os botões são criados por ordem, guiados pela posição do primeiro, mantendo uma pequena distância entre si.
O botão 'Exit' é o único que é tratado de forma diferente. Ele deve ser o ÚLTIMO da lista *game_mode* e o seu texto deverá conter de alguma forma as letras ['E', 'X', 'I', 'T'], nesta ordem, para que seja atribuída uma distância um pouco maior entre ele e o botão anterior.</p>
Posteriormente, a função trata verificar a colisão do mouse com o botão, e pinta-o de acordo e também imprime a string passada na lista *game_mode* no botão:
```python
for button in button_set:
    if button.collision(mouse) == True:
        button_color = white
    else:
        button_color = yellow
    # draws button text based on the game_mode list elements    
    button.draw_text(button_color)
    button.draw_button(button_color, 2)
```
Feito isto, o programa verifica se algum botão é clicado, caso seja, entrará no modo de jogo definido. Caso o botão seja o 'Exit', o jogo irá encerrar.</p>
Caso seja passada na lista *game_mode* uma string que não contenha, pelo menos, dois números ou a string 'exit' o jogo irá fechar e apresentar uma mensagem de erro.</p>
Segue o exemplo caso seja passado na lista a string 'pudim':
```
------------------------------  E R R O R ------------------------------
File "main.py", line 126
'pudim' is not a valid game mode.

Try creating a game mode with the format '4 x 3'.
The game mode you add to the list MUST be a string.
------------------------------------------------------------------------
```
Esta verificação é feita da seguinte forma:
```python
try:
    in_game(gm_list[i][0], gm_list[i][1])
except IndexError:
    <imprime o erro referido acima>
```
Não havendo nenhum erro, a função *in_game()* é chamada, e passa-se como parâmetro os valores guardados na lista *gm_list* que correspondem ao número de cartas na horizontal e vertical, respectivamente:
```python
gm_list = [[4, 3], [4, 4], [5, 4], [6, 5], [6, 6]]
```
### [game_mode.py](https://github.com/JundMaster/projeto_final_fp/blob/master/game_mode.py)
Este ficheiro contém a função que roda o modo de jogo selecionado: 
`in_game(cards_hor, cards_vert)`.</p>
Inicialmente, esta função define o tamanho máximo do "tabuleiro" de cartas, tendo em conta o tamanho da janela de jogo:
`board_width = display_width - display_width/6`
`board_height = display_height - display_height/6`
Em seguida, é definido a dimensão das cartas, que tem me conta o tamanho do tabuleiro desta vez.</p>
E para que a dimensão das cartas fosse estéticamente agradável, inicialmente adotou-se um método para estabelecer primeiro a largura da carta e depois a altura, em função da largura. Mas isto só funcionava para casos em que o número de cartas horizontais fosse maior que o número de cartar verticais. Quando o caso era inverso, as cartas podiam ultrapassar o limite do tabuleiro, em termos de largura.</p>
Para contornar esse problema, adotou-se a seguinte medida: 
```py
if cards_vert > cards_hor:
    card_width = (board_width/cards_vert) / 2.5
else:
    card_width = (board_width/cards_hor) / 2.5
```
Isto verifica em que caso nos encontramos - mais cartas na vertical (ou igual número de cartas) ou na horizontal. E assim define a dimensão das cartas, de modo a não se ultrapassar as medidas máximas do tabuleiro.</p>
Tendo estabelecido a largura das cartas, o programa então define a distância que deverá haver entre as cartas, considerando a sua largura:
`card_dist = card_width/15` 
Desta forma, garantimos que, mesmo não havendo uma distância fixa estabelecida entre as cartas, ela sempre será proporcional à largura das mesmas, o que depende do número de cartas no ecrã.</p>
Procede-se da mesma forma para a altura das cartas:
`card_height = card_width*1.5`
As formas que aparecem nas cartas são passadas numa lista de strings:
```py
shape_list = ['square', 'circle', 'triangle']
```
<sub>*Mais à frente será explicado como estas strings influenciam realmente na forma atribuida à carta.*</sub></p>
E as cores das cartas são passadas em outra lista.
```py
shape_color = [cyan, red, blue, green, orange, pink, yellow, blue_green]
```
<sub>*Todas estas variáveis estão definidas no ficheiro [colors.py](https://github.com/JundMaster/projeto_final_fp/blob/master/colors.py).*</sub></p>
Tendo listado as cores e formas possíveis, o programa cria uma lista de cartas que são possíveis criar combinando ambos os parâmetros:
```py
possible = []
for j in shape_color:
    for i in shape_list:
        possible.append((i,j))
```
Como próximo passo, o programa verifica, com base na quantidade de cartas possíveis, é possível criar número de cartas que se pretende no *game mode* escolhido.</p>
Caso não seja possível, o jogo fecha e a seguinte mensagem de texto é impressa na linha de comandos:
```
----------------------------------  E R R O R  ----------------------------------
The game board has too many cards.
You may try either creating new colors/shapes or reducing the amount of cards.
---------------------------------------------------------------------------------
```
