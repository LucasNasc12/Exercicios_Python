from time import sleep
print('### aumento de salário ###'.upper())
s = float(input('Informe seu salário: '))
a10 = s + (s * 10 / 100)
a15 = s + (s * 15 / 100)
print('CALCULANDO...')
sleep(3)
if s > 1250.00:
  print('Seu salário é R${:.2f}, e com 10% de aumento você receberá R${:.2f}.'.format(s, a10))
else:
  s <= 1250.00
  print('Seu salário é R${:.2f}, e com 15% de aumento você receberá R${:.2f}.'.format(s, a15))