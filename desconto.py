p = float(input('Digite o valor do produto: R$ '))
#d = p - (p / 100 * 5)
d = p - (p * 5 / 100)
# as duas formulas estão corretas 
print('O produto no valor de R$ {:.2f} com 5% de desconto custará R$ {:.2f}.'.format(p,d))