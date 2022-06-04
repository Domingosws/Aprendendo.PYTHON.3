#Criando um Menu de Opções
#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('\033[1;36mPrimeiro valor: '))
n2 = int(input('Segundo valor:\033[m '))
opção = 0
while opção != 5:
    print('''\033[1;33m    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números   
    [5] Sair do programa\033[m''')
    opção = int(input('Qual é sua opção? '))
print('\033[1;37mFim do programa!\033[m')
