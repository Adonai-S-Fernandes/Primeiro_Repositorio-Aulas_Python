import sys
while True:
    comando = int(input('Digite 1 para ir, e 0 para sair: '))
    if (comando == 1):
        print('Muito burro')
    elif (comando == 0):
            desejasair = str(input('Você tem certeza que deseja sair? [Sim] ou [Não]: '))
            if desejasair == 'Sim':
                print('Saindo do programa...')
                exit()
            elif desejasair == 'Não':
                continue
            else:
                 print('Opção invalida!')
                    
              
