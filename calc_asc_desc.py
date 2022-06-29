p = float(input('Digite o preço: R$ '))
d = float(input('Digite o desconto: '))
a = float(input('Digite o acréscimo: '))
desc = p - (p / 100 * d)
acs = p + (p / 100 * a)
print('O produto que custa R${:.2f}, custará R${:.2f} com {}% de desconto.'.format(p,desc, d))
print('E com o acréscimo de {}%, o produto custará R${:.2f}.'.format(a, acs))

#fazer o calculo com numeros redondos para ter a certeza se a formula está certa. 