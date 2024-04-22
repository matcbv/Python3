lista = [1, 2, 3, 4, 5]
contador = enumerate(lista)
print(len(lista))

for num in range(len(lista)+1):
    print(num)

print(next(contador))

