# Fará uma cópia do dicionário em questão, não associando as informações contidas nele.
# Essa cópia irá enviar somente dados imutáveis para o objeto a ser atribuído,
# enquanto mutáveis (listas, dicionários, etc.) também serão associadas entre o dicionário e o objeto em questão.
# Esse evento é chamado de shallow copy (cópia rasa).
# Caso desejemos que todos os elementos do nosso dicionário sejam copiados,
# devemos importar o módulo copy, e utilizar o método deepcopy(‘dicionario’).
from copy import deepcopy

lista01 = [1, 2, 3, {'Número final': 999}]
print(lista01)
# Iremos realizar uma cópia rasa de nossa lista01.
lista02 = lista01.copy()
print(lista02)
lista02[3]['Número final'] = 1000
# Ao alterarmos nosso dicionário no interior da lista02, a lista01 também é afetada.
print(lista01, lista02)

# Desta maneira, os iteráveis contidos na lista 01 não serão mais vinculados a lista02
# e seus valores não serão alterados.
lista02 = deepcopy(lista01)
lista02[3]['Número final'] = 0
print(lista01, lista02)
