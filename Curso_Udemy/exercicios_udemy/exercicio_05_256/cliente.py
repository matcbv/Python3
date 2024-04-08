class Pessoa:
    def __init__(self, nome, idade):
        self.obter_nome = nome
        self.obter_idade = idade

    @property
    def obter_nome(self):
        return self._nome

    @obter_nome.setter
    def obter_nome(self, nome):
        self._nome = nome

    @property
    def obter_idade(self):
        return self._idade

    @obter_idade.setter
    def obter_idade(self, idade):
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, *contas):
        super().__init__(nome, idade)
        self.contas = contas
