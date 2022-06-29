d = int(input('Informe por quantos dias o carro foi alugado: '))
km = float(input('Informe quantos km foram percorridos: '))
pgto = (d * 60) + (km * 0.15)
print('O valor a ser pago pelo aluguel do carro é: R$ {:.2f}'.format(pgto))