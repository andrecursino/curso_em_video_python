from datetime import date
ano = int(input('Insira o ano(ou coloque 0 para o ano atual): '))
if ano == 0:
    ano = date.today().year #ano da máquina.
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('{} é bissexto.'.format(ano))
else:
    print('{} não é bissexto.'.format(ano))