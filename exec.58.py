#Repetições em Python (while)
#Validação de Dados
#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('\033[1;34mInforme seu sexo: [M/F]\033[m')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por  favor, informe seu sexo ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
