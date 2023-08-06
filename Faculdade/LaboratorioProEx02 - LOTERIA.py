import random
print('== SUPER LOTERIA ==')
print('-= LOTOFACIL =-')
print('')
while True:
    try:
        dezenas = int(input('Informe a quantidade de dezenas, que você deseja marcar (Entre 15, 16, 17 e 18): '))
        if 15 <= dezenas <= 18:
            break
        else:
            print('Você cometeu um erro. \nInforme uma quantidade de dezenas valida.')
    except ValueError:
        print('Você cometeu algum erro. \nDigite somente números inteiros, que estejam entre [15, 16, 17 ou 18].')
    print('')

primeira_aposta = set()
while len(primeira_aposta) < dezenas:
    numpri_aposta = 0
    while numpri_aposta < 1:
        try:
            numpri_aposta = int(input(f'Informe o {len(primeira_aposta) + 1}º número da aposta (Entre 1 e 25): '))
            if numpri_aposta < 1 or numpri_aposta > 25:
                print('Dezena Invalida! \nVocê digitou um número fora do intervalo entre 1 e 25 números.')
                print('')
            elif numpri_aposta in primeira_aposta:
                print(f'Número Repetido! \nVocê deve digitar {dezenas} números diferentes. \nTente Novamente.')
                print('')
            else:
                primeira_aposta.add(numpri_aposta)
        except ValueError:
            print('Você cometeu um erro! \nDigite somente números inteiros. (Entre 1 e 25)')
            print('')
print('='*30)
primeira_aposta_ordem = sorted(list(primeira_aposta))
surpresinha1 = (random.sample(range(1, 26), 18))
surpresinha2 = (random.sample(range(1, 26), 18))
resultado_sorteio = (random.sample(range(1, 26), 15))
acertos = len(primeira_aposta.intersection(resultado_sorteio))

print('= SUA APOSTA =')
print(f'A sua aposta de {dezenas} dezenas:', ", ".join(map(str, primeira_aposta_ordem)))
print('-'*30)
print('= SURPRESINHA =')
print('Os números da Primeira Surpresinha são:', ", ".join(map(str, surpresinha1)))
print('Os números da Segunda Surpresinha são:', ", ".join(map(str, surpresinha2)))
print('-'*30)
print('= RESULTADO LOTOFACIL =')
print('O Resultado do Sorteio da LotoFácil é:\n', ", ".join(map(str, resultado_sorteio)))
print('')
if acertos >= 11:
    print('VOCÊ VENCEU!')
else:
    print('FRACASSADO!')





'''A LOTOFACIL consiste na extração de 15 números aleatórios diferentes, no universo de 01 a 25. Você
marca entre 15 a 18 números, dentre os 25 disponíveis no volante, e fatura o prêmio se acertar 11, 12,
13, 14 ou 15 números. Pode ainda deixar que o sistema escolha os números para você por meio da
Surpresinha. Considerando estas informações, faça um programa em Python para:

a) Solicitar ao usuário a quantidade de dezenas que ele deseja marcar na primeira aposta (entre 15 e 18 números).
Caso o usuário informe uma quantidade de dezenas fora do intervalo válido, o programa deve solicitar nova digitação,
tantas vezes quantas forem necessárias;

b) Solicitar ao usuário informar os números da primeira aposta (dezenas de 01 a 25, sem repetição). Caso o usuário
informe um número repetido, o programa deverá apresentar uma mensagem “Número repetido” e solicitar nova
digitação. Assim como se o usuário informar um número fora do intervalo válido, o programa deverá apresentar uma
mensagem “Dezena inválida” e solicitar nova digitação.

c) Gerar aleatoriamente duas apostas, com 18 números, usando a “Surpresinha”.

d) Simular o resultado (15 dezenas sorteadas) de um concurso da Lotofácil;

e) Imprimir (em ordem crescente) as dezenas da primeira aposta, das duas apostas (surpresinha) e do resultado do
concurso da Lotofácil simulado.'''