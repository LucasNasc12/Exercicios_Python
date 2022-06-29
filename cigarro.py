c = int(input('Informe quantos cigarros você fuma por dia: '))
a = int(input('Informe a quantos anos vocês fuma: '))
temp = a * 365 * c * 10
d = temp / (24*60)
print('Um fumante que fuma {} cigarros por dia, a {} dias perde {:.2} anos de vida.'.format(c, a, d))