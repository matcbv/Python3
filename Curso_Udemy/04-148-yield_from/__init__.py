# Caso quisermos dar continuidade na contagem de um gerador por outro gerador,
# podemos utilizar o método yield from.

def gerador01():
    yield 1
    yield 2
    yield 3


def gerador02():
    # Especificando para qual função geradora queremos dar continuidade, notamos que a contagem
    # continua normalmente, sem ser interrompida.
    yield from gerador01()
    yield 4
    yield 5
    yield 6


def gerador03(gen):
    yield from gen()
    yield 4
    yield 5
    yield 6


g01 = gerador02()
for num in g01:
    print(num)
print('-'*60)

# Ainda podemos passar a função geradora que quisermos por parâmetro:
# Dessa maneira, passamos a própria função geradora, que será executada dentro da função geradora 03.
g02 = gerador03(gerador01)
for num in g02:
    print(num)
