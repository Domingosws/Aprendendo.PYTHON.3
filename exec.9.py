#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e motre quantos Dólares ela pode comprar. Considere US $100 = R$5.53
real = float (input('\033[1;32m Quanto dinheiro voçê tem na carteira? R$'))
dolar = real / 5.53
print('Com R${:.2f} Voçê pode comprar US${:.2f}'.format(real, dolar))
