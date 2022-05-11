#Índice de Massa Corporal
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
peso = float(input('\033[1;32mQual é seu peso? (Kg)\033[m'))
altura = float(input('\033[1;32mQual é sua altura? (m)\33[m'))
imc = peso / (altura ** 2)
print('\033[1;37mO IMC dessa pessoa é de {:.1f}\033[m'.format(imc))
if imc < 18.5:
    print('\033[1;31mVocê está ABAIXO DO PESO normal\033[m')
elif 18.5 <= imc < 25:
    print('\033[1;37mPARABÊNS, você está na faixa de peso NORMAL\033[m')
elif 25<= imc < 30:
    print('\033[1;37mVocê está em SOPREPESO\033[m')
elif 30 <= imc < 40:
    print('\033[1;37mVocê está em OBESIDADE!\033[m')
elif imc >=40:
    print('\033[1;31mVocê está em OBESIDADE MÓRBIDA, CUIDADO!\033[m')
