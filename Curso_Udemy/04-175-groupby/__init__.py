# O método groupby é responsável por agrupar os elementos de um iterável, criando grupos para cada
# valor diferente existente naquele iterável.
# Ele retorna uma tupla contendo um elemento chave, indicando o valor que considerou ao criar
# aquele grupo, e um grupo em forma de iterador, contendo todos os elementos do iterável que
# continham aquele valor em questão.

from itertools import groupby

# Para utilizarmos o groupby, os elementos em nossa lista precisam estar ordenados sequencialmente.
# Caso contrário, o groupby acabará criando grupos de mesmo valor.
# Ex.: lista = ['a', 'a', 'b', 'b', 'c', 'a'], nesse caso o groupby criará dois grupos de valor a,
# já que elementes de mesmo valor se encontram separados.
lista = ['a', 'b', 'c', 'a', 'a', 'b', 'c', 'b', 'c', 'c']
lista_organizada = groupby(sorted(lista))

for k, g in lista_organizada:
    print('\nChave:', k)
    for e in g:
        print(e, end=' ')

alunos = [
    {'nome': 'matheus', 'turma': 'A'}, {'nome': 'claudio', 'turma': 'C'},
    {'nome': 'leonardo', 'turma': 'B'}, {'nome': 'thaisa', 'turma': 'B'},
    {'nome': 'camila', 'turma': 'C'}, {'nome': 'lucas', 'turma': 'A'}
]
print('\n', '-'*60)

alunos_organizados = sorted(alunos, key=lambda lst: lst['turma'])
grupos_turma = groupby(alunos_organizados, key=lambda lst: lst['turma'])
for k, g in grupos_turma:
    print('')
    print(k, end=' - ')
    for e in g:
        print(e, end='; ')
