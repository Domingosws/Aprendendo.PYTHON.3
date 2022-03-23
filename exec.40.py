#Faça um programa que leia o nacimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistarao serviço militar, se é a hora exata de se alista ou se já passou do tempo do alistamento. Seu programa também
# deverá mostra o tempo que flata ou que passou do prazo.
from datetime import date
atual = date.today().year
nasc = int(input('\033[1;32mAno dae nacimento:\033[m'))
idade = atual - nasc
print('\033[1;33mQuem nasceu em {} tem {} ano em {}\033[m'.format(nasc, idade, atual))
if idade == 18:
    print('\033[1;34mVocê tem que se alistar INEDIATAMENTE!\033[m')
elif idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu aleistamento será em {}'.format(ano))
elif idade > 18:  # poderia ser também -> else:
    saldo = idade - 18
    print('\033[1;31mvocê ja deveria ter se alistado ha {} anos\033[m'.format(saldo))
    ano = atual - saldo
    print('\033[1;37mSeu alistamento foi em {}\033[m'.format(ano))
