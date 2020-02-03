x'km = float(input('Quantos km foram rodados com o carro ?'))
dias = int(input('Quantos dias o carro foi alugado ?'))
preço = dias*60 + km*0.15
print('O preço a ser pago pelo carro alugado por {} dias e rodado {}km será de R${}'.format(dias, km, preço))
