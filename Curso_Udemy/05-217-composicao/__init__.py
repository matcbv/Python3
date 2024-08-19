# A composição é uma especificação da agregação. Nela, como o próprio nome diz, uma classe compõe a outra.
# Caso uma das classes da composição seja apagada, as referências a ela contidas na outra classe também serão.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def obter_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def obter_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def exibir_informacoes(self):
        print('Nome:', self.nome)
        print('-' * 20)
        for endereco in self.enderecos:
            print('Rua:', endereco.rua)
            print('Número:', endereco.numero)
            print('-' * 20)
        print('# FIM')


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


pessoa = Cliente('Matheus')
pessoa.obter_endereco('Rua do Quincão', 277)
endereco_cliente = Endereco('Rua Barão do Rio Branco', 254)
pessoa.obter_endereco_externo(endereco_cliente)
pessoa.exibir_informacoes()

# Agora, caso deletarmos a instância da classe Cliente criada, as instâncias da classe Endereco vinculadas a instância
# enderecos serão perdidos. Entretanto, o endereco externo adicionado, ainda existirá, podendo ser acessado através da
# classe Endereco.

del pessoa
print('Rua:', endereco_cliente.rua)
print('Número:', endereco_cliente.numero)
