nasc = int(input('Qual o ano (ex.:1999) de nascimento do atleta? '))
idade = 2017 - nasc

if idade <= 9:
    print('Categoria mirim')
elif idade <= 14:
    print('Categoria infantil')
elif idade <= 20:
    print('Categoria Sênior')
elif idade > 20:
    print('Categoria Master')

