# No módulo itertools, temos mais alguns métodos que podem ser muito úteis em certos momentos.
# Alguns desses módulos são:
# - combinations: Realiza uma combinação de todos os elementos contidos em um iterável, ignorando as
# combinações repetidas (com elementos iguais, mas em posições diferentes).
# - permutations: Realiza uma combinação de todos os elementos contidos em um iterável, considerando
# também as combinações repetidas.
# - product: Realiza o produto entre os elementos de diferentes iteráveis,
# ignorando combinações repetidas.
from itertools import combinations, permutations, product

nomes = ['matheus', 'mariana', 'thomaz', 'thalia']
vestuario = [['camiseta', 'bermuda'], ['p', 'm', 'g']]
print(*list(combinations(nomes, r=2)))
print(*list(permutations(nomes, r=2)))
print(*list(product(*vestuario)))
