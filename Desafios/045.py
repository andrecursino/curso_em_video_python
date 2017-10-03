from random import randint
minha_vez = int(input('Escolha\n'
                      '1 - pedra\n2 - papel\n3 - tesoura\n'))
vez_pc = randint(1,3)

if vez_pc == 1:
    if minha_vez == 1:
        print('O computador jogou pedra, empate!')
    elif minha_vez == 2:
        print('O computador jogou pedra, você ganhou!')
    elif minha_vez == 3:
        print('O computador jogou pedra, você perdeu!')
elif vez_pc == 2:
    if minha_vez == 1:
        print('O computador jogou papel, você perdeu!')
    elif minha_vez == 2:
        print('O computador jogou papel, empate!')
    elif minha_vez == 3:
        print('O computador jogou papel, você ganhou!')
elif vez_pc == 3:
    if minha_vez == 1:
        print('O computador jogou tesoura, você ganhou!')
    elif minha_vez == 2:
        print('O computador jogou tesoura, você perdeu!')
    elif minha_vez == 3:
        print('O computador jogou tesoura, empate!')
