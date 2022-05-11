#Gerenciador de Pagamentos
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format('\033[1;36m LOJA BARATO TODA VIDA \033[m'))
preço = float(input('\033[1;35mpreço das compras: R$\033[m'))
print(''''\033[1;33mFORMAS DE PAGAMENTO.
[ 1 ] Á vista no dinheiro/cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\033[m''')
opção = int(input('\033[1;34mQual é a opção?\033[m'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcelado = total / 2
    print('\033[1;34mSua compra sera pacelada em 2x de {:.2f} SEM JUROS\033[m'.format(parcelado))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas pacelas?'))
    parcela = total / totparc
    print('\033[1;34mSua compra será pacelada em {}x de R${:.2f} COM JUROS.\033[m'.format(totparc, parcela))
else:
    total = preço
    print('\033[1;31mOPÇÃO INVÁLIDA de pagamento. Tente novamente.\033[m')
print('\033[1;35mSua compra de R${:.2f} vai custar R${:.2f} no final.\033[m'.format(preço, total))
