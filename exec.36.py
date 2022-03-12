#Analisando Triângulo
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('\033[35m-*-\033[m'*15)
print('\033[1;34mAnalisando Triângulo\033[m')
print('\033[35m-*-\033[m'*15)
r1 = float(input('\033[1;36mPrimeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:\033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[1;33mOs segmentos acima PODEM FORMAR um TRÂGULO!\033[m')
else:
    print('\033[1;31mOs segmentos acima NÃO PODEM FORMAR um TRÂGULO!\033[m')
