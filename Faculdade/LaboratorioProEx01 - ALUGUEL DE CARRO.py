lista_registro = []
print('')
print('================= \nLocadora De Carros\n=================')
print('')
while True:
    print('-'*20)
    print('Informe os seguintes dados.')
    nome_cliente = str(input('Informe o nome do cliente: '))
    sexo_cliente = str(input('Informe o sexo do cliente (Digite "M" - Para Masculino | Digite "F" - Para Feminino): '))
    placa_carro = str(input('Informe a placa do carro alugado: '))
    dias_contratados = int(input('Informe a quantidade de dias contratados (Dias Inteiros): '))
    km_contratados = float(input('Informe a quantidade de quilômetros contratados: '))
    print('')
    clientes = {
        "nome_cliente": nome_cliente,
        "sexo_cliente": sexo_cliente,
        "placa_carro": placa_carro,
        "dias_contratados": dias_contratados,
        "km_contratados": km_contratados
    }
    lista_registro.append(clientes)
    print('=== Cliente Registrado! ===')
    desejamais = str(input('Deseja registrar mais um cliente? \nCaso queira continuar, escreva: CONTINUAR \nCaso queira parar, escreva: SAIR \n>> '))
    print('')
    if desejamais.upper() == 'SAIR':
        break

print('')
print('='*30)
print('= Relatorio dos Clientes Cadastrados =')
valor_total = 0
total_km = 0
for clientes in lista_registro:
    valor_total = (clientes["dias_contratados"]*70) + (clientes["km_contratados"]*0.10)
    total_km += (clientes["km_contratados"])
    print('-'*20)
    print(f'Nome | Sexo | Placa do Carro \n{clientes["nome_cliente"]} | {clientes["sexo_cliente"]} | {clientes["placa_carro"]}')
    print('-'*20)
    print(f'O custo de {clientes["dias_contratados"]} dias contratados, é de: R${clientes["dias_contratados"]*70} \nO custo de {clientes["km_contratados"]} quilômetros contratados é de: R${clientes["km_contratados"]*0.10:.2f} \nO Valor total a se pagar é de: R${valor_total} \n-------------------- \n')

print('= Informações Extras =')
media_km = total_km / len(lista_registro)
print(f'A media de quilômetros contratados pelos clientes foi de {media_km:.2f} km.')
print('')
print('O Total de clientes do sexo feminino, com mais de 7 dias contratados:')
for clientes in lista_registro:
    if (clientes["sexo_cliente"]).upper() == 'F' and (clientes["dias_contratados"]) > 7:
        print(f'Nome: {(clientes["nome_cliente"])} \nDias Contratados: {(clientes["dias_contratados"])} \n-------------')


'''nome do cliente
sexo
placa do carro alugado
quantidade de quilometros contratados (0.10 por km)
quantidade de dias contratados (70 reais por dia)

imprimir placa do carro
valor total = (dias * 70) + (km * 0.10)

imprimir a media de km contratado
contador de cada cliente, e seus km
km anterior + km novo
depois dividir pela quantidade de vezes, com contador km total / Contador

imprimir nome das mulheres, com mais de 7 dias contratados'''
