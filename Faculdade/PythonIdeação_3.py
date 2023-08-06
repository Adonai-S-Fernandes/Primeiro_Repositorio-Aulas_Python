print('y = (x + 1) + (x + 2) + (x + 3) + ... + (x + 20)')
valor = int(input('Insira um número inteiro: '))
y = 0
for c in range(1, 21):
    y += (valor + c)
print(f'y = {y}')

