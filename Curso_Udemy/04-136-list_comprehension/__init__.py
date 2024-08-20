# -------# List Comprehension #-------
# A compreensão de listas é o processo de empacotar listas com auxílio de estruturas de repetição.
# Todavia, realizamos esse empacotamento de forma simplificada. Ex.:

lista_numeros = (num for num in range(10))

# No exemplo acima, o primeiro parâmetro num refere-se a expressão que iremos adicionar através do for,
# sendo o mesmo que:
# for num in range(10):
#     lista_numeros.append(num)

# -------# Mapeamento de dados em list comprehension #-------

# O mapeamento em list comprehension é a aplicação de uma função para cada elemento de uma sequência
# (como uma lista) para criar uma nova sequência.
produtos = [
    {'nome': 'p1', 'preco': 30},
    {'nome': 'p2', 'preco': 20},
    {'nome': 'p3', 'preco': 10}
]
novos_produtos = []

# Digamos que queremos utilizar o list comprehension no mapeamento feito abaixo:
for produto in produtos:
    if produto['preco'] > 10:
        novos_produtos.append({'nome': produto['nome'], 'preco': produto['preco'] * 1.05})
    else:
        novos_produtos.append({'nome': produto['nome'], 'preco': produto['preco']})
print(novos_produtos)
print('-'*90)

# Ficaria da seguinte maneira por meio de um list comprehension:
novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05} if (produto['preco']) > 10 else {**produto}
                  for produto in produtos]
print('list comprehension:', novos_produtos)
print('-'*90)

# No exemplo acima, utilizando o kwargs para desempacotarmos nosso dicionário. Caso desejemos que
# um dos valores sejam alterados, devemos informar a chave com o respectivo novo valor.

# ------- Filtramento de dados em list comprehension -------

# Podemos também utilizar filtros para adicionar ou não elemento em nossa nova sequência.
# Nesse caso, devemos utilizar o if após nosso for. Digamos que queremos que a condição acima seja feita
# somente para valores maiores que 20:
# Obs: Devemos utilizar **produto para que as demais chaves também sejam armazenadas no novo dicionário,
# enquanto a especificada é alterada pelo novo valor.
novos_produtos = [{**produto, 'preco': produto['preco'] * 1.05} if (produto['preco']) > 10 else {**produto}
                  for produto in produtos
                  if produto['preco'] > 20]
print(novos_produtos)
print('-'*90)

# Múltiplos for num mapeamento com list comprehension:
multiplos_valores = []

for x in range(3):
    for y in range(3):
        multiplos_valores.append((x, y))

# Com a list comprehension, ficaria desta forma:
multiplos_valores = [(x, y) for x in range(3) for y in range(3)]
print(multiplos_valores)
print('-'*90)

# Obs.: Podemos ter uma list comprehension dentro de outra list comprehension e assim por diante.
# As possibilidades vão depender da nossa necessidade.
