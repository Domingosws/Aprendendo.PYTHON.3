#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele,lendo o nome dos alunos e escrevendo na telao nome do escolhido.
import random
n1=str(input('\033[1;33mPrimeiro aluno:\033[m'))
n2=str(input('\033[1;34mSengundo aluno:\033[m'))
n3=str(input('\033[1;32mTerceiro aluno:\033[m'))
n4=str(input('\033[1;35mQuarto aluno:\033[m'))
lista=[n1,n2,n3,n4]
escolhido=random.choice(lista)
print('\033[1;31mO aluno escolido foi:\033[m {}'.format(escolhido))#Sorteia