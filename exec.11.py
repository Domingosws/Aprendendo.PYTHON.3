#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço.com 5% de desconto.
preço = float(input('\033[1;33mQual é o preço do produto? R$\033[m'))
novo = preço - (preço * 5 / 100)
print('\033[1;34mO produto que custa R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))