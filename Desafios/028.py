from random import randint
from time import sleep
num = int(input('Insira um número de 0 a 5: '))
numpc = randint(0, 5) #pc pensa entre 0 e 5
print('PROCESSANDO...')
sleep(3) #aguarda 3sec antes do proximo comando
if num == numpc:
    print('Acertou Miseravi!')
else:
    print('Não foi dessa vez :( ')
print('O número sorteado foi {}'.format(numpc))
