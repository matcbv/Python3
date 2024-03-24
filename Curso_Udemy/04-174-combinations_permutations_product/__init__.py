# No módulo itertools, temos mais alguns métodos que podem ser muito úteis em certos momentos.
# Alguns desses módulos são:
# - combinations: realiza uma combinação de todos os elementos contidos em um iterável, ignorando as
# combinações repetidas (com elementos iguais, mas em posições diferentes).
# - permutations: realiza uma combinação de todos os elementos contidos em um iterável, considerando
# também as combinações repetidas.
# - product: realiza o produto entre os elementos de diferentes iteráveis,
# ignorando combinações repetidas.
from itertools import combinations, permutations, product

nomes = ['matheus', 'mariana', 'thomaz', 'thalia']
vestuario = [['camiseta', 'bermuda'], ['p', 'm', 'g']]
# Com o argumento r, definimos a quantidade de valores contidos em cada combinação gerada.
# Obs.: As combinações são geradas em tuplas.
print(*list(combinations(nomes, r=2)))
print(*list(permutations(nomes, r=2)))
print(*list(product(*vestuario)))
