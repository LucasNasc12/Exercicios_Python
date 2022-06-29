import math

ang = float(input('Digite o valor do ângulo: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('Para o ângulo de {}° o seno é {:.2f}'.format(ang, s))
print('O cosseno é {:.2f}'.format(c))
print('E a tangente é {:.2f}'.format(t))