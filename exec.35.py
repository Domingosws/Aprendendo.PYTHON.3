#Aumento múltipos
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para sálários superioresa R$ 150.00, calcule um aumento de 10% para os inferiores ou iguais, o aumento é de 15%.
salário = float(input('\033[1;34mQual é o seu salário do funcionario? R$\033[m'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('\033[1;35mQuem ganhava R${:.2f} passa a ganhar R${:.2f} agora.\033[m'.format(salário, novo))
