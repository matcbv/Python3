tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro')
# Comando for com variáveis compostas:
for pos, cont in enumerate(tupla):
    print(f'Posição {pos} - {cont}')

# Segunda opção ao utilizar o comando for:
for cont in range(0, len(tupla)):
    print(f'Posição {cont} - {tupla[cont]}')

print('-' * 20)

# Soma de tuplas:
a = (1, 2, 3)
b = (3, 2, 1)
c = a + b
print(c)
print(c.index(3))
