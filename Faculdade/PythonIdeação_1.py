lista = []
resp = 1
soma = 0
while resp != 0:
    resp = int(input('Insira um número inteiro: '))
    if resp >= 1:
       lista.append(resp)
       soma += resp
print(lista)
print('A soma de todos os números inseridos é de {}'.format(soma))
