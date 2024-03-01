numeros = (int(input('Primeiro número: ')), int(input('Segundo número: ')), int(input('Terceiro número: ')), int(input('Quarto número: ')))

print(f'Você digitou o número nove {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'A primeira posição que aparece o valor três é {numeros.index(3) + 1}')
else:
    print('O número três não foi informado entre os 4 números.')
print('Os números pares dentre os listados acima são: ', end='')
for c in range(0, 4):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=', ')
print('Fim')
