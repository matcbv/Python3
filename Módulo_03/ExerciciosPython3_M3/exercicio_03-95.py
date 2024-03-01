dadosJogadores = {'nome': [], 'numJogos': [], 'golsJogador': []}
cont = exibir = cond = 0
while True:
    temp = []
    dadosJogadores['nome'].append(input(f'\nInforme o nome do {cont+1}º jogador: ').title())
    dadosJogadores['numJogos'].append(int(input('Informe o número de partidas jogadas pelo jogador: ')))
    for c in range(0, dadosJogadores['numJogos'][cont]):
        temp.append(int(input(f'Informe o número de gols feitos pelo jogador no jogo Nº{c+1}: ')))
    dadosJogadores['golsJogador'].append(temp[:])
    cont += 1
    cond = input('Deseja adicionar mais algum jogador? [S/N]').upper()
    while cond not in 'SN':
        print('Resposta inválida.')
        cond = input('Deseja adicionar mais algum jogador? [S/N]').upper()
    if cond == 'N':
        break
cond = input('\nDeseja exibir os dados de um ou mais jogadores? [S/N] ').upper()
while cond not in 'SN':
    print('Opção inválida.')
    cond = input('Deseja exibir os dados de um ou mais jogadores? [S/N] ').upper()
while cond == 'S':
    print('\n[1] - Exibir um jogador específico'
          '\n[2] - Exibir todos os jogadores'
          '\n[3] - Encerrar programa')
    exibir = int(input('Escolha uma das opções acima: '))
    while exibir != 1 and exibir != 2 and exibir != 3:
        print('Opção inválida.')
        exibir = int(input('Escolha uma das opções acima: '))
    if exibir == 1:
        somaGols = cont = 0
        nomeJogador = input('informe o nome do jogador a ser exibido: ').title()
        for c in dadosJogadores['nome']:
            if c == nomeJogador:
                print(f'\nDados do jogador {dadosJogadores["nome"][cont]}:')
                pos = 1
                for v in dadosJogadores['golsJogador'][cont]:
                    print(f'Jogo Nº {pos} - {v} gol(s)')
                    pos += 1
                    somaGols += v
                print(f'O jogador tem um total de {somaGols} gols.')
            else:
                cont += 1
        cond = input('\nDeseja continuar exibindo os dados de um ou mais jogadores? [S/N] ').upper()
        while cond not in 'SN':
            print('Opção inválida.')
            cond = input('Deseja continuar exibindo os dados de um ou mais jogadores? [S/N] ').upper()
    elif exibir == 2:
        somaGols = 0
        for c in range(0, len(dadosJogadores['nome'])):
            print(f'\nDados do jogador {dadosJogadores["nome"][c]}:')
            for i, v in enumerate(dadosJogadores['golsJogador'][c]):
                print(f'Jogo Nº{i+1} - {v} gols')
                somaGols += v
        print(f'O jogador tem um total de {somaGols} gols.')
        cond = input('\nDeseja continuar exibindo os dados de um ou mais jogadores? [S/N] ').upper()
        while cond not in 'SN':
            print('Opção inválida.')
            cond = input('Deseja continuar exibindo os dados de um ou mais jogadores? [S/N] ').upper()
    else:
        cond = 'N'
print('\nPrograma encerrado...')
