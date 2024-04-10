# Através da classe Sequence, definimos o comportamento de nossas próprias sequências.
# Uma sequência é um objeto que contém elementos ordenados, onde cada elemento tem
# uma posição específica na sequência, chamada de índice. Exemplos de sequências são:
# listas, tuplas, strings, etc.

# Nossa classe Sequence, possui como métodos abstratos os métodos especiais __len__ e __getitem__.
# Nada nos impede de definirmos outros métodos, como __iter__, __next__, __setitem__, etc.
from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def append(self, *values):
        for value in values:
            # Usaremos nossa propriedade _index para adicionarmos elementos ao nosso
            # dicionário com o append.
            self._data[self._index] = value
            self._index += 1

    # Responsável por informar o comprimento de nosso iterável.
    def __len__(self):
        return self._index

    # Responsável por retornar um determinado valor através de seu índice.
    def __getitem__(self, index):
        return self._data[index]

    # Responsável por definir um valor através de seu índice.
    def __setitem__(self, index, value):
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self):
        # Como _index terá o último índice e nosso dicionário. Iremos comparar o
        # _next_indice com o valor de _index a cada iteração. Caso se igualem,
        # a exceção StopIteration será levantada.
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        value = self._data[self._next_index]
        self._next_index += 1
        return value


lista = MyList()
lista.append('Maria', 'Helena')
# Podemos substituir valores graças ao __setitem__:
lista[0] = 'João'
# Conseguimos acessar valores graças ao __getitem__:
print(lista[0])
lista.append('Luiz')
# Podemos descobrir o comprimento do iterável graças ao __len__:
print(len(lista))
print('-'*10)
# Por fim, também é possível iterar sobre nossos elementos graças ao __init__ e __next__.
for item in lista:
    print(item)
