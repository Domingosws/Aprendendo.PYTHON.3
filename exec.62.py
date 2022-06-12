#Progressão Aritmética v2.0
#lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while
print('   Gerador de PA')
print('☆' * 15)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} ➮ '.format(termo), end='')
    termo += razão
    cont += 1
