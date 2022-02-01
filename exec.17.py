#Seno, cosseno e tangente
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, e tangente desse ângulo.
import math
ângulo=float(input('\033[1;31m Digite o ângulo que você deseja:\033[m'))
seno=math.sin(math.radians(ângulo))
print('\033[1;36m O angulo de {} tem o SENO de {:.2f}'.format(ângulo,seno))
cosseno=math.cos(math.radians(ângulo))
print('O ângulo de {}tem o COSENO de {:.2f}'.format(ângulo,cosseno))
tangente=math.tan(math.radians (ângulo))
print('O ãngulo de {} tem a TANGENTE de {:.2f}\033[m'.format(ângulo,tangente))