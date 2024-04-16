import random

# Com o método randint definimos um número inteiro aleatório passando um começo e fim para as escolhas:
print('randint:', random.randint(1, 10))
print()

# Com o método randrange definimos um número inteiro aleatório passando um começo e fim para as escolhas
# e tendo a opção de informar um salto. No exemplo abaixo, só número pares serão selecionados
print('randrange:', random.randrange(0, 10, 2))
print()

# Com o método uniform definimos um número flutuante aleatório passando um começo e fim para as escolhas.
# Podemos definir o número de casas flutuantes ao exibí-lo caso quisermos:
rand_float = random.uniform(1, 10)
print(f'randfloat: {rand_float:.2f}')
print()

# Com o método shuffle, conseguimos embaralhar os valores contidos em uma lista.
# Obs.: O shuffle altera a lista original, não cria uma nova.
lista_nomes = ['Matheus', 'Lucas', 'Pedro', 'Ailton', 'Marcos']
random.shuffle(lista_nomes)
print('shuffle:', lista_nomes)
print()

# Caso quisermos embaralhar uma lista sem alterar a lista original, ou seja, criando uma nova lista,
# podemos utilizar o método sample.
# Junto de sample, também temos o parâmetro k, que define o número de índices que nossa nova lista terá.
# Obs.: Para criarmos uma nova lista de mesmo tamanho da original, basta utilizarmos k=len(lista_original).
nova_lista = random.sample(lista_nomes, k=3)
print('sample:', nova_lista)
print()

# O método choices é semelhante ao método sample, porém, permite a repetição de valores em nossa nova lista.
# No caso de choices, o valor padrão de k é 1, sendo opcional alterá-lo.
nova_lista_com_repeticao = random.choices(lista_nomes, k=2)
print('choices:', nova_lista_com_repeticao)
print()

# O método choice é responsável por selecionar um elemento aleatório de nosso iterável:
print(random.choice(lista_nomes))
