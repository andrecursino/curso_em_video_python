num_inteiro = int(input('Insira um número: '))
decisao = int(input('Qual sera sua base de conversão:\n'
                    '1 - para binário\n'
                    '2 - para octal\n'
                    '3 - para hexadecimal\n'
                    ''))
if decisao == 1:
    print('O numero {} em binário ficará {}.'
          .format(num_inteiro, bin(num_inteiro)))
elif decisao == 2:
    print('O número {} em octal ficará {}.'
          .format(num_inteiro, oct(num_inteiro)))
elif decisao == 3:
    print('O número {} em hexadecimal ficara {}'
          .format(num_inteiro, hex(num_inteiro)))
