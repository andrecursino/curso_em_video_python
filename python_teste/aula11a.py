print('\033[1;31;43mola mundo\033[m')
print('\033[4;30;45mola mundo\033[m')
print('\033[0;33;44molá mundo\033[m')
a = 3
b = 5
print('\033[32m{}\033[m e \33[31m{}\033[m'.format(a, b))
nome = 'Andre'
print('olá, {}{}{}'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretobranco' : '\033[7;30m'}
print('ola, {}{}{}'.format(cores['azul'], nome, cores['limpa']))
print('ola, {}{}{}'.format(cores['pretobranco'], nome, cores['limpa']))
