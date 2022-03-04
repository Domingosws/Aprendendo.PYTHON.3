#Par ou Impa?
#Crie um programa que leia um número e mostre na tela se ele é Par ou Impar?
número = int(input('\033[1;32mMe diga um numero qualquer:\033[m'))
resultado = número % 2
if resultado == 0:
    print('\033[1;34mO numero {} é Par!\033[m'.format(número))
else:
    print('\033[1;35mO numero {} é Impar!\033[m'.format(número))
