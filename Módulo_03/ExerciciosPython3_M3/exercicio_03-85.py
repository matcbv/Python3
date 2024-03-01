numeros = []
impares = []
pares = []
numeros.append(pares)
numeros.append(impares)
# Também poderíamos criar uma lista já com outras listas atribuidas a ela.
# Ex: numeros = [[], []]
# A primeira seria numeros[0] e a segunda numeros[1]

for cont in range(0, 7):
    num = int(input(f'Informe a seguir, o {cont+1}º número a ser adicionado na lista: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
print('-' * 30)
print('Números pares da lista:')
for i in range(0, len(pares)):
    print(pares[i], end=' ')
print('\nNúmeros ímpares da lista:')
for i in range(0, len(impares)):
    print(impares[i], end=' ')
