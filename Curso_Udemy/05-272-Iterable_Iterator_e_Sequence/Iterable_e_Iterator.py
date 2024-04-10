# Através das classes Iterator e Iterable, podemos criar nossos próprios iteráveis e iteradores
from collections.abc import Iterator, Iterable


# Tais classes acima serão herdadas pelas nossas classes Iteravel e Iterador.
# A classe Iterable possui como método abstrato o método especial __init__.
# Já a classe Iterator, possui __init__ e __next__ como métodos abstratos.
class Iteravel(Iterable):
    def __init__(self, *iteravel):
        self.iteravel = list(iteravel)

    def __iter__(self):
        return Iterador(self.iteravel)


class Iterador(Iterator):
    def __init__(self, iteravel):
        self.iteravel = iteravel
        self.index = 0

    # Nosso Iterador também terá o método especial __iter__ e retornará ele mesmo.
    # Isso ocorre por prevenção no caso de nosso iterador for iterado. Como ele já é
    # um iterador, ele mesmo será o resultado.
    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iteravel):
            self.index = 0
            raise StopIteration
        valor = self.iteravel[self.index]
        self.index += 1
        return valor


# Primeiro estaremos criando nosso iterável:
obj_iteravel = Iteravel('Matheus', 'Cerqueira', 'Baião', 'Victor')
# Chamando o método __iter__, criamos o iterador de nosso iterável
iterador = obj_iteravel.__iter__()
# Dessa forma, conseguimos iterar através de nosso iterador por meio do método __next__:
print(iterador.__next__())
# Ou com estruturas de repetição, como o for:
for v in iterador:
    print(v)
