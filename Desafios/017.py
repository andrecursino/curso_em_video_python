#Calcular hipotenusa
from math import hypot
catop = float(input('Insira o cateto oposto: '))
catadj = float(input('Insira o cateto adjacente: '))
print('Dado o cateto oposto {} e o cateto adjacente {} o valor da '
      'hipotenusa é {:.2f}'.format(catop, catadj, hypot(catop, catadj)))
