# Com o módulo csv, conseguimos trabalhar com arquivos do tipo csv.
import csv
from pathlib import Path

csv_path = Path().absolute().parent / 'banco_de_dados.csv'

with open(csv_path, 'r', encoding='utf-8') as file:
    # Através do método reader, obtemos um iterador que gera listas, cada uma representando uma das linhas
    # de nosso arquivo csv. Em cada uma das listas, haverá os valores da respectiva linha.
    reader = csv.reader(file)
    for row in reader:
        # Assim, conseguimos manipular tais listas normalmente. Abaixo, iremos exibir
        # somente os endereços contidos em nossa tabela:
        print(row[-1])
print()
# Também podemos obter nossas linhas por meio de um iterador que gera dicionários ao invés de lista.
# Isso pode ser feito através do método DictReader:
with open(csv_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Assim como as lista, podemos manipular nosso dicionário da maneira que desejarmos.
        print(row['Nome'])
