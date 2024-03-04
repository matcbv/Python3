def somar(num1, num2):
    return num1 + num2


def multiplicar(multiplicador, *numeros):
    result = 0
    for n in numeros:
        result += n * multiplicador
    return result


# Também podemos passar diversos argumentos para uma função lambda.
num1 = 2
num2 = 3
print(somar(num1, num2))
print(lambda num1, num2: num1 + num2)

# A Seguir temos outro exemplo com um parâmetro de empacotamento:
# Lembrando que o primeiro argumento será o multiplicador, e os demais serão postos em uma tupla.
print(multiplicar(2, 1, 2, 3, 4))
print(lambda m, *nums: 2, 1, 2, 3, 4)
