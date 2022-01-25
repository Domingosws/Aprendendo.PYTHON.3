#Crie um programa que leia um número real qual quer pelo teclado e mostre na tela a sua porção inteira.
import math
num = int(input('\033[1;31m Digite um numero? \033[m'))
raiz = math.sqrt(num)
#print('\033[1;34m A raiz de {:.2f} é igual á {:.2f}'.format(num, raiz))
print('\033[1;34m A raiz de {} é igual á {}'.format(num, math.ceil(raiz)))#math.ceil()para redondar pra cima!
