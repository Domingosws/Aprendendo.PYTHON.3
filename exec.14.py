#Excreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quis ele foi alugado.
#Clcule o preço a pagar. Sabendo que  o carro custa R$ 0,15 por Hm rodado.
dias = int(input('\033[1;35m Quantos dias alugados?'))
km = float(input('Quantos Km rodado? \033[m '))
pago = (dias * 60)+(km * 0.15)
print('\033[1;36m O toal a pagar é de {:.2f}'.format(pago))
