#Detector de Palíndromo
#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
frase = str(input('\033[1;32mDigite uma frase: \033[m')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('\033[1;32mTemos um palíndromo!\033[m')
else:
    print('\033[1;32mA frase digitada não é um palindromo!\033[m')
