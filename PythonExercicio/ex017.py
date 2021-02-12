from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(ca, co)
print(f'A hipotenusa vai medir {hi:.2f} !')
