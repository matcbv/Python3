from functools import reduce

dicionario = [{'nome': 'Matheus', 'idade': 21}, {'nome': 'Mariana', 'idade': 29}]

result = reduce(lambda soma_idade, dic: soma_idade + dic['idade'], dicionario, 0)
print(result)
