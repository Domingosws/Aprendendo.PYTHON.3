# Condições em Pyton(if.elif).
#Aprovando Empréstimo.
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal, não pode execeder 30% do salário ou então o emprestimo sera negado.
casa = float(input('Valor da casa: R$'))
salário = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de finaciamento?'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end =' ')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Emprestimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
