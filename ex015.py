dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos KM foram rodados com o carro? '))
valor = ( dias * 60 ) + ( km * 0.15 )
print('O total a pagar é R${:.2f}.'.format(valor))