#Analizandor de textos 
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#-o nome com todas as letras ,aiusculas e minúsculas.
#-Quantas letras ao todo (sem considerar espaços).
#-Quantas letras tem o primeiro nome.
nome = str(input('\033[1;33mDigite seu nome completo:')).strip()
print('Analisando seu nome...\033[m')
print('\033[1;35mSeu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {}'.format(len(nome) - nome.count(' ')))
#print('Seu nome tem {} letras'.format(nome.find(' ')))
separa=nome.split()#Segunda maneira de fazer!
print('Seu primeiro nome é {} ele tem {} letras'.format(separa[0],len(separa[0])))
