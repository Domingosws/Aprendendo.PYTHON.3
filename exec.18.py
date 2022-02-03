#Continuaçãodo execicio 17
#Usando inportação
from math import  radians,sin,cos,tan
ângulo = float(input('\033[1;33mDigite o angulo que você deseja:\033[m'))
seno = sin(radians(ângulo))
print('\033[1;34mO ãngulo de {} tem o SENO de {:.2f}'.format(ângulo,seno))
cosseno = cos (radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo,cosseno))
tangent = tan(radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}\033[m'.format(ângulo, tangent))

