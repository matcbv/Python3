from collections.abc import Iterator, Iterable

class Iteravel(Iterable):
    def __init__(self, iteravel):
        self.iteravel = iteravel

    def __iter__(self):
        return Iterador(self.iteravel)


class Iterador(Iterator):
    def __init__(self, iteravel):
        self.iteravel = iteravel
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
