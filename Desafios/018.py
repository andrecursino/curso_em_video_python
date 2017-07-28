#Exibir seno, cosseno e tangente.
from math import cos, sin, tan
ang = float(input('Insira um angulo qualquer: '))
print('O valor do seno {:.3f}, do cosseno {:.3f} e tangente {:.3f}'
      ' do angulo '.format(sin(ang), cos(ang), tan(ang)))