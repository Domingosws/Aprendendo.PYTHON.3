#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n=int(input('\033[1;33mDigite um numero:'))
d=n*2
t=n*3
r=n**(1/2)
print('\033[m \033[1;34m O dobro de {} vale {},'.format(n, d))
print('O triplo de {} vale {},A raiz quadrada de {} é igual a {:.2f}'.format(n,t,n,r))