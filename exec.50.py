#Tabuada v.2.0
#Refaça o execício 8, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um loço for.
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
