# O método count é responsável por realizar uma contagem infinita, ao contrário do método range.
# Para utilizarmos o count, devemos importar o módulo itertools. Ex.:
from itertools import count

# O count, assim como o range, é um iterável. A diferença entre eles é que count também é um iterador.
print('count:', hasattr(count, '__iter__'))
print('count:', hasattr(count, '__next__'))
print('range', hasattr(range, '__iter__'))
print('range', hasattr(range, '__next__'))

# Quando utilizamos uma estrutura de repetição, a estrutura irá utilizar o método (iter()) para obter
# o iterador do objeto. Ex.: for c in lista -> iterador = iter(lista), e então c = next(iterador).
# Como o count já é um iterador, ao utilizarmos o método iter, ele mesmo é retornado.
contador = count()
for c in contador:
    if c == 100:
        break
    print(contador)
