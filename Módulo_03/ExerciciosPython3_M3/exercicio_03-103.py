def ficha(nome='?', gols=0):
    print(f'O jogador {nome} marcou {gols} gols.')


#Programa principal
jogador = input('Informe o nome do jogador: ')
numGols = input('Informe o número de gols do jogador: ')
if numGols.isnumeric():
    numGols = int(numGols)
    if jogador:
        ficha(jogador, numGols)
    else:
        ficha(gols=numGols)
else:
    if jogador:
        ficha(jogador)
    else:
        ficha()
