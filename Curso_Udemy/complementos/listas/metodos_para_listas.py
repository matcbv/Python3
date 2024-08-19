# --------- append(objeto) ---------
import random

# Adiciona o objeto passado por parâmetro ao final da lista em questão.
random_list = [1, 2, 3, 4]
random_list.append(5)
print(random_list)

# --------- insert(i, objeto) ---------

# Insere determinado objeto na posição especificado no parâmetro.
random_list.insert(5, [6, 7, 8])
print(random_list)

# --------- del list[i] ---------

# Deletamos determinado elemento contido na lista em questão.
del random_list[5]
print(random_list)

# --------- pop() ---------

# Elimina e retorna o último índice contido na lista em questão.
last_element = random_list.pop()
print(last_element)
print(random_list)

# --------- remove(objeto) ---------

# Remove da nossa lista, todos os objetos iguais ao passado por parâmetro.
random_list.remove(1)
print(random_list)

# --------- sort() ---------

# Ordena determinada lista em ordem crescente ou alfabética, de acordo com seu conteúdo.
random.shuffle(random_list)
print(random_list)
random_list.sort()
print(random_list)
# Podemos estar ordenando em ordem decrescente com o parâmetro reverse=True.
random_list.sort(reverse=True)
print(random_list)
