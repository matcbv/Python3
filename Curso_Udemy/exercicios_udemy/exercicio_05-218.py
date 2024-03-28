class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor_carro):
        self._motor = motor_carro.motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante_carro):
        self._fabricante = fabricante_carro.fabricante


class Motor:
    def __init__(self, motor):
        self.motor = motor


class Fabricante:
    def __init__(self, fabricante):
        self.fabricante = fabricante
        self._carros = []

    @property
    def carros(self):
        return self._carros

    @carros.setter
    def carros(self, lista_carros):
        for c in lista_carros:
            self._carros.append(c)

    def listar_carros(self):
        for carro in self._carros:
            print(carro.nome)


carro_01 = Carro('Mustang')
motor_01 = Motor('V8')
fabricante_01 = Fabricante('Ford')
carro_02 = Carro('Ford GT')

carro_01.motor = motor_01
carro_01.fabricante = fabricante_01
fabricante_01.carros = (carro_01, carro_02)

fabricante_01.listar_carros()
print(carro_01.nome, carro_01.motor, carro_01.fabricante)
