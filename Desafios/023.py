num = input('Digite um numero de 0 a 9999: ')

print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(num[-1:], num[-2:-1], num[-3:-2], num[-4:-3]))
