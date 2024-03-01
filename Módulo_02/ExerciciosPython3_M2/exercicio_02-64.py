cont = soma = 0
numero = int(input('Informe a seguir, o número a ser somado: '))

while numero != 999:
    soma += numero
    numero = int(input('Informe a seguir, o número a ser somado: '))
    cont += 1

print(f'\nA soma total dos {cont} números informados é {soma}')
