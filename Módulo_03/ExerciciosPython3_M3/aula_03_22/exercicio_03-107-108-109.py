from utilidades.cauculos import *
print(f'\n{"MERCADINHO DO CERQUEIRA":-^50}')

while True:
    quantia = float(input('\nInforme o valor do produto: '))
    print('\nQual a operação que deseja realizar?'
          '\n[1] Aumentar o valor'
          '\n[2] Diminuir o valor'
          '\n[3] Dobrar o valor'
          '\n[4] Metade do valor'
          )
    operacao = int(input('\nDigite a seguir: '))
    porcentagem = 0
    while operacao < 1 and operacao > 4:
        print('Resposta inválida!')
        operacao = int(input('\nDigite a seguir: '))
    if operacao == 1 or operacao == 2:
        porcentagem = int(input('Informe a porcentagem da alteração: '))
    if operacao == 1:
        result = aumentar(quantia, porcentagem)
        print(f'\nO valor final do produto é: {moeda(result[0], result[1])}')
    elif operacao == 2:
        result = diminuir(quantia, porcentagem)
        print(f'\nO valor final do produto é: {moeda(result[0], result[1])}')
    elif operacao == 3:
        result = dobro(quantia)
        print(f'\nO valor final do produto é: {moeda(result[0], result[1])}')
    else:
        result = metade(quantia)
        print(f'\nO valor final do produto é: {moeda(result[0], result[1])}')
    cont = input('Deseja recalcular o preço de mais algum produto? [S/N] ').upper()[0]
    while cont not in 'SN':
        print('Resposta inválida!')
        cont = input('Deseja recalcular o preço de mais algum produto? [S/N] ').upper()[0]
    if cont == 'N':
        print('\nPROGRAMA ENCERRADO...')
        break
