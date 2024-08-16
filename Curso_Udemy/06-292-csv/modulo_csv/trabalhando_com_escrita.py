from pathlib import Path
import csv

csv_path = Path().absolute() / 'banco_de_dados_interno.csv'

csv_list_dict = [
    {'Nome': 'Matheus', 'Sobrenome': 'Cerqueira', 'Idade': '22', 'Endereço': 'Rua do Quincão, 277 - Centro'},
    {'Nome': 'Lucas', 'Sobrenome': 'Silva', 'Idade': '18', 'Endereço': 'Rua Nelson Viana, 30 - Centro'},
    {'Nome': 'Daniel', 'Sobrenome': 'Lima', 'Idade': ' 34', 'Endereço': 'Avenida Circular Ocidental, 344 - Nova Niterói'}
]

csv_list = [
    ['Matheus', 'Cerqueira', 22, 'Rua do Quincão, 277 - Centro'],
    ['Lucas', 'Silva', 18, 'Rua Nelson Viana, 30 - Centro'],
    ['Daniel', 'Lima', 34, 'Avenida Circular Ocidental, 344 - Nova Niterói']
]

# Escrevendo dados contidos em listas:

# Ex. 1: Listas contendo listas
# Ao trabalharmos com arquivos csv, é recomendado utilizar o parâmetro newline, definindo-o como uma string vazia.
# Isso impede a criação de uma nova linha ao final de cada linha escrita.
with open(csv_path, 'w', encoding='utf-8', newline='') as file:
    # Abaixo, iremos criar um objeto escritor para escrevermos nossos dados no arquivo desejado.
    writer = csv.writer(file)
    for row in csv_list:
        # Com o método writerow, escreveremos uma linha em nosso arquivo csv.
        # Também há o método writerows, que pode escrever várias linhas de uma única vez.
        # Ao trabalharmos com ele, passaremos um iterável contendo várias listas, ao invés de uma única lista.
        writer.writerow(row)
    # Utilizando writerows:
    writer.writerows(csv_list)

# Ex. 2: Listas contendo dicionários
with open(csv_path, 'w', encoding='utf-8', newline='') as file:
    # Com dicionários, devemos obter primeiramente os nomes de suas colunas:
    columns_names = csv_list_dict[0].keys()
    writer = csv.writer(file)
    # Abaixo, escreveremos o nome de suas colunas e, em seguida, suas linhas.
    writer.writerow(columns_names)
    for row in csv_list_dict:
        writer.writerow(row.values())

# Escrevendo dados contidos em dicionários:

with open(csv_path, 'w', encoding='utf-8', newline='') as file:
    calumns_names = csv_list_dict[0].keys()
    # Em dicionários, também podemos utilizar o método DictWriter. Junto dele, devemos definir
    # o valor do parâmetro fieldnames, que são os nomes das colunas que obtemos acima.
    writer = csv.DictWriter(file, fieldnames=calumns_names)
    # Com o método writeheader, escrevemos em nosso arquivo, o nome das colunas obtidos.
    writer.writeheader()
    for dict_ in csv_list_dict:
        # Já com writerow, conseguimos escrever nossas linhas passando nossos dicionários por parâmetro.
        writer.writerow(dict_)
