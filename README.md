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
<br/><br/>*Esta lista deve conter SOMENTE strings.*<br/><br/>
Uma vez que esta lista está criada, é invocada a função *get_gm_list()* que vai converter toda essa lista de strings, para uma lista de inteiros:
```
gm_list = [[4, 3], [4, 4], [5, 4], [6, 5], [6, 6]]
```
<br/><br/>*Esta função vai explicada mais à frente.*<br/><br/>
Sendo esta uma lista de inteiros, o conteúdo do botão 'Exit é ignorado e deixado de fora desta lista.</p>
A função chega então a um loop, que irá criar realmente os botões.</p>
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
<sub>*A lista *button_set* contém, REALMENTE, os botões. Não é apenas uma lista de strings ou inteiros.*</sub><br/><br/>
<sub>As strings passadas na lista *game_mode* serão, exatamente, os textos dos botões. 
</sub><br/><br/>
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
### [game_mode.py](https://github.com/JundMaster/projeto_final_fp/blob/master/game_mode.py)
