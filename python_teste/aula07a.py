
nome = str(input('Qual o seu nome? '))
print('Prazer em te conhecer {:a<20}!'.format(nome))
# :20 --- 20 espaços
# :>20 --- alinhado à direita
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end=" ")
print('Divisão inteira é {} e a potencia {}'.format(di, e))