# O empacotamento e desempacotamento de iteráveis em Python, é o ato de armazenarmos ou retirarmos
# uma quantidade n de valores em um iterável, armazenando tais valores em uma lista. Ex.:

nomes = ['Matheus', 'Mariana', 'Thomaz', 'Thalia']
# Utilizado o asterisco (*), indicamos que queremos empacotar ou desempacotar nossos elementos.
# Empacotando:
a, b, *c = nomes
print(a, b, c, sep=', ')
# Desempacotando:
print(a, b, *c, sep=', ')

# Por convenção, quando iremos empacotar itens que não iremos utilizar, utilizamos o símbolo de underline (_).
# Ex.: Digamos que queremos apenas os itens de índice 0, 1 e 4:

tupla = (0, 1, 2, 3, 4)
zero, um, *_, quatro = tupla
# Os itens acima com o símbolo _ não serão de uso em nosso código, por mais que ainda estejam
# armazenados nos elementos de nome _.
print(zero, um, _, quatro, sep=', ')
