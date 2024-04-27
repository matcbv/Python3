from itertools import groupby
from functools import reduce, partial

lista_01 = [{'nome': 'matheus', 'sobrenome': 'cerqueira'}, {'nome': 'mariana', 'sobrenome': 'veiga'},
            {'nome': 'thomas', 'sobrenome': 'veiga'}, {'nome': 'thalia', 'sobrenome': 'veiga'}]

lista_02 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_03 = [11, 12, 13, 14, 15, 16, 17, 18]

lista_01.sort(key=lambda num: num['nome'])
print(lista_01)
lista_ordenada = groupby(lista_02, lambda num: num['nome'])
soma_lista = reduce(lambda num, acumulador: num + acumulador, lista_02, 0)


def somar(num01, num02, val_inicio):
    val_inicio += num01 + num02
    return val_inicio


soma_padrao = partial(somar, val_inicio=0)

print(soma_padrao(3, 5))

lista_zippada = zip(lista_02, lista_03)
for i in lista_zippada:
    print(i)

lista_mapeada = map(lambda num: num if num % 2 == 0 else 'Não é par', lista_02)
for i in lista_mapeada:
    print(i)
print()

lista_filtrada = filter(lambda num: num % 2 == 0, lista_03)

for n in lista_filtrada:
    print(n)
