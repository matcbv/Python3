from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass


Classe = namedtuple('Classe', ['Valor'], defaults=('Teste',))
obj = Classe()
# print(obj.Valor)


class Classe02(NamedTuple):
    valor: str = 'Teste_02'


@dataclass(frozen=True, order=True)
class NossaDataClasse:

    nome = ['b', 'd', 'a', 'c']
    sobrenome = 'sobrenome'


obj = NossaDataClasse()
ordenado = sorted(obj.nome)
print(ordenado)