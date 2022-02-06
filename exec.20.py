#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteando.
import random#Metodos dentro de modulos
n1=str(input('Primeiro aluno:'))
n2=str(input('Segundo aluno'))
n3=str(input('Terceio aluno:'))
n4=str(input('Qarto aluno:'))
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será')
print(lista)
