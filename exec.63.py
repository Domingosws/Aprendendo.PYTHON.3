#Super Progressão Aritmética v3.0 Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
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
print('FIM !')
