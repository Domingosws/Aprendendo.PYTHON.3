#soma dos pares
#mostre a soma apenas daqueles que forem pares.Se o valor digitado for impar,desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} números e a soma foi {}'.format(cont, soma))
