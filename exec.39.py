#Comparado números
#Escreva um programa que leia dois numeros inteiros e compare - os mostrando na tela uma mensagem:
#Oprimeiro valor é maior
#O Segundo valor e maior
#Não existe valor maior, os dois são iguais
n1 = int(input('\033[1;34mPrimeiro número:\033[m'))
n2 = int(input('\033[1;33mSegundo número:\033[m'))
if n1 > n2:
    print('\033[1;34mO PRIMEIRO valor é maior\033[m')
elif n2 > n1:
    print('\033[1;33mO SEGUNDO valor é maior\033[m')
else:
    print('\033[1;4;31mOs dois valores são IGUAIS\033[m')
