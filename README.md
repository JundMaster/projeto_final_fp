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
##### Best Score & Last Score
Cada vez que o jogador "limpa" o tabuleiro por completo o programa registra a sua pontuação num ficheiro: *score.txt*.
Posteriormente é feita uma comparação entre todas as pontuações registradas no ficheiro e a maior delas é tida como *best score*.
A pontuação obtida na última vez em que se jogou e o tabuleiro foi "limpo" é tida como *last score*.
Uma música é tocada a cada vez que o jogador consegue limpar o tabuleiro.
Caso a pontuação feita supere o *best score* toca uma música, caso não aconteça, toca outra.
## Funcionalidade
