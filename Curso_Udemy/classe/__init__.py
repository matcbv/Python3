from datetime import datetime


class Carros:
    ano_atual = datetime.today().year

    def __init__(self, modelo, fabricante, ano, tempoUso, acelerando=False, freiando=False):
        self.modelo = modelo
        self.fabricante = fabricante
        self.ano = ano
        self.tempoUso = tempoUso
        self.acelerando = acelerando
        self.freiando = freiando

    def acelerar(self):

        if self.acelerando:
            print('O carro já está acelerando.')
        else:
            print('O carro começou a acelerar...')
            self.acelerando = True

    def freiar(self):
        if self.freiando:
            print('O carro já está freiando.')
        elif not self.acelerando:
            print('O carro está parado.')
        else:
            print('O carro começou a freiar...')
            self.freiando = True

    @classmethod
    def tempoUsoCalc(cls, modelo, fabricante, ano):
        tempoUso = cls.ano_atual - ano
        return cls(modelo, fabricante, ano, tempoUso)

    @staticmethod
    def mediaKM(tempo, KM):
        media = KM/tempo
        return media
