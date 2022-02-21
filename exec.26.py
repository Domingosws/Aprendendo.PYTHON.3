#primeiro e último nome de uma pessoa.
#Faça um programa que leia o nome completo de uma pessoa , mostrando em Seguida o primeiro e o último nome separadamente.
n=str(input('\033[7;30;44mDigite seu nome completo:\033[m'))
nome=n.split()
print('\033[1;36m muito prozer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}\033[m'.format(nome))