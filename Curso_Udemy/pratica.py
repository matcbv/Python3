from functools import reduce


class ClasseQualquer:
    def __init__(self):
        self._lista_numero = []

    @property
    def recebe_numero(self):
        return self._lista_numero

    @recebe_numero.setter
    def recebe_numero(self, valores):
        for num in valores:
            self._lista_numero.append(num)


obj = ClasseQualquer()
obj.recebe_numero = 1, 2, 3
print(obj.recebe_numero)

soma_lista = reduce(lambda cont, num: cont + num, obj.recebe_numero, 0)
print(soma_lista)
