#Índice de Massa Corporal
#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa passoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÊNS, você está na faixa de peso NORMAL')
elif 25<= imc < 30:
    print('Você está em SOPREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >=40:
    print('Você está em OBESIDADE MÓRBIDA, CUIDADO!')
