matriz = [[], [], []]
for c in range(0, 3):
    matriz[0].append(int(input(f'Informe a seguir, o componente da 1ª linha e {c+1}ª coluna: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Informe a seguir, o componente da 2ª linha e {c+1}ª coluna: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Informe a seguir, o componente da 3ª linha e {c+1}ª coluna: ')))
print('\nA matriz formada pelos componentes indicados acima é:')
for linhas in matriz:
    print(linhas)
