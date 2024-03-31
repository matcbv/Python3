# A função map é responsável por retornar um iterador, contento o mapping feito por uma função passada
# a ele por parâmetro.
lista_produtos = [
    {'Nome': 'Carne', 'Preço': 80},
    {'Nome': 'Queijo', 'Preço': 40},
    {'Nome': 'Pão', 'Preço': 10},
    {'Nome': 'Refrigerante', 'Preço': 15},
    {'Nome': 'Suco', 'Preço': 5}
]


def calc_preco(produto):
    if produto['Preço'] > 20:
        return produto['Preço'] * 90 / 100
    else:
        return produto['Preço']


# A função map irá entregar cada um dos elementos contidos na lista lista_produto para
# a função calc_preco.
# Obs.: Também podemos passar mais de um iterável para o método map.
# A estrutura da função é: map(função, *iteráveis)
novos_precos = map(calc_preco, lista_produtos)
for p in novos_precos:
    print(p)

print('-'*15)

# Caso a função seja simples, podemos passar como uma função lambda:
novos_precos = map(lambda produto:
                   produto['Preço'] * 90 / 100 if produto['Preço'] > 20 else produto['Preço'],
                   lista_produtos)
for p in novos_precos:
    print(p)
