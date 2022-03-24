#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import date
atual = date.today().year
nasc = int(input('\033[1;32mAno de nacimento: \033[m'))
idade = atual - nasc
print('\033[1;33mQuem naceu em  {} tem {} anos em {}. \033[m'.format(nasc, idade, atual))
if idade == 18:
    print('\033[1;35mVocê tem que se alistar\033[m \033[1;4;31mIMEDIATAMENTE!\033[m')
elif idade < 18:
    saldo = 18 - idade
    print('\033[1;36mAida faltam {} anos para se o alistamento.\033[m'.format(saldo))
    ano = atual + saldo
    print('\033[1;34mSeu alistamento será em {} ano.\033[m'.format(ano))
elif idade > 18:#Poderia ser também -> else:
    saldo = idade - 18
    print('\033[1;37mVocê ja deveria ter se alistado há {}. \033[m'.format(saldo))
    ano = atual - saldo
    print('\033[1;34mSeu alistamento foi em {}. \033[m'.format(ano))
