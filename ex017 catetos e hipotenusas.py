#esse foi eu tentando fazer

'''co = float(input('Informe o comprimento do cateto oposto : '))
ca = float(input('Informe o comprimento do cateto adjacente : '))
h = co**2 + ca**2
print('A hipotenusa é {}'.format(h))'''

#a hipotenusa é igual a raiz quadrada da soma dos quadrados dos catetos

'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
h =  (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f} '.format(h))'''

#usando o módulo math com a funcionalidade hypot que calcula a hipotenusa de uma forma mais fácil
'''import math
co = float(input('Informe o comprimento do cateto oposto : '))
ca = float(input('Informe o comprimento do cateto adjacente : '))
h = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))'''

#importando apenas a funcionalidade hypot do módulo math
from math import hypot
co = float(input('Informe o comprimento do cateto oposto : '))
ca = float(input('Informe o comprimento do cateto adjacente : '))
h = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))




