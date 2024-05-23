from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']


def zipper(lst_c, lst_e):
    menor = min(len(lst_c), len(lst_e))
    return [
        ([lst_c[i], lst_e[i]]) for i in range(menor)
    ]


cidades_e_estados = zipper(cidades, estados)
print(cidades_e_estados)
print('-'*90)
# A função acima pode ser realizada através do método zip. Esse retorna um iterador gerador de tuplas.
# Em cada uma dessas tuplas estarão contidos os valores dos respectivos índices das listas passadas por parâmetro.
# Ex.:
# lista_01 = [1, 2, 3]
# lista_02 = ['a', 'b', 'c']
# lista_final = list(zip(lista_01, lista_02))
# A lista final receberá o seguinte resultado: [(1, 'a'), (2, 'b'), (3, 'c')]
print(list(zip(cidades, estados)))
# O método zip, por padrão, utiliza a menor lista como referência para gerar as tuplas.
# Caso quisermos utilizar a maior entre as listas, devemos utilizar o módulo itertools, importando a classe zip_longest.
print(list(zip_longest(cidades, estados, fillvalue='SEM CIDADE')))
# No caso de utilizarmos a com maior índice, devemos utilizar a palavra-chave fillvalue. Através dela, iremos indicar
# o que será preenchido caso o índice da lista menor não tenha nenhum valor.
