#Grupo da Maioridade.
#Crie um programa que leia o ano de nascimento de sete pessoas.
#mostre quantas ainda não atingirama maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
nasc = int(input('\033[1;32mEm que ano a pessoa naceu? \033[m'))
idade = atual -nasc
print('Essa pessoa tem {} anos'.format(idade))
