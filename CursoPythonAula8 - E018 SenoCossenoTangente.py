print('')
from math import sin, cos, tan, radians
print('============== \nSenCosTan \n==============')
angulo = float(input('Digite o ângulo, para calcular o Seno, Cosseno e a Tangente: '))
print(f'O Seno do ângulo {angulo}°, é de: {sin(radians(angulo)):.2f} \nO Cosseno do ângulo {angulo}°, é de: {cos(radians(angulo)):.2f} \nA Tangente do ângulo {angulo}°, é de: {tan(radians(angulo)):.2f}')
#O Sin, cos, tan: Só podem fazer com números radianos. Por isso o "radians", para que o número possa ser calculado.