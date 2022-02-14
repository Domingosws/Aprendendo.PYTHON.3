#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num=int(input('\033[1;34mInforme um numero:\033[m'))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 100 % 10
print('\033[1;36mAnalizado o número {}\033[m'.format(num))
print('\033[1;33mUnidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('centena:{}'.format(c))
print('Milhar:{}\033[m'.format(m))
