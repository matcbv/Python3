class Produtos:
    def __init__(self, produto, preco, codigo):
        self.produto = produto
        self.preco = preco
        self.codigo = codigo
        self._dicionario = {}

    @property
    def dicionario(self):
        return self._dicionario

    @dicionario.setter
    def dicionario(self, inst):
        self._dicionario = inst

class Listagem:
    def __init__(self, produto, preco, codigo):
        i = len(self.lista)
        self.lista.update({i: {Produtos(produto=produto, preco=preco, codigo=codigo)}})


    def listar(self):
        for k, v in self.lista.items():
            print(f'{k}: ', end='')
            for e in v:
                print(e.produto, e.preco, e.codigo, sep='; ')


obj = Listagem('Papel', 10, 1)
obj_02 = Listagem('Caneta', 5, 2)
obj.listar()
del obj_02
obj.listar()
