class Teste:
    def __init__(self, valor):
        self.valor = valor

    def funcao_teste_01(self):
        print(self.valor)


class OutroTeste:
    def __init__(self):
        self.classe = Teste

    def funcao_teste_02(self):
        instancia = self.classe('aoba')
        self.classe.funcao_teste_01(instancia)


obj = OutroTeste()
obj.funcao_teste_02()
