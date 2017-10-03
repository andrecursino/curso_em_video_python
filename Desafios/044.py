preco_prod = float(input('Qual o preço do produto? '))
cond_pag = int(input('Como o pagamento será feito:\n'
                     '1 - Pagamento à vista\n'
                     '2 - Pagamento à prazo\n'
                     ''))

if cond_pag == 1:
    print('Pagamento a vista, como será feito? ')
    avista = int(input('1 - Dinheiro/Cheque\n'
                       '2 - Cartão\n'
                       ''))
    if avista == 1:
        print('O valor total para pagamento em dinheiro ou cheque ficará'
              'R${:.2f}'.format(preco_prod - (preco_prod * 0.1)))
    elif avista == 2:
        print('O valor total para pagamento em cartão ficará'
              'R${:.2f}'.format(preco_prod - (preco_prod * 0.05)))
elif cond_pag == 2:
    vezes = int(input('Pagamento à prazo, fará em quantas vezes? '))
    if vezes <= 2:
        print('O preço total em {}x no cartão será R${:.2f}.'.format(
            vezes, preco_prod
        ))
    else:
        print('O preço total em {}x no cartão será R${:.2f}.'.format(
            vezes, preco_prod + (preco_prod * 0.2)
        ))