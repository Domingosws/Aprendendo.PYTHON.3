#Ano bissexto
#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano=int(input('\033[1;33mQue ano quer analizar?\033[m\033[1;4;33m Ou coloca 0 para analizar o ano atual:\033[m'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('\033[1;34mO ano {} é BISSESTO!\033[m'.format(ano))
else:
    print('\033[1;31mO ano {} NÃO é BISSESTO!\033[m'.format(ano))
