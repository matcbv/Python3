import funcoes


class ListaPessoas:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


pessoa = ListaPessoas('Matheus', 'Cerqueira', 21)
dados_pessoa = pessoa.__dict__
funcoes.converter_para_JSON(dados_pessoa)
