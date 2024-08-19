# --------- add() ---------

# Adiciona um elemento ao conjunto. Caso esse elemento já esteja contido no conjunto, a ação é ignorada.
random_set = {'Matheus', 'Ângela', 'Marcos'}
random_set.add('Luiz')
print(random_set)

# --------- remove() ---------

# Remove do conjunto determinado valor, caso existente. Caso contrãrio, levanta uma exceção.
random_set.remove('Luiz')
print(random_set)

# --------- discard() ---------

# Possui a mesma função de remove, porém, não levanta uma exceção caso o mesmo não exista.
random_set.discard('Luiz')
print(random_set)

# --------- clear() ---------

# Limpa por completo o conteúdo do conjunto.
random_set.clear()
print(random_set)

# --------- set_01.intersection(set_02) ---------

# Realizará a interseção de dois conjuntos, criando um terceiro apenas com os elementos existentes nos outros dois.
set_01 = {1, 2, 3}
set_02 = {3, 4, 5}
intersection_set = set_01.intersection(set_02)
print(intersection_set)
# Obs.: Também podemos realizar a operação com o operador |. Ex.:
intersection_set = set_01 | set_02
print(intersection_set)

# --------- set_01.difference(set_02) ---------

# Diferentemente do intersection, difference irá criar um novo conjunto com os elementos não existentes nos conjuntos.
difference_set = set_01.difference(set_02)
print(difference_set)
# Obs.: Também podemos realizar a operação com o operador %. Ex.:
intersection_set = set_01 - set_02
print(intersection_set)

# --------- set_01.symmetric_difference(set_02) ---------

# Criará um terceiro conjunto contendo apenas os valores exclusivos entre dois outros conjuntos.
symmetric_difference_set = set_01.symmetric_difference(set_02)
print(symmetric_difference_set)
# Obs.: Podemos realizar a operação com o operador ^. Ex.:
symmetric_difference_set = set_01 ^ set_02
print(symmetric_difference_set)

# --------- set_01.symmetric_difference_update(set_02) ---------

# Possui a mesma função do symmetric_update, porém, ao invés de criar um terceiro conjunto, irá alterar o primeiro.
set_01.symmetric_difference_update(set_02)
print(set_01)
set_01 ^= set_02
print(set_01)
