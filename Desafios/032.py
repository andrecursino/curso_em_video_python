ano = int(input('Insira o ano: '))
if ano%4 == 0:
    print('{} é bissexto.'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))