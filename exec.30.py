#Rada eletrônico
#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/l, mostre uma mensagem dizendo que ele foi multato vai custar R$7,00 por cada Km acima do limite.
velocidade=float(input('\033[1;36mQual é a velocidade atual do carro?\033[m'))
if velocidade>80:
    print('\033[1;31mMULTADO! Você execeu o limite permitido que é de 80Km/h')
    multa=(velocidade-80)*7
    print('você deve pagar uma multa de R${:.2f}!\033[m'.format(multa))
print('\033[1;36mTenha um bom dia! Dirija com segurança!\033[m')
