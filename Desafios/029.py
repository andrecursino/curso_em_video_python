vel = int(input('Qual a velocidade do carro: '))
if vel > 80:
    print('Você está acima da velocidade permitida')
    print('Multa R$7,00 por Km acima do limite, total: R${}'
          .format(7.00 * (vel - 80)))
else:
    print('Você está dentro do limite.')