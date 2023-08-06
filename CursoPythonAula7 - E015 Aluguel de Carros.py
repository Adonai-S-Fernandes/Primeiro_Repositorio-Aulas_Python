print(''*24)
print('')
print('Aluguel Supremo de Carros')
print('')
print('Qualquer carro alugado, vai custar RS$60 por dia alugado. \nE a cada KM percorrio, irá ter um custo adicional de RS$0,15.')
print('-'*15)
diasalugados = (int(input('Informe a quantidade de dias pelo qual o carro foi alugado: ')))
kmpercorrido = (float(input('Informe a quantidade de quilômetros do qual o carro percorreu: ')))
custodias = diasalugados*60
custokm = kmpercorrido*0.15
custototal = custodias + custokm
print('-'*15)
print(f'Você utilizou o carro por um total de {diasalugados} dias, o que custará R${custodias:.2f}. \nE percorreu um total de {kmpercorrido} quilômetros, o que custará R${custokm:.2f}')
print(f'O Custo total é de: R${custototal:.2f}')
print('')
print(''*24)
