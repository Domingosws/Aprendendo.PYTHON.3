# Condições em Pyton(if.elif).
#Aprovando Empréstimo.
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal, não pode execeder 30% do salário ou então o emprestimo sera negado.
casa = float(input('\033[1;32mValor da casa: R$\033[m'))
salário = float(input('\033[1;35mSalario do comprador: R$\033[m'))
anos = int(input('\033[1;34mQuantos anos de finaciamento?\033[m'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('\033[1;36mPara pagar uma casa de R${:.2f} em {} anos\033[m'.format(casa, anos), end =' ')
print('\033[1;37mA prestação será de R${:.2f}\033[m'.format(prestação))
if prestação <= mínimo:
    print('\033[1;33mEmprestimo pode ser CONCEDIDO!\033[m')
else:
    print('\033[1;31mEmprestimo NEGADO!\033[m')
