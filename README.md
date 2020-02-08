# Projeto Final - Shuffle
![alt text](/README_images/game_menu.png)
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
O [main.py](https://github.com/JundMaster/projeto_final_fp/blob/master/main.py) contém a função `game_menu()` que, assim como o nome indica, apresenta o menu principal ao jogador.
![alt text](/README_images/game_menu.png)
Mas para além de mostrar na tela o menu principal, esta função realiza todos os processos necessários para a execução das tarefas que são atribuídas a cada botão presente na tela.
#### Botões:
Para criar os botões que o jogo vai aprensentar, basta acrescentar o texto referente ao *game mode* pretendido na lista `game_mode`:
<br/><br/>
```python
game_mode = ['4 x 3', '4 x 4', '5 x 4', '6 x 5', '6 x 6','Exit']
```
*Esta lista deve conter SOMENTE strings.*</p>
Uma vez que esta lista está criada, é invocada a função `get_gm_list()` que vai converter toda essa lista de strings, para uma lista de inteiros:
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
Sendo um `Button` cada um dos botões deve receber os seguintes parâmetros:
* largura;
* altura;
* posição x;
* posição y;
* texto do *game mode*;</p>
Ao entrar no loop, são criados os botões com base nas strings contidas na lista `game_mode` e os *Button*'s são realmente colocados na lista `button_set`:
```python
button_set.append(Button(button_width, button_height, button_x, button_y, game_mode[<index>]))
```
<sub>*A lista *`button_set`* contém, REALMENTE, os botões. Não é apenas uma lista de strings ou inteiros.*</sub></p>
<sub>As strings passadas na lista *`game_mode`* serão, exatamente, os textos dos botões. 
</sub><br/>
Os botões são criados por ordem, guiados pela posição do primeiro, mantendo uma pequena distância entre si.
O botão 'Exit' é o único que é tratado de forma diferente. Ele deve ser o ÚLTIMO da lista `game_mode` e o seu texto deverá conter de alguma forma as letras ['E', 'X', 'I', 'T'], nesta ordem, para que seja atribuída uma distância um pouco maior entre ele e o botão anterior.</p>
Posteriormente, a função trata verificar a colisão do mouse com o botão, e pinta-o de acordo e também imprime a string passada na lista `game_mode` no botão:
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
Feito isto, o programa verifica se algum botão é clicado. Caso seja, entrará no modo de jogo definido.</p>
Caso o botão seja o 'Exit', o jogo irá encerrar.</p>
Caso seja passada na lista `game_mode` uma string que não contenha, pelo menos, dois números ou a string 'exit' o jogo irá fechar e apresentar uma mensagem de erro.</p>
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
Não havendo nenhum erro, a função `in_game()` é chamada, e passam-se como parâmetro os valores guardados na lista `gm_list` que correspondem ao número de cartas na horizontal e vertical, respectivamente:
```python
gm_list = [[4, 3], [4, 4], [5, 4], [6, 5], [6, 6]]
```
### [game_mode.py](https://github.com/JundMaster/projeto_final_fp/blob/master/game_mode.py)
Este ficheiro contém a função que roda o modo de jogo selecionado: 
`in_game(cards_hor, cards_vert)`.</p>
#### Dimensões:
Inicialmente, esta função define o tamanho máximo do "tabuleiro" de cartas, tendo em conta o tamanho da janela de jogo:
`board_width = display_width - display_width/6`</p>
`board_height = display_height - display_height/6`</p>
Em seguida, é definida a dimensão das cartas, que tem me conta o tamanho do tabuleiro desta vez.</p>
E para que a dimensão das cartas fosse estéticamente agradável, inicialmente adotou-se um método para estabelecer primeiro a largura da carta e depois a altura (em função da largura). Mas isto só funcionava para casos em que o número de cartas horizontais fosse maior que o número de cartar verticais. Quando o caso era inverso, as cartas podiam ultrapassar o limite do tabuleiro, em termos de largura.</p>
Para contornar esse problema, adotou-se a seguinte medida: 
```py
if cards_vert > cards_hor:
    card_width = (board_width/cards_vert) / 2.5
else:
    card_width = (board_width/cards_hor) / 2.5
```
Isto verifica em que caso nos encontramos - mais cartas na vertical (ou igual número de cartas) ou na horizontal. E assim define a dimensão das cartas, de modo a não se ultrapassar as medidas máximas do tabuleiro.</p>
Tendo estabelecido a largura das cartas, o programa então define a distância que deverá haver entre as cartas, considerando a sua largura:
`card_dist = card_width/15`.</p> 
Desta forma, garantimos que, mesmo não havendo uma distância fixa estabelecida entre as cartas, ela sempre será proporcional à largura das mesmas, o que depende do número de cartas no ecrã.</p>
Procede-se da mesma forma para a altura das cartas:
`card_height = card_width*1.5`.</p>
#### Cores e formas:
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
A lista `possible` passa a guardar as formas e cores como túpulos, seguindo o seguinte formato:
```
possible = [('square', [0, 255, 255]), ('circle', [0, 255, 255]), ('triangle', [0, 255, 255]]
```
Como próximo passo, o programa verifica, com base na quantidade de cartas possíveis, é possível criar número de cartas que se pretende no *game mode* escolhido.</p>
Caso não seja possível, o jogo fecha e a seguinte mensagem de texto é impressa na linha de comandos:
```
----------------------------------  E R R O R  ----------------------------------
The game board has too many cards.
You may try either creating new colors/shapes or reducing the amount of cards.
---------------------------------------------------------------------------------
```
#### Criação das cartas:
Não ocorrendo nenhum erro, o programa cria uma lista que contém pares de cartas, com base na lista de cartas possíveis:
```py
for i in range (0, (cards_vert * cards_hor)//2):
    game_deck.append(possible[i])
    game_deck.append(possible[i])
```
E então baralha a ordem destas cartas:
```
random.shuffle(game_deck)
```
Feito isto, é criada então mais uma lista - `card_list` -, que vai conter, desta vez, as cartas propriamente ditas, isto é, as instânciações da classe `Card`.</p>
<sub>*A explicação da criação destas instânciações está num docstring no próprio ficheiro [game_mode.py](https://github.com/JundMaster/projeto_final_fp/blob/master/game_mode.py).*</sub></p>
Considerando a possibilidade de se criar um *game mode* que não gere um número total de cartas par, como '3 x 3', adotou-se a seguinte medida:
```py
try:
    card.draw_flip(game_deck[num][0], game_deck[num][1])
except:
    print("-"*30," E R R O R " + "-"*30 )
    print(f'File "game_mode.py", line {line}\n')
    print(f"'{cards_hor} x {cards_vert}' is not a valid game mode")
    print("Try making a game mode that will generate a odd number of cards\n" + "-"*72)
    exit()
```
Isto irá sair do jogo e imprimir para a linha de comandos a seguinte mensagem:
```
------------------------------  E R R O R ------------------------------
File "game_mode.py", line 146

'3 x 3' is not a valid game mode
Try making a game mode that will generate a odd number of cards
------------------------------------------------------------------------
```
#### Lógica do jogo:
Para entender como a lógica foi estruturada, há que atentar para as seguintes variáveis:
* flipped_cards_num
* flipped_cards_list
* clickable
* card.selected
* flipped_time
* flips
* card_color
* score

`flipped_cards_num` trata-se do número de cartas que estão viradas com a face para cima.</p>
`flipped_cards_list` é uma lista que contém as cartas que foram viradas.</p>
`card.selected` é uma variável associada ao objeto *card*, que define se a carta encontra-se selecionada ou não</p>
`clickable` é uma variável booleana que define se a é possível clicar ou não nas cartas.</p>
`flipped_time` conta o tempo que se passou desde que duas cartas foram viradas.</p>
`flips` registra o número de vezes que o jogador tentou encontrar um par de cartas sem ter sucesso.</p>
`card_color` trata-se da cor da carta.</p>
`score` é a pontuação do jogador.</p>
___
O primeiro passo para desenhar as cartas, é verificar se cada carta está ou não selecionada, através da variável `selected`, da classe `Card`.</p>
Se o programa verificar que a carta não esta selecionada, ele avança para o passo seguinte:</p>
Verificar se o mouse está a colidir com a carta:</p>
* Caso esteja a colidir, a carta é pintada de branco, senão, deve ser pintada de verde;
* Verificar se é possível clicar nas cartas através da variável `clickable`:</p>
    Se as carta forem "clickable", for feito um click sobre uma carta e o usuário levantar o botão do rato, o programa avançará para o passo seguinte:
    * Incrementa o número de cartas viradas em uma unidade:</p>
    `flipped_cards_num += 1`</p>
    * Adiciona a carta clicada à lista de cartas viradas:</p>
    `flipped_cards_list.append(card)`</p>
    * Passa a carta para "selected":</p>
    `card.selected = True`</p>
    * Toca o som da carta a virar:</p>
    `flip_sound.play()`</p>
    * Verifica quantas cartas já foram viradas e caso o número seja 2, incrementa o número de tentativas em 1 unidade e torna as cartas não clicáveis:</p>
    `flips += 1`</p>
    `clickable = False`</p>
___
Uma vez que a carta estiver "selected", o programa irá deixar de verificar a colisão afim de desenhar a parte de trás da carta como verde ou branco.</p>
O que irá acontecer agora é desenhar a forma da carta (com a sua respectiva cor) e pintar o *outline* de branco, caso o rato esteja a colidir com a carta, ou da cor da forma caso não esteja.</p>
A partir do momento em que duas cartas estiverem selecionadas, a variável `fliped_card_num` irá assumir o valor 2, que é um gatilho para algumas ações ocorrerem:
* Nenhuma das cartas do tabuleiro será clicável;
* O número de tentativas é incrementado em 1 unidade;
* A variável `fliped_time` aumenta uma unidade a cada segundo;
  * Assim que esta variável atinge o valor 2 ou superior, a função `card_check()` é chamada, e verifica se as duas últimas cartas acrescentadas à lista de cartas viradas tem cor e forma correspondente.
    * Caso tenham o *score* aumenta em 100 unidades, o número de tentativas (`flips`) volta a ser 0 e as cartas são removidas da lista de cartas selecionadas.
    * Caso contrário, ambas as cartas selecionadas passam a estar "não selecionadas", e o jogador recebe uma penalização na pontuação tendo em conta o número de tentativas que realizou até o momento.
  * Independentemente do retorno da função `card_check()`, todas as cartas do tabuleiro passam a ser "clicáveis" novamente: `clickable = True`; o contador de tempo volta a zero: `flipped_time = 0` e o número de cartas viradas também volta a zero: `flipped_cards_num = 0`.</p>
  
#### Why not *pygame.time.delay*?
Inicialmente, a ideia era usar a função `pygame.time.delay()` para fazer o jogo esperar o tempo desejado até virar as cartas para baixo novamente.</p>
Entretanto, esta medida faz com que o jogo realmente pare. Sendo assim, enquanto não passasse o tempo que havia sido definido, nenhuma ação seria registrada.</p>
Quais são as implicações disto?</p>
Considerando o executável dado pelo professor, notei que mesmo quando as cartas estão viradas, o seu *outline* ainda sofria alterações caso houvesse colisão do rato com a carta. Isto significa que o jogo ainda estava a registrar as ações. Ele não estava simplesmente parado.</p>
Desta forma, para contornar a situação, fiz um simples contador de tempo que é acionado assim que o número de cartas viradas é 2, e que volta a zero assim que a função `card_check()` faz o seu trabalho.</p>
___
#### Registro de score:
Assim que o jogador limpa todo o tabuleiro, o programa registra a pontuação obtida nesse jogo e compara com a pontuação mais alta até aquele momento. E, dependendo do resultado da comparação, é tocada uma música de vitória diferente.</p>
Há uma música para quando o jogador ultrapassa a melhor pontuação até o momento: `win_sound1` e outra para caso isso não aconteça `win_sound2`.</p>


Se o jogador desistir a meio do jogo, não é feito registro algum de score.</p>
### [classes.py](https://github.com/JundMaster/projeto_final_fp/blob/master/classes.py)
Este ficheiro contém as duas classes utilizadas ao longo do código: `Card` e `Button`.</p>
As duas são muito semelhantes, pois a `Button` é uma variação da outra classe.</p>
Porque não usar a mesma classe?</p>
Inicialmente esta classe era uma só, mas mais tarde, pelo bem da legibilidade e da praticidade definiu-se uma classe apenas para os botões e outra apenas para as cartas.</p>
Esta é mais uma medida em vista a facilitar a compreensão e manipulação do código no futuro, não só por mim, mas por qualquer pessoa.</p>
Olhando agora para alguns dos métodos das classes, temos:</p>
`collision(self, mouse):`, que verifica a colisão do rato com a carta.</p>
`draw_card(self, color, stroke = 0)`, que desenha a carta com a cor e com a espessura de *outline* passados como parâmetro.</p>
`button(self, mouse)`, que verifica se a carta foi clicada.</p>
`draw_flip(self, shape, shape_color, stroke = 2)`, que é o método mais complexo desta classe `Card`.</p>
Esta função é invocada durante o jogo para desenhar a forma da carta, com a sua respectiva cor.</p>
Para isto, basta:
* Passar a forma da carta em formato de string;</p>
<sub>daí usar-se uma lista com strings, como referido anteriormente.
```py
shape_list = ['square', 'circle', 'triangle']
```
</sub>

* Passar a cor da forma;

Posteriormente o programa irá reconhecer o formato e cor passados como parâmetro e desenhá-los quando a função for invocada.

### [functions.py](https://github.com/JundMaster/projeto_final_fp/blob/master/functions.py)
Este ficheiro contém todas as funções do jogo, com exceção da `game_menu()` e da `in_game()`.</p>
Todas estas funções estavam, inicialmente, nos próprios ficheiros em que haviam de ser necessárias. Todavida, optou-se por colocá-las num ficheiro à parte pelo bem da legibilidade e organização do código.
A função mais complexa que está aqui definida, é a `get_gm_list(game_mode)`.
#### get_gm_list(game_mode)
O objetivo desta função é receber uma lista de strings e procurar por, pelo menos, dois números, em cada string e depois retornar a string recebida como uma lista de inteiros.</p>
Exemplo:
```py
game_mode = ['4 x 3']
get_gm_list(game_mode) = [4, 3]
```
Para fazer isto, a função deve percorrer a string com dois loops:
```py
for j in range (0, len(game_mode)):
    for i in range (0, len(game_mode[j])):
```
O primeiro para percorrer a lista passada como parâmetro, e o segundo para percorrer cada uma das strings da lista.</p>
Então verifica-se se o elemento da string que está a ser percorrido naquele momento é um número e adiciona-o a uma lista chamada `number`:
```py
if game_mode[j][i].isdigit():
    number.append(str(game_mode[j][i]))
```
Caso um elemento da string não seja um digito, o função entrará na seguinte condição:
```py
elif number:
    temp_list.append(number)
    number = []
```
Isto faz com que a lista `number` seja guardada numa lista chamada `temp_list`.</p>
Deste modo, a `temp_list` vai guardando listas de strings que são digitos.</p>
Então a lista `number` volta a estar fazia, para poder guardar mais números.</p>
Ao sair deste loop, entra-se em outro loop onde a lista de strings `temp_list` vai dar origem a uma lista de inteiros: `mode_list`.</p>
Então, ao invés de se ter uma lista com o formato:
```py
[['4'], ['3'], ['4'], ['4'], ['5'], ['4'], ['6'], ['5'], ['6'], ['6']]
```
Tem-se uma no formato:
```py
[4, 3, 4, 4, 5, 4, 6, 5, 6, 6]
```
E como passo final, esta lista dá origem a uma outra lista, que irá conter todos esses inteiros agrupados de dois em dois. Passa-se então a ter uma lista no formato:
```py
[[4, 3], [4, 4], [5, 4], [6, 5], [6, 6]]
```
E, por fim, esta lista sim pode ser usada passar os parâmetros da função `in_game()`
___
#### save_score(score)
Esta função cria um ficheiro de texto e salva nele a pontuação passada por parâmetro quando a função é chamada.</p>
Os ficheiros ficam salvos com o seguinte formato:
![alt text](/README_images/score_file.png)
___
#### get_score()
A `get_score()` é usada para abrir o ficheiro de texto que foi criado pela função `save_score()` e encontrar nesse ficheiro a última pontuação registrada e a maior dessas pontuações.</p>
Para isto, a função faz uma verificação muito semelhante à `get_gm_list()` e salva as pontuações lidas numa lista: `score_list`.</p>
A função retorna então o último valor dessa lista e o maior valor também:
```py
return (score_list[-1], max(score_list))
```
