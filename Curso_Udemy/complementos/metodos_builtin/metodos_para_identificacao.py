# --------- count('x', start, stop) ---------

# Com count, obtemos a quantidade de repetições de determinado valor em um objeto.
random_phrase = 'Essa é uma frase aleatória criada para exemplo.'
print(f'A frase possui {random_phrase.count(' ', 5, 15)} entre os índices 5 e 15.')

# --------- find('x', start, stop) ---------

# Com find, será retornado o índice da primeira aparição de determinado valor em um objeto.
print('A primeira aparição da letra s a partir do índice 3 está em:', random_phrase.find('s', 3))
# Obs.: Caso a substring não seja encontrada, o valor -1 é retornado.

# --------- rfind('x', start, stop) ---------

# Semelhante a find, o rfind inicia sua busca a partir do fim do objeto.
print('A primeira aparição da letra i a partir do final do objeto está em:', random_phrase.rfind('i'))

# --------- index('x', start, stop) ---------

# O método index possui a mesma função de find, entretanto, caso a substring não seja encontrada, levanta uma exceção
# do tipo ValueError contendo a mensagem "substring not found".
print('A primeira aparição da letra x está em:', random_phrase.find('x'))
