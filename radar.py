print('## RADAR ELETRÔNICO ##')
print('Se o veículo ultrapassar 80km/h será multado em R$ 7,00 por km.')
v = float(input('Informe a velecidade do veículo: '))
m = (v-80) * 7.00
if v > 80:
  print('##### Droga é o Bria #####'.upper())
  print('Você atingiu {}km/h e por isso foi multado em R$ {:.2f}'.format(v, m))
else:
  print('{}km/h está dentro do permitido, continue assim!'.format(v))