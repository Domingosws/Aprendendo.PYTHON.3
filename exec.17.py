#Seno, cosseno e tangente
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, e tangente desse ângulo.
import math
ângulo=floot(input('Digite o ângulo que você deseja:'))
seno=math.sin(math.radians(ângulo))
print('O angulo de {} tem o SENO de {}'.format(angulo,seno))
cosseno=math.cos(math.radians(ângulo))
print('O ângulo de {}tem o COSENO de {}'.format(ângulo,cosseno))
tangente=