# A função filter é responsável por realizar a filtering de um iterável por meio de uma função
# e um iterável, passados a ele por parâmetro. Dessa maneira, irá retornar um iterador com todos
# os elementos filtrados pela função que foi passada por parâmetro.
lista_produtos = [
    {'Nome': 'Carne', 'Preço': 80},
    {'Nome': 'Queijo', 'Preço': 40},
    {'Nome': 'Pão', 'Preço': 10},
    {'Nome': 'Refrigerante', 'Preço': 15},
    {'Nome': 'Suco', 'Preço': 5}
]
# Aqui, passamos um lambda, informando que só serão retornados os produtos com o preço maior que 20.
# Para tal filtragem, a função filter irá retornar True ou False para cada elemento do iterável,
# baseando-se na função passada a ela por parâmetro. Caso o elemento retorna True,
# é adicionado no iterador do filter.
produtos_acima_10 = filter(lambda produto:
                           produto['Preço'] > 20,
                           lista_produtos)
for p in produtos_acima_10:
    print(p)
