#Cateto e hipotenusa
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de uma triângulo retângulo.
#  Calcle e mostre o compremento da hipotemusa.
co = float (input('\033[1;34m Comprimento do cateto oposto:\033[m'))
ca = float (input('\033[1;33m Comprimento do cateto adiacente\033[m:'))
hi = (co ** 2 + ca ** 2)**(1/2)
print('\033[1;31m A hipotenusa vai medir: {:.2f} \033[m'.format(hi))
