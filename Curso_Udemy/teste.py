from datetime import datetime


class Dados:
    def __init__(self, valor):
        self.dado = valor


class BancoDeDados:
    def __init__(self):
        self.logs = []
        self.dados = []
        self.dado = None

    def mostrar_dados(self):
        for d in self.dados:
            print(self.logs[-1], '-', d)

    def recebe_dados(self, dado):
        self.dado = Dados(dado)
        self.dados.append(self.dado.dado)
        horario = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.logs.append(horario)


obj = BancoDeDados()
obj.recebe_dados('Um texto qualquer')
obj.mostrar_dados()
obj.recebe_dados('Outro texto')
obj.mostrar_dados()
