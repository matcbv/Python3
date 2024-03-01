soma = 0

for i in range(1, 501):
    if i % 2 != 0 and i % 3 == 0:
        soma += i

print('A soma de todos os ímpares múltiplos de 3, entre 1 e 500 é:', soma)
