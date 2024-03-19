from functools import partial, reduce
from itertools import groupby

dicionario = [{'nome': 'Matheus', 'idade': 21}, {'nome': 'Mariana', 'idade': 29}]

result = reduce(lambda soma_idade, dic: soma_idade + dic['idade'], dicionario, 0)
print(result)

print('-'*60)

lista_nomes = ['Matheus', 'Mariana', 'Thomaz', 'Thalia']
lista_idade = [21, 29, 4, 0.4]

lista_de_tuplas = list(zip(lista_nomes, lista_idade))
print(lista_de_tuplas)
for e in lista_de_tuplas:
    print(e)

print('-'*60)

familia = [{'Nome': 'Matheus', 'Idade': 21},
           {'Nome': 'Matheus', 'Idade': 29},
           {'Nome': 'Thomaz', 'Idade': 4},
           {'Nome': 'Thalia', 'Idade': 0.4}]



familia = groupby(familia, key=lambda lista: lista['Nome'])
for k, e in familia:
    print(k)
    for p in e:
        print(p)
