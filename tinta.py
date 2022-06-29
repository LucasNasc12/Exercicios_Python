larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
t = area / 2
print('A parede com {:.2f} de largura x {:.2f} de altura tem {:.2f}m²'.format(larg, alt, area))
print('E precisa de {:.2f} l de tinta para a pintura.'.format(t))