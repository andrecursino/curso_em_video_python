nome = str(input('Coloque o seu nome inteiro: '))
dividido = nome.split()
print('O seu nome com todas as letras maiúsculas: {}'.format(
    nome.upper()
))
print('Com todas as letras minuscúlas:{} '.format(
    nome.lower()
))
print('Ele tem {} letras'.format(
    len(nome.strip()) - nome.count(' ')
))
print('Comprimento primeiro nome: {}'.format(
    len(dividido[0])
))
print('Comprimento primeiro nome {}'.format(nome.find(' ')))