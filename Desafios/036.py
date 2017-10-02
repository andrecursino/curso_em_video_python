valor_casa = int(input('Qual o valor da casa? '))
salario = int(input('Qual o seu salário? '))
anos = int(input('Pretende pagar em quantos anos? '))

prestacao_mensal = valor_casa / (anos * 12)

if prestacao_mensal < (salario * 0.3):
    print('Emprestimo concedido')
    print('Com uma prestação mensal de R${0:.2f}.'.format(prestacao_mensal))
else:
    print('Emprestimo negado')

