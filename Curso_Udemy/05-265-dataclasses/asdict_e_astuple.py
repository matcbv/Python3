# No módulo dataclasses, também temos outras funções que podem nos auxiliar nos
# procedimento envolvendo nossas instâncias. Duas delas são asdict e astuple,
# responsáveis por transformar nossas instâncias em dicionários e tuplas, respectivamente.
from dataclasses import dataclass, asdict, astuple


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


pessoa = Pessoa('Matheus', 'Cerqueira')
dicionario_pessoa = asdict(pessoa)
tupla_pessoa = astuple(pessoa)
print(dicionario_pessoa, type(dicionario_pessoa))
print(tupla_pessoa, type(tupla_pessoa))
