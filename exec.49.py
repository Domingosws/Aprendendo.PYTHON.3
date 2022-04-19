#Soma ímpares múltiplos de três.
#faça um programa que calcule a soma entre todos os numeros que são mútiplos de trê eque se encantram no intevalo de 1 até 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os valores {} solicitados é {}'.format(cont, soma))
