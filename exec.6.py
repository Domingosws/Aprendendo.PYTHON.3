#Desenvolva um programa que leia as duas notas de um aluno, calculae e mostre a sua média .
n1 = float(input('\033[1;36m Primeira nota do aluno:'))
n2 = float(input('Segunda nota do aluno: \033[m'))
média = (n1+n2) /2
print('\033[1;35m A média entre {:.1f} é {:.1f} é igual a {:.1f}'.format(n1, n2, média))
