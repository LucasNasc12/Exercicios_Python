saldo = float(input('Digite seu saldo: R$ '))
moeda = float(input('Digite o valor atual da moeda: ')
print('Com R$ {:.2f}, você pode comprar US$ {:.2f}.'.format(saldo, (saldo / moeda)))#dol
print('E pode comprar £ {:.2f}'.format(saldo / 5.69)) #euro
#print('Com R$ {:.2f}, você pode comprar US${:.2f}.'.format(saldo, (saldo * moeda)))