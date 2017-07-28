#litros por metro
h = float(input('Qual altura da parede? '))
l = float(input('Qual a largura da parede? '))
a = h * l
print('Será necessário {0:,.2f} litros de tinta.'.format(a/2))