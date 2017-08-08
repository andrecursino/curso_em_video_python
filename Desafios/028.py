from random import randint
num = int(input('Insira um número de 1 a 5: '))
numpc = randint(1, 5)

if num == numpc:
    print('Acertou Miseravi!')
else:
    print('Não foi dessa vez :( ')
print('O número sorteado foi {}'.format(numpc))
