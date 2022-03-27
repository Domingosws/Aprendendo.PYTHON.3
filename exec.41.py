#Aquele clássico da Média
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
nota1 = float(input('\033[1;32mPrimeira nota:\033[m'))
nota2 = float(input('\033[1;32mSegunda nota:\033[m'))
média = (nota1 + nota2) / 2
print('\033[1;35mTirando {:.1f} e {:.1f}, a média do aluno é {:.1f}\033[m'.format(nota1, nota2, média))
if média >=5 and média < 7:# Ou if 7 > media >=5:
    print('\033[1;31mO aluno está em RECUPERAÇÃO.\033[m')
elif média <=5:
    print('\033[1;31mO aluno está REPROVADO\033[m')
else: #Ou elif média > = 7:
    print('\033[1;34mO aluno está APROVADO.\033[m')
