#Maior e menor valores
#Faça um programaa que leia três numeros e mostre qual é o maior e qual é o menor.
a=int(input('\033[1;32mPrimeiro valor:'))
b=int(input('Segundo valor:'))
c=int(input('Terceiro valor:\033[m'))
#Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('\033[1;31mO menor valor digitado foi {}\033[m'.format(menor))
#verificando quem é maior
maior = a
if b>a and a>c:
    maior = b
    
