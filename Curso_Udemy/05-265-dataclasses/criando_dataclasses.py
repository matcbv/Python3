# Dataclasses são shorthands para criação de nossas classes. Podemos utilizá-las por meio
# do módulo dataclasses. Tal módulo nos disponibiliza um decorador e funções para criação
# de métodos como __init__, __repr__, __eq__, etc. Tais meios fornecidos, irão nos poupar
# dos detalhes durante a criação da classe, simplificando consideravelmente o processo.
from dataclasses import dataclass


# Utilizando o decorador dataclass para criarmos uma classe através do módulo dataclasses:
@dataclass
class ClasseComDataclasses:
    # Para criarmos nossos atributos, basta informarmos seus nomes e tipos, separando-os
    # por dois pontos (:).
    nome: str
    idade: int


pessoa_01 = ClasseComDataclasses('Matheus', 21)
pessoa_02 = ClasseComDataclasses('Davi', 17)
# Além disso, ele também já adiciona métodos especiais, como __repr__ e __eq__:
# __repr__:
print(pessoa_01)
# __eq__:
print(pessoa_01 == pessoa_02)
