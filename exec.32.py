#Custo da viagem
#Desenvolva um programa que pergunta a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
distância=float(input('\033[1;33mQual é a distância da sua viagem?\033[m'))
print('\033[1;34mVocê esta prestes a comecar uma viagem de {} Km!\033[m'.format(distância))
if distância <= 200:
    preço= distância * 0.50
else:
    preço= distância * 0.45
print('\033[1;31mÉ o preço dea sua passagem será de R${:.2f}\033[m'.format(preço))
