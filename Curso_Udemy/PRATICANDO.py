from functools import partial, reduce
from itertools import zip_longest, groupby

lista_1 = [1, 1, 3, 3, 3]
lista_2 = [6, 7, 8, 9, 9]

# resultado = reduce(lambda num: num, lista, 0)
# resultado(lista_1)

funcao = partial(lambda num1, num2: num1 + num2, num2=10)


funcao_02 = groupby(lista_1)


def funcao_04(num, seq):
    seq += num
    return seq


funcao_03 = reduce(lambda seq, num: seq+num, lista_1, 0)
print(funcao_03)

lista_par = [num for num in lista_1 if num % 3 == 0]
print(lista_par)

lista_impar = [num if num % 3 == 0 else None for num in lista_1]
print(lista_impar)

dicionario = [{'nome': 'matheus', 'idade': 20}, {'nome': 'lucas', 'idade': 30}, {'nome': 'lucia', 'idade': 21}]
dicionario.sort(key=lambda d: d['idade'], reverse=True)
print(dicionario)

dicionario = [d for d in dicionario if d['nome'] == 'matheus']
print(dicionario)
