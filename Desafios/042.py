r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Dá pra fazer um triangulo!')
    if r1 == r2 == r3:
        print('Um triangulo equilátero')
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1:
        print('Um triangulo isosceles.')
    elif r1 != r2 !=r3:
        print('Um triangulo escaleno')
else:
    print('Não dá pra fazer')