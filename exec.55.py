#Grupo da Maioridade.
#Crie um programa que leia o ano de nascimento de sete pessoas.
#mostre quantas ainda não atingirama maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('\033[1;32mEm que ano a {} pessoa naceu?\033[m'.format(pess)))
    idade = atual -nasc
    if idade >= 21:
        totmaior += 1
        print('\033[1;32mEssa pessoa tem {} anos!\033[m'.format(idade))
    else:
        tomamenor += 1
        print('\033[1;32mEssa pessoa é menor\033[m')
print('\033[1;32mAo todo tivemos {} pessoas maiores de idade\033[m'.format(totmaior))
print('\033[1;32mE tambem tivermos {} pessoas menores de idade\022[m'.format(totmenor))
