# --------- split(separador, número_de_elementos) ---------

# Transforma uma string em uma lista, onde, por padrão, utiliza cada espaço da frase como separados.
# Obs.: Podemos especificar nos parâmetros, o separador a ser utilizado e a quantidade de elementos a serem criados.
# Ex. 1:
random_phrase = 'Uma frase qualquer criada para exemplo'
random_list = random_phrase.split()
print(random_list)
# Ex. 2:
random_phrase = 'Uma_frase_qualquer_criada_para_exemplo'
random_list = random_phrase.split('_', 3)
print(random_list)

# --------- join() ---------

# Com o método join, conseguimos unificar nossa lista em uma string, juntando os elementos contidos nela.
# Iremos especificar o separador pela string ao início da chamada. No abaixo acima, utilizaremos o espaço.
' '.join(random_list)
# Obs.: O método join altera a própria lista.
