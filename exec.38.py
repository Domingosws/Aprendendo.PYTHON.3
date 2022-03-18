#Execício 37 conversor de bases de numéricas
#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
#conversão: 1 para binario, 2 para octal e 3 para hexadecimal.
num = int(input('\033[1;34mDigite um número inteiro:\033[m'))
print('''\033[1;37mEscolha uma das bases para conversão:\033[m\033[1;33m
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL\033[m''')
opção = int(input('\033[1;31mSua opção:\033[m'))
if opção == 1:
    print('\033[1;34m{} Convertido para BINÁRIO é igual a {}\033[m'.format(num, bin(num)[2:]))
elif opção == 2:
    print('\033[1;34m{} Convertido para OCTAL é igual a {}\033[m'.format(num, oct(num)[2:]))
elif opção == 3:
    print('\033[1;34m{} Convertido para HEXADECIMAL é igual a {}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[1;31mOpção invalida. Tente novamente.\033[m')
