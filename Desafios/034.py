sal = float(input('Qual o salario? '))
if sal > 1250.00:
    print('Aumento de 10%. Total: R${:.2f}'.format(sal + (sal * 0.10)))
else:
    print('Aumento de 15%. Toral: R${:.2f}'.format(sal + (sal * 0.15)))
