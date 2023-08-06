alugueis = []

while True:
    print("=== Locadora de Veículos ===")
    nome = input("Nome do cliente (ou SAIR para encerrar): ")
    if nome.upper() == "SAIR":
        break
    
    sexo = input("Sexo do cliente (F/M): ")
    placa_carro = input("Placa do carro alugado: ")
    km_contratados = float(input("Quantidade de quilômetros contratados: "))
    dias_contratados = int(input("Quantidade de dias contratados: "))
    
    aluguel = {
        "nome": nome,
        "sexo": sexo,
        "placa_carro": placa_carro,
        "km_contratados": km_contratados,
        "dias_contratados": dias_contratados
    }
    alugueis.append(aluguel)
    
    print("\nAluguel registrado!\n")

print("\n=== Relatório de Aluguéis ===")
total_km = 0
total_valor = 0

for aluguel in alugueis:
    valor_total = (aluguel["dias_contratados"] * 70) + (aluguel["km_contratados"] * 0.10)
    total_km += aluguel["km_contratados"]
    total_valor += valor_total
    
    print(f"Cliente: {aluguel['nome']}")
    print(f"Placa do carro: {aluguel['placa_carro']}")
    print(f"Valor total a pagar: R$ {valor_total:.2f}\n")

media_km = total_km / len(alugueis)
print(f"Média de quilômetros contratados: {media_km:.2f} km")

print("\nClientes do sexo feminino com aluguéis acima de 7 dias:")
for aluguel in alugueis:
    if aluguel["sexo"].upper() == "F" and aluguel["dias_contratados"] > 7:
        print(aluguel["nome"])

#Usando ajuda externa