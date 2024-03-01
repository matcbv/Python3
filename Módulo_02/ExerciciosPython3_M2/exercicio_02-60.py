from math import factorial

num = int(input('Informe um número a ser cauculado o seu fatorial: '))
result = factorial(num)

print('O fatorial do número informado é:', result)

# Método de resolução sem um módulo:
'''num = int(input('Informe um número a ser cauculado o seu fatorial: '))
i = num
result = 1

while i > 1:
    fatorial = result * i
    i -= 1

print('O fatorial do número informado é:', result)'''