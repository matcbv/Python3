class Soma:

    def __init__(self):
        self._valor01 = 1
        self._valor02 = 2
        self.__result = self._valor01 + self._valor02

    @property
    def valor(self):
        return self._valor01, self._valor02

    @valor.setter
    def valor(self, novoValor):
        self._valor01, self._valor02 = novoValor


primeiraConta = Soma()
print(primeiraConta._Soma__result)
segundaConta = Soma()
segundaConta.valor = (4, 5)
print(segundaConta._Soma__result)
