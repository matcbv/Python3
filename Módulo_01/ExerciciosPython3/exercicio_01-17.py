from math import sqrt, pow

lado1 = int(input('Informe o cateto oposto do triângulo retângulo: '))
lado2 = int(input('Informe o cateto adjacente do triângulo retângulo: '))

print(f'A hipotenusa desse triângulo é {sqrt(pow(lado1, 2) + pow(lado2, 2)):.0f}')
