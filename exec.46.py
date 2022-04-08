#Papel e Tesoura
#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens = ('pedra','Papel', 'tesoura')
computador = randint(0, 2)
print(''''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-='*10)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*10)
if computador == 0:# computador jogou PEDRA
    elif jogador == 1:

    elif jogador == 2:
    else:
    print('JOGADA INVALIDA!')
elif computador == 1:# computador jogou PAPEL
    if jogador == 0:
    elif jogador == 1:
    elif jogador == 2:
    else:
        print('JOGADA INVALIDA!')
elif  computador == 2:# computador jogou TESOURA
    if jogador == 0:
    