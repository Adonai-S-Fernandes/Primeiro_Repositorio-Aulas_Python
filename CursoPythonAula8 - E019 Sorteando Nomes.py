import random
print('')
lista_nomes = []
print('=============== \nSorteadorNomes \n===============')
print('')
c = 1
while len(lista_nomes) < 4:
    nome = str(input(f'Informe o nome do {c}° aluno: '))
    lista_nomes.append(nome)
    c += 1
print('')
print(f'Dentre os alunos mencionados {sorted(lista_nomes)}, o aluno randomicamente escolhido foi: {random.choice(lista_nomes)}')

