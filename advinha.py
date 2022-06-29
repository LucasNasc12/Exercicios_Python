from random import randint
from time import sleep
pc = randint(0, 10 )
print('Tente advinhar em que numero eu pensei!')
print('Vou pensar em um numero entre 0 e 10...')
n = int(input('Você pensou no numero: '))
print('Processando...')
sleep(5)
if n == pc:
  print('Parabéns você ganhou!')
else:
  print('Que pena você perdeu! Eu pensei no numero {}'.format(pc))