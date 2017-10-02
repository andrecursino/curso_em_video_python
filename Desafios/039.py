nasc = int(input('Insira o ano de nascimento(ex.:1999): '))
alistamento = 2017 - nasc
falta = alistamento - 18

if alistamento == 18:
    print('Tá na hora de se alistar.')
    print('Vai!!')
elif alistamento > 18:
    print('Passou do tempo. Deveria ter feito {} anos atrás.'.format(
        abs(falta)
    ))
elif alistamento < 18:
    print('Ainda vai se alistar. Espere {} anos.'.format(
        abs(falta)
    ))
