# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    jogador = int(input('\033[1;34mDiga um valor:\033[m'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo =''
    while tipo not in 'Pp Ii':
        tipo = str(input('Par ou Impar?')).strip().upper()[0]
    print(f'\033[1;34mVoce jogou {jogador} e o computador {computador}. total de {total} ', end='')
    print('Deu  PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('\033[1;34mVamos jogar novamente...')
    print(f'GAME OVER! Você venceu {v} vezes.\033[m')


