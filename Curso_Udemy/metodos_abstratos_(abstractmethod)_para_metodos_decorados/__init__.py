from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.receive_name = name

    # Para criarmos uma property abstrata, devemos utilizar como decorador
    # mais interno o abstractmethod.
    @property
    @abstractmethod
    def receive_name(self): ...

    @receive_name.setter
    def receive_name(self, name):
        self._name = name


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print('Sou inútil')
