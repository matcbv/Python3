from funcoes import reverter_JSON


class NovaListaPessoas:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


dados_revertidos = reverter_JSON()
nova_pessoa = NovaListaPessoas(**dados_revertidos)
print(vars(nova_pessoa))
