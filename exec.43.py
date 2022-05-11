#Analisando Triângulos v2.0
#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes
r1 = float(input('\033[1;34mPrimeiro segmento: \033[m'))
r2 = float(input('\033[1;34mSegundo segmento: \033[m'))
r3 = float(input('\033[1;34mTerceiro segmento: \033[m'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('\033[1;34mOs segmentos acimam PODEM FARMAR um triagulo\033[m', end=' ')
    if r1 == r2 == r3:
        print('\033[1;36mEQUILATERO!\033[m')
    elif r1 != r2 != r3!= r1:
        print('\033[1;36mESCALENO!\033[m')
    else:
        print('\033[1;36mISÓSCELES\033[m')
else:
    print('\033[1;31mOs segmentos acima NÃO PODEM FORMA um triagulo\033[m')
