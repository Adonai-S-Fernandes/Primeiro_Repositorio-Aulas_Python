lista = [1, 11, 12, 11, 14, 15, 16, 12, 12, 11]
num = 11
cont = 0
pares = 0
for c in lista:
    if c == num:
        cont += 1
    if c % 2 == 0:
        pares += 1
print(lista)
print(f'A quantidade de vezes que o número 11, apareceu na lista é de {cont} vezes.')
print(f'E nessa lista, existem um total de {pares} números pares.')