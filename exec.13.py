# Escreva um programa que coverta uma temperatura digitada em °C e converta para °F.
c = float(input('\033[1;33m Informe a temperatura em °C:\033[m'))
f = ((9 * c) / 5 ) + 32
print('\033[1;34m A temperatura de {}°C correspode a {}°F!'.format(c, f))