# Uma classe se torna agregada a outra se a associação entre elas é vital para seu funcionamento.
class VerifDivisor:

    def __init__(self):
        self._num = None

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, valor):
        self._num = valor
        while self._num <= 0:
            self._num = int(input('Informe um divisor maior do que 0: '))


class Divisao:

    def __init__(self, dividendo):
        self.dividendo = dividendo
        self.ferramentaVerif = VerifDivisor()

    def dividir(self):
        result = self.dividendo / self.ferramentaVerif.num
        print(f'{result:.2f}')


divisao = Divisao(int(input('Qual o dividendo? ')))
divisao.ferramentaVerif.num = int(input('Qual o divisor? '))
divisao.dividir()

# Nesse exemplo acima, as funções ‘Divisao’ e ‘VerifDivisao’ podem existir por si mesmas,
# porém para serem completamente funcionais, precisam umas das outras.
# Assim como a classe ‘Divisao’ poderia receber um divisor inválido,
# a classe ‘VerifDivisao’ recebe o divisor a ser verificado com o auxílio da classe ‘Divisao’.
