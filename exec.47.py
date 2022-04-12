#Estruturas de Repetição.
#Faça um programa que mostre na tela uma contagem regressiva para o estouo de fogos de artifício, indo de 10 até 0
# com uma pausa de 1 segundo entre eles.
from time import sleep # Tempo
for cont in range(10, -1 , -1):# 10 até 0
     print(cont)
     sleep(1.5) # Tempo de contagem.
print('\033[1;34mBUM!\033[m  \033[1;35mBUM!\033[m \033[1;33m BUM! \033[m')
