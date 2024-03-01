matriz = [[], [], []]
somaPares = somaColuna3 = maiorSegLinha = 0

for c in range(0, 3):
    matriz[0].append(int(input(f'Informe a seguir, o componente da 1ª linha e {c+1}ª coluna: ')))
    if matriz[0][c] % 2 == 0:
        somaPares += matriz[0][c]
somaColuna3 += matriz[0][2]

for c in range(0, 3):
    matriz[1].append(int(input(f'Informe a seguir, o componente da 2ª linha e {c+1}ª coluna: ')))
    if matriz[1][c] % 2 == 0:
        somaPares += matriz[1][c]
    if matriz[1][c] > maiorSegLinha:
        maiorSegLinha = matriz[1][c]
somaColuna3 += matriz[1][2]

for c in range(0, 3):
    matriz[2].append(int(input(f'Informe a seguir, o componente da 3ª linha e {c+1}ª coluna: ')))
    if matriz[2][c] % 2 == 0:
        somaPares += matriz[2][c]
somaColuna3 += matriz[2][2]

print('\nA matriz formada pelos componentes indicados acima é:')
for linhas in matriz:
    print(linhas)
print('A soma dos valores da terceira coluna é:', somaColuna3)
print('A maior valor da segunda linha é:', maiorSegLinha)
