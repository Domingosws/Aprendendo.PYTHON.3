#Primeira e ultima ocorrência de uma String
#faça 8um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a premeira vez e em que posição ela aparece a ultíma vez.
frase=str(input('\033[1;31mDigite uma frase:')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')))
print('A ultima letra A apareceu na posição {}.\033[m'.format(frase.rfind('A')+1))#rfind -> procure aparte do lado direito
