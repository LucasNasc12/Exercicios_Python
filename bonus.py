p = float(input('Digite o valor do produto: R$ '))
dav = p - (p / 100 * 15)
parc = p + (p / 100 * 15)
print('Para pagamento do valor R${:.2f} a vista você irá pagar R$ {:.2f} com 15% de desconto.'.format(p,dav))
print('Para o pagamento parcelado você irá pagar R$ {:.2f} com 15% de acréssimo.'.format(p, parc))