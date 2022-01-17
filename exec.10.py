#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua ária e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta
#litro de tinta, pinta uma aréa de 〖2m〗^2.
larg = float(input('\033[1;34m Larguara da parede:'))
alt = float(input('Altura da parede:'))
área = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área ´é de {}〖2m〗^2.'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, voçê precisará de {} l de tinta.'.format(tinta))