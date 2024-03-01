print('---------------- CONTROLE DE ESTOQUE - SUPERMERCADO COMPRA FÁCIL ----------------')
total = [[], [], []]
cont = 0
codProd = 0

while True:
    total[0].append(input('Informe o nome do produto: ').title())
    total[1].append(input('Informe a quantidade no estoque: '))
    total[2].append(codProd)
    print('-'*20)
    print('Nome do produto:', total[0][cont])
    print('Quantidade:', total[1][cont])
    print('Código do produto:', codProd)
    print('-' * 20)
    codProd += 1
    cont += 1
    cond = input('Deseja continuar adicionando produtos? [S/N] ').upper()
    while cond not in 'SN':
        print('Resposta inválida!')
        cond = input('Deseja continuar adicionando produtos? ').upper()
    if cond == 'N':
        break
    print('-' * 20)
print('-' * 20)
print(
    '1 - Lista completa dos produtos cadastrados'
    '\n2 - Exibir um produto específico'
    '\n3 - Sair do programa'
)
opcao = int(input('\nQual das opções acima deseja escolher? '))
if opcao != 1 and opcao != 2 and opcao != 3:
    print('Opção inválida! Tente novamente.')
    opcao = int(input('Qual das opções acima deseja escolher? '))
elif opcao == 1:
    for c in range(0, cont):
        print(
            f'\nNome do produto: {total[0][c]}'
            f'\nQuantidade: {total[1][c]}'
            f'\nCódigo do produto: {codProd}'
        )
    while True:
        cond = input('\nDeseja exibir algum produto específico? [S/N] ').upper()
        while cond not in 'SN':
            print('Resposta inválida. Tente novamente.')
            cond = input('Deseja exibir algum produto específico? [S/N] ').upper()


elif opcao == 2:
    while True:
        limite = codProd
        codProd = int(input('Qual o código do produto que deseja que seja exibido? '))
        while 0 > codProd > limite:
            print('Código incorreto! Tente novamente.')
            codProd = int(input('Qual o código do produto que deseja que seja exibido? '))
        print(
            f'Nome do produto: {total[0][codProd-1]}'
            f'\nQuantidade: {total[1][codProd-1]}'
            f'\nCódigo do produto: {codProd}\n'
        )
        cond = input('Deseja exibir mais algum produto? [S/N] ').upper()
        while cond not in 'SN':
            print('Resposta inválida. Tente novamente.')
            cond = input('Deseja exibir mais algum produto específico? [S/N] ').upper()
        if cond == 'N':
            opcao = 3
            break

elif opcao == 3:
    print('Programa encerrado...')
