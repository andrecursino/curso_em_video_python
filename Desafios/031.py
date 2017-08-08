dist = float(input('Qual a distância da viagem: '))
if dist <= 200:
    print('O valor dessa viagem será R${:.2f}, sendo R$0,50 por Km'.
          format(dist * 0.5))
else:
    print('O valro da viagem será R${:.2f}, sendo R$0,45 por Km.'
          .format(dist * 0.45))
