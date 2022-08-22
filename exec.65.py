#Exercício 64 - Tratando vários valores v1.0
#Crie um programa que leia vários números inteiros pelo teclado. O prograama só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada.
#no final, mostre quantos números foram digitados e qual foi a soma entrw eles(desconsiderando o flag).
núm = cont = soma = 0
núm = int(input('Digigite um número [999 para parar]:'))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digigite um número [999 para parar]:'))
print('Você digitou {} número e a soma entre eles foi {}.'.format(cont, soma))
print('Acabou')
