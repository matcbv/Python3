from abc import abstractmethod, ABC


class ClasseAbstrata(ABC):
    def __init__(self, valor01, valor02, valor03):
        self.lista_valores = [valor01, valor02, valor03]

    @abstractmethod
    def soma_valores(self) -> (int, float): ...


class ValoresPares(ClasseAbstrata):
    def __init__(self, valor01, valor02, valor03, valor_base=0):
        super().__init__(valor01, valor02, valor03)
        self.valor_base = valor_base
        self.multiplicador = None

    def soma_valores(self):
        for num in self.lista_valores:
            self.valor_base += num
        return self.valor_base

    def __call__(self):
        print(f'{self.__class__.__name__} - {self.__dict__}')


class ContextGenerator:
    def __init__(self, path, opening_mode):
        self.path = path
        self.opening_mode = opening_mode
        self.arquivo = None

    def __enter__(self):
        self.arquivo = open(self.path, self.opening_mode)
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()


obj = ValoresPares(3, 2, 1)
result = obj.soma_valores()
obj()

cg = ContextGenerator('banco_de_dados', 'w')

with cg as arquivo:
    arquivo.write('teste')
