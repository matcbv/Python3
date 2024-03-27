class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.motor = None
        self.fabricante = None


class Motor:
    def __init__(self, motor):
        self.motor = motor

    def atribuir_motor(self, carro):
        carro.motor = self.motor


class Fabricante:
    def __init__(self, fabricante):
        self.fabricante = fabricante
        self.carros = []

    def atribuir_fabricante(self, carro):
        carro.fabricante = self.fabricante

    def adicionar_carro(self, *carro):
        for c in carro:
            self.carros.append(c)

    def listar_carros(self):
        for carro in self.carros:
            print(carro.carro)


carro_01 = Carro('Mustang')
motor_01 = Motor('V8')
fabricante_01 = Fabricante('Ford')
carro_02 = Carro('Ford GT')

motor_01.atribuir_motor(carro_01)
fabricante_01.atribuir_fabricante(carro_01)
fabricante_01.adicionar_carro(carro_01, carro_02)

fabricante_01.listar_carros()
print(carro_01.carro, carro_02.motor, carro_01.fabricante)
