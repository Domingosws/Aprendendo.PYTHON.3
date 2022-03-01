#Jogo da adivinhação
#Escreva um programa que faça o computador, 'pensar' em um número inteiro entre 0 e 5 e peça para o usário tentar
#descobrir qual foi o número escolhido pelo computador: O programa derá escrever na tela se o usuário venceu ou perdeu.
from random import randint
computador=randint(0,5)#Faz o computador "PESSAR# "
print('-=-'*20)
print('Vou pesar em um núméro entre 0 e 5 , tente adivinhar')
print('-=-'*20)
jogador=int('Ém que número eu pensei?')
if jogador==computador:
    print('PARABÉNS! Você conceguiu me vencer!')
    