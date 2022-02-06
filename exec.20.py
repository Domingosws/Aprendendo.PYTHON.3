#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteando.
import random#Metodos dentro de modulos
n1=str(input('\033[1;33mPrimeiro aluno:\033[m'))
n2=str(input('\033[1;34mSegundo aluno\033[m'))
n3=str(input('\033[1;32mTerceio aluno:\033[m'))
n4=str(input('\033[1;35mQarto aluno:\033[m'))
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print('\033[1;31mA ordem de apresentação será:\033[m')
print(lista)
