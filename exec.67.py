#INTERROMPENDO REPETIÇÕES WHILE
#Nessa aula, vamos  aprender como utilizar a instrução break e os loopings infinitos a favor das nossas estratégias de código.
#É muito importante saber usar o break no Pyton,já que em alguns casos precisamos interromper um laço no caminho.
#Além disso, vamos aprender como trabalhar com as novas fstrngs do pyth
n= s =0
while True:
    n=int(input('digite um numero'))
    if n == 999:
        break
    s += n
print(f'a soma {s} {n}')