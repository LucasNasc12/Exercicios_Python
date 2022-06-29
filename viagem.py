from time import sleep
print('Quanto sua viagem irá custar? ')
d = float(input('Informe quantos km serão percorridos: '))
print('Até 200km será cobrado R$0,50 por km, e acima de 200km R$0,45 por km.')
p = d * 0.50 #ate 200 km
p2 = d * 0.45 #acima de 200km
print('Calculando...')
sleep(3)
if d <= 200:
  print('Serão percorridos {:.2f}km, então sua passagem custará R$ {:.2f}'.format(d, p))
else:
  print('Serão percorridos {:.2f}km, então sua passagem custará R$ {:.2f}'.format(d, p2))
