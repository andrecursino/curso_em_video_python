#converter metros em cm e mm
n = float(input('Coloque o valor a ser convertido: '))
print('O valor em centímetros é {} cm, e em milimetros é {} mm.'.format(
    int(n*100), int(n*1000)
))