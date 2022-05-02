#Detector de Palíndromo
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
frase = str(input('\033[1;32mDigite uma frase: \033[m')).strip().upper()# Lendo a frase.
palavras = frase.split()#Aqui foi separado em um  vetor -> numa lista.
junto = ''.join(palavras)#Aqui eu juntei tudo numa so string.
inverso = ''# 2 forma pode tira isso!
inverso = junto[::-1]#2 forma.
"""for letra in range(len(junto) -1, -1, -1):#Aqui foi feito o inverso dela.
    inverso += junto[letra]"""#Outra forma de fazer é o de fatiamento.
print('\033[1;32mO inverso de {} é {}\033[m'.format(junto, inverso))
if inverso == junto:
    print('\033[1;32mTemos um palíndromo!\033[m')
else:
    print('\033[1;32mA frase digitada não é um palindromo!\033[m')
