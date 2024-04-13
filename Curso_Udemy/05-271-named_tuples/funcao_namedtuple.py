# Para utilizarmos nossas tuplas nomeadas, devemos utilizar o pacote
# collection e a função namedtuple.
from collections import namedtuple

# Através da função namedtuple, criaremos uma classe chamada Carros, com os atributos
# Modelo e Motor. Também podemos definir valores padrão para nossos atributos através
# da propriedade defaults:
Carros = namedtuple('Carros', ['Modelo', 'Motor'],
                    defaults=['Polo', '1.0'])
# Abaixo criaremos uma instância de nossa Classe, onde podemos ter acesso a cada um
# dos atributos individualmente.
# Em carros_01, como não passamos nenhum valor para nossos atributos, eles terão
# seus valores padrão.
carro_01 = Carros()
print(carro_01)
carro_02 = Carros('Mustang', 'V8')
print(carro_02)
print()

# Integradas a função namedtuple, temos nossas funções asdict e astuple. Entretanto,
# as funções contidas em namedtupla são antecedidas com um underline (_):
dicionario_carro = carro_02._asdict()
print(dicionario_carro)

tupla_carro = carro_02._fields
print(tupla_carro)
print()

# Também podemos criar uma instância de nossa tupla nomeada por meio de um iterável.
# Isso pode ser feito através da função _make.
lista = ['LaFerrari', 'V12']
lista_carros = Carros._make(lista)
print(lista_carros)
