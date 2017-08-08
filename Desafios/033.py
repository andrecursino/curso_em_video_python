n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('{} é o numero maior.'.format(n1))
    if n2 > n3:
        print('{} é o menor numero.'.format(n3))
    else:
        print('{} é o menor número'.format(n2))
if n2 > n1 and n2 > n3:
    print('{} é o maior número.'.format(n2))
    if n1 > n3:
        print('{} é o menor número.'.format(n3))
    else:
        print('{} é o menor número.'.format(n1))
if n3 > n1 and n3 > n2:
    print('{} é o maior número.'.format(n3))
    if n1 > n2:
        print('{} é o menor número.'.format(n2))
    else:
        print('{} é o menor número.'.format(n1))