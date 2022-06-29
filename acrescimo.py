s = float(input('Digite seu salário: R$ '))
#a = s + (s /100 * 15)
a = s + (s * 15 / 100)
print('O funcionário com salário R${:.2f}, vai receber R${:.2f} com aumento de 15%.'.format(s,a))