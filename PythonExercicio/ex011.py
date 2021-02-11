larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg:.2f}x{alt:.2f} e sua area é de {area:.2f}m². ')
tinta = area / 2
print(f'Você vai precisar de {tinta:.2f}l de tinta pra pintar sua parede. ')
