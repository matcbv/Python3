from collections import namedtuple
from typing import NamedTuple
from dataclasses import dataclass


Classe = namedtuple('Classe', ['Valor'], defaults=('Teste',))
obj = Classe()
print(obj.Valor)


class Classe_02(NamedTuple):
    valor: str = 'Teste_02'


@dataclass(frozen=True)
class NossaDataClasse:

    nome = 'nome'
    sobrenome = 'sobrenome'





