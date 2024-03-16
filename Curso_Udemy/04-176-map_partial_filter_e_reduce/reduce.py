from functools import reduce

lista_produtos = [
    {'Nome': 'Carne', 'Preço': 80},
    {'Nome': 'Queijo', 'Preço': 40},
    {'Nome': 'Pão', 'Preço': 10},
    {'Nome': 'Refrigerante', 'Preço': 15},
    {'Nome': 'Suco', 'Preço': 5}
]


# Ao criarmos uma função para acumularmos os elementos do iterável informado, nosso acumulador terá
# o valor inicial passado a ele através do método reduce (nesse caso 0). A cada iteração, a função
# soma_acumulador será chamada, onde produto irá receber um dos elementos do iterável, retornando a soma
# do valor do acumulador com o elemento chaveado Preço. Na próxima chamada, o valor do acumulador será
# o retornado. Esse processo irá se repetir até que o iterador seja esgotado.
def soma_acumulador(acumulador, produto):
    return acumulador + produto['Preço']


soma_precos = reduce(soma_acumulador, lista_produtos, 0)
print(soma_precos)
print('-'*10)

# Podemos simplificar o código acima utilizando uma função lambda:
soma_precos = reduce(lambda acumulador,produto: acumulador + produto['Preço'], lista_produtos, 0)
print(soma_precos)
