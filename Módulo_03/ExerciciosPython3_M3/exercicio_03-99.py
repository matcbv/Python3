def maior(*ordem):
    print('\nA sequência ', end='')
    for v in ordem:
        print(v, end='')
    print(f', contendo {len(ordem[0])} números, tem como maior deles o número:', end=' ')
    ordem[0].sort()
    numMaior = 0
    for i, v in enumerate(ordem[0]):
        if i == len(ordem[0])-1:
            numMaior = v
    print(numMaior)


ordem = []
while True:
    ordem.append(int(input('Informe um número: ')))
    cont = input('Deseja adicionar mais algum número? [S/N]').upper()[0]
    while cont not in 'SN':
        print('Resposta inválida.')
        cont = input('Deseja adicionar mais algum número? [S/N]').upper()[0]
    if cont == 'N':
        break

maior(ordem)
