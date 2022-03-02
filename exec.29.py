#Jogo da adivinhação
#Escreva um programa que faça o computador, 'pensar' em um número inteiro entre 0 e 5 e peça para o usário tentar
#descobrir qual foi o número escolhido pelo computador: O programa derá escrever na tela se o usuário venceu ou perdeu.
from random import randint#inportação de biblioteca
from time import sleep
computador=randint(0,5)#Faz o computador "PESSAR# "
print('-=-'*20)
print('\033[1;32mVou pesar em um núméro entre 0 e 5 , tente adivinhar...\033[m')
print('-=-'*20)
jogador=int(input('\033[1;34mEm que numero eu pensei?\033[m'))#Jogador tenta adivinhar
print('\033[1;31mPROCESSANDO...\033[m')
sleep(3)
if jogador==computador:
    print('\033[1;33mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
    print('\033[1;35mGANHEI! Eu pensei no número {} e não no {}!\033[m'.format(computador,jogador))
