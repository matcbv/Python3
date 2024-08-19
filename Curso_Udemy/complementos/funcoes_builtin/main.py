# --------- range(start, stop, step) ---------

# Com range, obtemos uma sequência numérica através dos índices passados por parâmetro.
# O stop é obrigatório, já start e step são opcionais.
range_interval = range(0, 10, 2)
for i in range_interval:
    print(i)


# --------- round(número, ‘número de casas decimais’) ---------

# Com round, realizamos a formatação de um número real.
random_number = 11.11
rounded_number = round(11.19, 1)
print(rounded_number)

# --------- len() ---------

# Com len, obtemos o comprimento do objeto em questão.
# Obs.: Se inicia pelo índice 1.
random_phrase = 'Essa é uma frase de exemplo'
print(len(random_phrase))

# --------- max() ---------

# Com max, obtemos o maior valor contido em um objeto, seja numérico ou alfabético.
number_list = [1, 2, 3, 4, 5]
print(max(number_list))

# --------- min() ---------

# Com min, obtemos o menor valor contido em um objeto, seja numérico ou alfabético.
print(min(number_list))

# --------- sum() ---------

# Com sum, é retornado a soma de todos os valores numéricos de um objeto.
print(sum(number_list))

# --------- sorted() ---------

# Com sorted, conseguimos ordenar os valores de determinado objeto.
unordered_list = ['b', 'a', 'd', 'e', 'c']
ordered_list = sorted(unordered_list)
print(ordered_list)
