#verificando as primeiras letras de um texto.
#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cid=str(input('\033[1;32mEm que cidade você naceu?')).strip()
print(cid[:5].upper()=='SANTO\033[m')