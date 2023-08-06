print('')
print('============== \nCalculoHipotenusa \n============== ')
print('')
'''co = float(input('Informe o valor do comprimento do cateto oposto: '))
ca = float(input('Informe o valor do comprimento do cateto adjascente: '))
print('')
print(f'O valor do comprimento da hipotenusa é de {(co**2 + ca**2)**(1/2):.2f}')'''

from math import hypot
co = float(input('Informe o valor do comprimento do cateto oposto: '))
ca = float(input('Informe o valor do comprimento do cateto adjascente: '))
print('')
print(f'O valor do comprimento da hipotenusa é de {hypot(co, ca):.2f}')



