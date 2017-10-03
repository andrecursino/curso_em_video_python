peso = float(input('Qual o peso, em kg (ex.:70.4): '))
alt = float(input('Qual sua altura em metros (ex.:1.90): '))
imc = peso / (alt * alt)

if imc < 18.5:
    print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
