r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))
if (r1 - r2) < r3 < (r1 + r2) and (r2 - r3) < r1 < (r2 + r3) and (
            r3 - r1) < r3 < (r3 + r1):
    print('Dá pra fazer um triangulo!')
else:
    print('Não dá pra fazer')