#Números primos
#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
núm = int(input('Digite um numero: '))
for c in range(1, núm +1):
    if núm % c == 0:
        print('\033[1;34m')
    else:
    print('\033[m')
print('{}'.format(c), end ='')