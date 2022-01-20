#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo Salálario 15% de aumento.
salário = float(input('\033[1;34m Qual é o seu salário do Funcionario? R$'))
novo = salário + (salário * 15/100)
print('Um funcionario que ganhava R${:.2f},com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))