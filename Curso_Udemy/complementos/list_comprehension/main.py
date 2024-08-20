# Em uma list comprehension, podemos aninhar uma sequência de estruturas de repetição,
# onde a mais externa deve ser a primeira a ser colocada em nossa list comprehension. Ex.:

lista_01 = [1, 2, 3]
lista_02 = ['a', 'b', 'c']

lista_03 = [[x, y] for x in lista_01 for y in lista_01]
print(lista_03)

# Podemos também chamar funções em nossas list comprehensions
