from dataclasses import dataclass


# Temos diversas configurações em nossas que podemos ou não habilitar. Duas delas são:
# frozen - 'Congela' nossa classe, impossibilitando a criação de novos atributos através de
# suas instâncias. Só poderemos utilizar os valores que instanciamos na criação da instância.
# order - Realiza a ordenação de nossas instâncias. Por padrão, utiliza sempre o primeiro
# atributo contido nas instâncias para ordená-las. Caso quisermos ordenar por outro valor,
# devemos atribuir False a função order.
# Obs.: ordem e frozen vem como False por padrão.
@dataclass(frozen=True, order=True)
class Pessoa:
    nome: str
    sobrenome: str


lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'), Pessoa('C', 'X')]
lista_ordenada = sorted(lista)
print(lista_ordenada)
