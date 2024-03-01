from time import sleep
from random import randint
from operator import itemgetter
dadosJogo = {'Jogador 1': randint(1, 6),
             'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6),
             'Jogador 4': randint(1, 6)}
ranking = []

print('\nNúmeros sorteados:\n')
for k, v in dadosJogo.items():
    print(f'O jogador {k} tirou {v}.')
    sleep(1)
ranking = sorted(dadosJogo.items(), key=itemgetter(1), reverse=True)
# itemgetter(0) acessa o primeiro elemento de um par de elementos, já itemgetter(1), acessa o segundo elemento do par
print()
for i, c in enumerate(ranking):
    print(f'{i+1}ª posição: {c[0]} com o número {c[1]}.')

# Segunda resolução (Feita por mim, com algumas alterações):
# from time import sleep
# from random import randint
# dadosJogo = {}
# jogadores = []
# jogadas = []
# resultado = []
# ranking = {}
#
# for c in range(0, 4):
#     jogadores.append(input(f'Informe o nome do {c+1}º jogador: ').title())
#     sleep(0.8)
#     print('Jogando dado...')
#     sleep(0.8)
#     jogadas.append(randint(1, 6))
#     print('Jogada coletada!\n')
#     if c == 0 or jogadas[c] > jogadas[-1]:
#         maior = jogadas[c]
#         resultado.append(jogadores[c])
#     else:
#         for v in range(1, len(jogadas)+1):
#             if jogadas[c] <= jogadas[-v]:
#                 resultado.insert(-v, jogadores[c])
#                 break
# dadosJogo['jogadores'] = jogadores[:]
# jogadas.sort()
# dadosJogo['jogadas'] = jogadas[:]
# dadosJogo['resultado'] = resultado[:]
#
# pos = 1
# for c in range(1, 5):
#     if c != 1 and dadosJogo['jogadas'][-c] == dadosJogo['jogadas'][-c+1]:
#         print(f'O jogador {dadosJogo["resultado"][-c]} tirou o número {dadosJogo["jogadas"][-c]}, obtendo o {pos-1}º lugar também.')
#         pos -= 1
#     else:
#         print(f'O jogador {dadosJogo["resultado"][-c]} tirou o número {dadosJogo["jogadas"][-c]}, obtendo o {pos}º lugar.')
#     pos += 1
#
# print('\nPrograma encerrado...')
