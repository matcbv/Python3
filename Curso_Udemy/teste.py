from functools import partial, reduce
from itertools import groupby

dicionario = [{'nome': 'Matheus', 'idade': 21}, {'nome': 'Mariana', 'idade': 29}]

result = reduce(lambda soma_idade, dic: soma_idade + dic['idade'], dicionario, 0)
print(result)

print('-' * 60)

lista_nomes = ['Matheus', 'Mariana', 'Thomaz', 'Thalia']
lista_idade = [21, 29, 4, 0.4]

lista_de_tuplas = list(zip(lista_nomes, lista_idade))
print(lista_de_tuplas)
for e in lista_de_tuplas:
    print(e)

nova_funcao = partial(lambda num1, num2: num1 * num2, num2=10)
print(nova_funcao(2))
