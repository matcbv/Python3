numeros = []
cont = 0
print('-' * 25)
for c in range(0, 5):
    numeros.append(int(input(f'Informe o {c + 1}ª número: ')))
print('-' * 25)
print(f'O maior valor informado acima foi {max(numeros)}, aparecendo nas posições: ', end='')
for c in numeros:
    if c == max(numeros):
        cont += 1
for pos, c in enumerate(numeros):
    if c == max(numeros) and cont > 1:
        print(pos, end=', ')
        cont -= 1
    elif c == max(numeros):
        print(pos, end='.')

print(f'O menor valor informado acima foi {min(numeros)}, aparecendo nas posições: ', end='')
cont = 0
for c in numeros:
    if c == min(numeros):
        cont += 1
for pos, c in enumerate(numeros):
    if c == min(numeros) and cont > 1:
        print(pos, end=', ')
        cont -= 1
    elif c == min(numeros):
        print(pos, end='.')
