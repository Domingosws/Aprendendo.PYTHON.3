# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.
media = float(input('Uma distacia em metros:'))
cm = media * 100
mm = media * 1000
print('A media de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(media, cm, mm))
