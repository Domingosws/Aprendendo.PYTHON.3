#fibonacci v1.0
#Escreva um programa que leia um número Ninteiro qualquer e mostre na tela os N pro[imeiros elementos de uma sequência de
#Fibonacci.Exemplo: 0-1-1-2-3-5-8

print('-'*30)
print('Sequência de fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} ➮ {}'.format(t1, t2), end='')
cont =3
while cont <= n:
    t3 = t1 + t2
    print(' ➮ {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ➮ FIM')
