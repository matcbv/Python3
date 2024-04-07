# Para criarmos docstrings, devemos utilizar aspas triplas.
# As docstrings representam nossa documentação para um determinado item.
# Podemos criá-las em uma só linha:
"""Essa é uma docstring em uma linha"""
# Ou tem várias linhas:
"""
Essa é uma docstring de várilhas linhas.

Podemos utilizar espaços e quebras de linha em seu interior.
"""


# Podemos adicionar docstring em diversos objetos em Python além de módulos.
# Exemplos desses objetos são: metaclasses, classes, funções, métodos, etc.
# Exemplo de uma docstring em uma função:
def somar(x, y):
    """
    Soma x e y

    Essa função é responsável por somar dois números inteiros ou flutuantes,
    retornando seu resultado.

    :param x: Primeiro número.
    :param y: Segundo número.
    :return: Resultado da soma.
    """
    resultado = x + y
    return resultado


# Exemplo de uma docstring em uma classe:
class Foo:
    """
    Classe Foo

    Classe responsável por receber dois valores e repassá-los para a classe multiplica.

    """
    def __init__(self, valor_01, valor_02):
        self.valor_01 = valor_01
        self.valor_02 = valor_02

    # Ainda podemos adicionar docstrings em nossos métodos:
    def mutiplica(self):
        """
        Multiplicar valor_01 e valor_02

        :return: Resultado da multiplicação entre os dois valores.
        """
        resultado = self.valor_01 + self.valor_02
        return resultado

