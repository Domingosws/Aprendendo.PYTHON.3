# INTERROMPENDO REPETIÇÕES WHILE
# Nessa aula, vamos aprender como utilizar a instrução break e os ‘loopings’ infinitos a favor das nossas estratégias de código.
# É muito importante saber usar o break no Pyton, já que em alguns casos precisamos interromper um laço no caminho.
# Além disso, vamos aprender como trabalhar com as novas fstrngs do python.

# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que
# é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)

n = s = cont = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A soma {cont} valores foi {s}.')
