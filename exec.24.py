#Procurando uma String dentro de outra.
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('\033[1;34mQual é seu nome completo?')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome))
