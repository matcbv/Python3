# Em uma list comprehension, podemos aninhar uma sequência de estruturas de repetição,
# onde a mais externa deve ser a primeira a ser colocada em nossa list comprehension. Ex.:

lista_01 = [1, 2, 3]
lista_02 = ['a', 'b', 'c']

lista_03 = [[x, y] for x in lista_01 for y in lista_01]
print(lista_03)

# Podemos chamar funções em nossas list comprehensions:

def factorial(num):
    if num > 1: num *= factorial(num - 1)
    return num

number_list = [1, 2, 3, 4, 5]
factorial_list = [factorial(num) for num in number_list]

print(factorial_list)

# Também podemos filtrar elementos:

number_list = [1, 2, 3, 4, 5]
odd_list = [num for num in number_list if num % 2 != 0]

print(odd_list)

# Por fim, podemos utilizar o operador := para capturar o valor de uma expressão e reutilizá-lo:

n = 0
results = [(n := x ** 2) for x in range(10) if n > 20]
print(results)
