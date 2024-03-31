# utilizando o mesmo exemplo da classe anterior:
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self.name = None
        self._receive_name = name

    @property
    def _receive_name(self):
        return self.name

    # Desta vez, utilizaremos o decorador somente em nosso setter:
    @_receive_name.setter
    @abstractmethod
    def _receive_name(self, name): ...


class Foo(AbstractFoo):

    def __init__(self, name):
        super().__init__(name)

    # Para especificarmos nosso setter em uma subclasse, devemos específicar o nome da classe
    # abstrata que este setter pertence:
    @AbstractFoo._receive_name.setter
    def _receive_name(self, value):
        self.name = value


obj = Foo('Bar')
print(obj.name)
