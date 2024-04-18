class SetGetItem:
    def __init__(self):
        self.value01 = [1, 2, 3, 4, 5]
        self.value02 = ['a', 'b', 'c', 'd', 'e']

    # O método __getitem__ é responsável por retornar um determinado valor através de seu índice:
    def __getitem__(self, index):
        return self.value01[index]

    # O método __setitem__ é responsável por definir um valor através de seu índice:
    def __setitem__(self, index, value):
        self.value02[index] = value


values = SetGetItem()
print('Valor 1:', values.value01,
      '\nValor 2:', values.value02,)

# Utilizando nosso método __getitem__:
print(values[1])

# Utilizando nosso método __setitem__:
values[2] = 'z'
print(values.value02)
