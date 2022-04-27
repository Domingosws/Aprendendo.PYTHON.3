#Números primos
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
núm = int(input('\033[1;33mDigite um numero: '))
tot = 0# Pra saber o numero de divisives
for c in range(1, núm +1):
    if núm % c == 0:
        print('\033[1;35m', end='')#Valores divisives
        tot += 1
    else:
        print('\033[1;34m', end='')# Valores não divisives
    print('{} '.format(c), end ='')
print('\n\033[1;32mO numero {} foi divisísel {} veses'.format(núm, tot))
if tot==2:
    print('\033[1;36mE por isso ele É PRIMO!\033[m')
else:
    primo('\033[1;31mE por isso ele NÃO É PRIMO!\033[m')