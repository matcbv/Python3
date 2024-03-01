dadosJogador = {'Nome': input('\nInforme o nome do jogador: ').title(),
                'golsJogos': []}
numJogos = int(input('Quantas partidas foram jogadas pelo jogador?'))
print()
for c in range(0, numJogos):
    dadosJogador['golsJogos'].append(int(input(f'Número de gols marcados pelo jogador na {c+1}ª partida: ')))
print('-'*50)
somaGols = 0
for c in range(0, numJogos):
    print(f'Jogo Nº{c+1} - {dadosJogador["golsJogos"][c]} gols.')
    somaGols = somaGols + dadosJogador["golsJogos"][c]
print(f'\nO jogador {dadosJogador["Nome"]} marcou um total de {somaGols} gols.')

