#Execício 37 conversor de bases de numéricas
#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
#conversão: 1 para binario, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida. Tente novamente.')
