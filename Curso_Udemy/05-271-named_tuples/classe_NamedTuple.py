# Além da função namedtuple, podemos importar a classe NamedTuple do módulo typing para
# criarmos nossas classes.
from typing import NamedTuple


# Teremos o mesmo resultado de quando criamos nossa classe com a função namedtuple.
class Carros(NamedTuple):
    modelo: str
    sobrenome: str


carro_01 = Carros('Tiguan', '2.0 TSI')
print(carro_01)
