print(''*20)
print('')
print('= IMPORT/MÓDULOS =')
print('')
from math import sqrt, floor
num = int(input('Digite um número:'))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz):.2f}')
#ceil é a função, na qual arredonda o número, para um valor mais alto.
#floor é a função, aonde encontra a raiz mais próxima do número.