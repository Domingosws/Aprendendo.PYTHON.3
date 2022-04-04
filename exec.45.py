#Gerenciador de Pagamentos
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJA BARATO TODA VIDA '))
preço = float(input('preço das compras: R$'))
print(''''FORMAS DE PAGAMENTO.
[ 1 ] Á vista no dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcelado = total / 2
    print('Sua compra sera pacelada em 2x de {:.2f}.'.format(parcelado))
elif opção == 4:
    total = preço + (preço * 20 / 100)
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
