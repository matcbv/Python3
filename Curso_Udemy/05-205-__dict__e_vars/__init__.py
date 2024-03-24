# O método especial __dict__ é responsável por retornar um dicionário contendo o mapeamento de uma
# instância feita pelo interpretador Python. No conteúdo do dicionário, veremos todos os atributos
# criados e seus respectivos valores.

class Lista:
    def __init__(self, **kwargs):
        self.item_01 = 'valor'
        self.item_02 = 'valor_02'
        self.item_03 = 'valor_03'


listagem = Lista()
print(listagem.__dict__)

# O método especial __dict__ também tem a função de adicionar ou modificar atributos e seus
# respectivos valores:
listagem.__dict__['item_04'] = 'valor_04'
listagem.__dict__['item_01'] = 'valor_01'

# Ao invés do __dict__, podemos utilizar uma função embutida do Python chamada vars. Essa, contudo,
# só consegue exibir o dicionário, e não modificá-lo.
print(vars(listagem))

# O método especial __dict__ pode ser muito útil para armazenarmos nossos atributos em JSON, ou
# recriarmos nossos atributos em outra instância. Ex.:

dicionario_especial = listagem.__dict__


class ListaNova:
    def __init__(self, item_01, item_02, item_03, item_04):
        self.item_01 = item_01
        self.item_02 = item_02
        self.item_03 = item_03
        self.item_04 = item_04


listagem_nova = ListaNova(**dicionario_especial)
print(vars(listagem_nova))
