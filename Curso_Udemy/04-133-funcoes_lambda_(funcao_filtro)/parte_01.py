def filtrar(item):
    return item['nome']


lista_para_filtro = [{'nome': 'Pedro', 'Idade': 23},
                     {'nome': 'Carlos', 'Idade': 40},
                     {'nome': 'Daniel', 'Idade': 32},
                     {'nome': 'Mariana', 'Idade': 29},
                     {'nome': 'Matheus', 'Idade': 21}]

# Podemos utilizar funções para nos auxiliar com a filtragem de dicionários.
# Para isso, devemos criar uma função que irá receber o primeiro elemento e retornar
# com a chave que queremos realizar a filtragem. Nesse caso, nós não iremos chamar a função
# somente referenciá-la. Ex.:

# lista_para_filtro.sort(key=filtrar)
print(lista_para_filtro)

# Podemos simplificar o que realizamos acima através das chamadas funções lambda.
# Tais funções não possuem nome, sendo funções mais curtas, feitas em uma só linha. Ex.:
print()
lista_para_filtro.sort(key=lambda item: item['nome'])
print(lista_para_filtro)

# A estrutura delas se trada da seguinte forma:
# lambda (palavra-chave) (nome do(s) parâmetro(s): (return com as operações dos parâmetros)
