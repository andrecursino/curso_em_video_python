nasc = int(input('Insira o ano de nascimento(ex.:1999): '))
alistamento = 2017 - nasc

if alistamento == 18:
    print('Tá na hora de se alistar.')
elif alistamento > 18:
    print('Passou do tempo.')
elif alistamento < 18:
    print('Ainda vai se alistar.')
