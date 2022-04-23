#Progressão Aritmética
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No
#final, mostre os 10 primeros termos dessa progreção.
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo= primeiro + (10 - 1) * razão
for c in range(primeiro, décimo, razão):
    print('{}'.format(c), end=' ➪ ')
print('ACABOU')
