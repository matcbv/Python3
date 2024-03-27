# A agregação é um subconjunto da associação. Nesse conjunto, os dois objetos também são relacionados e
# funcionam separadamente, mas necessitam um do outro para uma determinada função.

class Carrinho:
    def __init__(self):
        self._produtos = []

    def recebe_produtos(self, *lista):
        for i in lista:
            self._produtos.append(i)

    def soma_valores(self):
        return sum(p.preco for p in self._produtos)

    def lista_produtos(self):
        for i in self._produtos:
            print(i.nome, i.preco)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
prod_01, prod_02 = Produto('Produto 01', 20), Produto('Produto 02', 10)
# Estaremos passando as instâncias da classe produto para o método recebe_produtos da classe Carrinho, que irá
# armazenar os atributos das instâncias no atributo _produtos da classe Carrinho.
carrinho.recebe_produtos(prod_01)
carrinho.recebe_produtos(prod_02)
# Dessa forma, podemos acessar as informações passadas para as instâncias da classe Produto pela classe Carrinho.
carrinho.lista_produtos()
preco_total = carrinho.soma_valores()
print(preco_total)

# Nessa associação vemos que a Classe produtos agrega objetos para a classe Carrinho. Elas podem existir separadamente,
# porém juntas, podem realizar todas as suas funções.
