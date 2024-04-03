from abc import ABC, abstractmethod


# Foo é apenas um placeholder, podendo ser qualquer nome que nos for conveniente.
class AbstractFoo(ABC):
    def __init__(self, name):
        # Neste exemplo, iremos passar o valor recebido para nosso setter que irá atribuí-lo
        # a nosso atributo nome.
        self.name = None
        self._receive_name = name

    # Para criarmos uma property abstrata, devemos utilizar como decorador
    # mais interno o abstractmethod.
    @property
    @abstractmethod
    def _receive_name(self): ...

    @_receive_name.setter
    def _receive_name(self, name): ...


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)

    # Iremos implementar nossos getter e setter em nossa subclasse.
    # Obs.: Lembrando que o getter e setter ainda serão da superclasse AbstractFoo
    @property
    def _receive_name(self):
        return self.name

    @_receive_name.setter
    def _receive_name(self, value):
        self.name = value


obj = Foo('Bar')
print(obj.name)
