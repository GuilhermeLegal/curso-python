n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
su = n1 - n2
print('A soma é {} o produto é {:.1f} e a divisão é {}'.format(s, d, di), end=' ')
print('A divisão inteira É {} subtração {} e potencia {}'.format(di, su, e))
