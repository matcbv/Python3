from abc import abstractmethod, ABC
from functools import reduce


# ------------------------------- CLASSES ABSTRATAS E MÉTOODS ABTRATOS -------------------------------
class ClasseAbstrata(ABC):
    def __init__(self, lista_valores):
        self.lista_valores = lista_valores
        resp = checar_valores(self.lista_valores)
        if resp in 'impar':
            print('Os valores passados não são todos pares! Informe novos valores')
            self.lista_valores = []

    @abstractmethod
    def soma_valores(self): ...


class ValoresPares(ClasseAbstrata):
    def __init__(self, lista_valores, valor_base=0):
        super().__init__(lista_valores)
        self.valor_base = valor_base

    def soma_valores(self):
        self.valor_base = reduce(lambda cont, num: cont + num, self.lista_valores, 0)
        return self.valor_base

    def __call__(self):
        print(f'{self.__class__.__name__} - {self.__dict__}')


class ValoresImpares(ClasseAbstrata):
    def __init__(self, lista_valores, valor_base=0):
        super().__init__(lista_valores)
        self.valor_base = valor_base

    def soma_valores(self):
        self.valor_base = reduce(lambda cont, num: cont + num, self.lista_valores, 0)
        return self.valor_base

    def __call__(self):
        print(f'{self.__class__.__name__} - {self.__dict__}')


def checar_valores(valores):
    cont = 0
    for num in valores:
        num = int(num)
        if num % 2 == 0:
            cont += 1
    if cont == len(valores):
        return 'par'
    elif cont == 0:
        return 'impar'
    return 'impar e par'


# ------------------------------- CONTEXT GENERATORS -------------------------------
class ContextGenerator:
    def __init__(self, path, opening_mode):
        self.path = path
        self.opening_mode = opening_mode
        self.arquivo = None

    def __enter__(self):
        print('Abrindo arquivo...')
        self.arquivo = open(self.path, self.opening_mode)
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo...')
        self.arquivo.close()
        if exc_type:
            print('Ocorreu um erro do tipo:', exc_type)
            print('O motivo do erro foi:', exc_val)
            return True


# ------------------------------- __new__ e __init__ -------------------------------

class CriandoInstancias:
    def __new__(cls, *args, **kwargs):
        print('Passei por aqui...')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, valor):
        self._valor = valor


# ------------------------------- METACLASSES -------------------------------
class NossaMetaclasse(type):
    def __new__(mcs, name, base, dct):
        classe = super().__new__(mcs, name, base, dct)
        return classe

    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(cls)
        return instancia


class NossaClasse(metaclass=NossaMetaclasse):
    def __new__(cls, *args, **kwargs):
        print('Passei por aqui...')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, valor):
        self.valor = valor


lista_pares = input('Informe três valores pares separando-os por espaço: ').split()
obj = ValoresPares(lista_pares)
result = obj.soma_valores()
obj()

cg = ContextGenerator('banco_de_dados', 'w')

with cg as arquivo:
    arquivo.write('Valor qualquer')

outro_obj = CriandoInstancias('Texto aleatório')
print(outro_obj.valor)
