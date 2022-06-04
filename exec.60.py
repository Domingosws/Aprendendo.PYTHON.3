#Criando um Menu de Opções
#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
n1 = int(input('\033[1;36mPrimeiro valor: '))
n2 = int(input('Segundo valor:\033[m '))
opção = 0
while opção != 5:
    print('''\033[1;33m    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números   
    [5] Sair do programa\033[m''')
    opção = int(input('\033[1;32mQual é sua opção?\033[m '))
    if opção == 1:
        soma = n1 + n2
        print('\33[1;35mA soma entre {} + {} é {}\033[m'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('\033[1;35mO resutado de {} x {} é {}\033[m'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[1;35mEntre {} e {} o maior valor é {}\033[m'.format(n1, n2, maior))
    elif opção == 4:
        print('\033[1;35mInforme os números novamente:\033[m')
        n1 = int(input('\033[1;33mPrimerio valor\033[m'))
        n2 = int(input('\033[1;33mSegundo valor:\033[m'))
    elif opção == 5:
        print('\033[1;35mFinalizado...\033[m')
    else:
        print('\033[1;31mOpção inválida. Tente novamente\033[m')
        print('--'* 10)
print('\033[1;37mFim do programa!\033[m')
