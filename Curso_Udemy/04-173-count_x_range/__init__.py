# O método count é responsável por realizar uma contagem infinita, ao contrário do método range.
# Para utilizarmos o count, devemos importar o módulo itertools. Ex.:
from itertools import count

# O count, assim como o range, é um iterável. A diferença entre eles é que count também é um iterador.
print('count:', hasattr(count, '__iter__'))
print('count:', hasattr(count, '__next__'))
print('range', hasattr(range, '__iter__'))
print('range', hasattr(range, '__next__'))
print('-' * 15)

# Quando utilizamos uma estrutura de repetição, a estrutura irá utilizar o método (iter()) para obter
# o iterador de um objeto iterável. Ex.: for c in lista -> iterador = iter(lista), e então c = next(iterador).
# Como o count já é um iterador, ao utilizarmos o método iter, ele mesmo é retornado.
contador = count()
for c in contador:
    if c == 100:
        break
    print(contador)

# Ao contrário do método range, não podemos definir um fim para o método count,
# somente um ínicio e um salto. Ex.:

# Nesse contador, estaremos exibindo somente os números pares, iniciando a contagem em 0 e pulando a cada 2.
contador = count(0, 2)
# Já abaixo, teremos um range que irá começar no 0, pulando a cada dois, contando até o número 100.
contagem_range = range(0, 2, 100)
