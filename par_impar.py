from time import sleep
print('par ou ímpar'.upper())
n = int(input('Digite um numero e direi se é par ou ímpar: '))
r = n % 2
#lista = [0,2,4,6,8,10]
print('Processando....')
sleep(3)
if r == 0:
  print('O numero {} é par!'.format(n))
else:
  print('O numero {} é ímpar'.format(n))