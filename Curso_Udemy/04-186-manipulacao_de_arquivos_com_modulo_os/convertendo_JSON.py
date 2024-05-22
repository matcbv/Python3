# Para convertemos um objeto para JSON, podemos utilizar o módulo json, pertencente a biblioteca padrão do Python.
import json

path = "H:\\GitHub\\Python3\\Curso_Udemy\\04-186-manipulacao_de_arquivos_com_modulo_os\\banco_de_dados\\dados_JSON.json"

dados_alunos = {'Pessoa01': {'Nome': 'Matheus', 'Idade': 21, 'Notas': [10, 8, 9]},
                'Pessoa02': {'Nome': 'Lucas', 'Idade': 32, 'Notas': [9, 7, 7]}}

# A seguir, veremos alguns dos métodos provenientes do módulo json:

# dumps(objeto) - Converte um objeto em uma string JSON.
# dump(objeto, arquivo) - Escreve um objeto Python em formato JSON em um arquivo.
# loads(string_json) - Converte uma string JSON para um objeto Python.
# load(arquivo) - Lê um arquivo JSON e converte para um objeto Python.

with open(path, 'w+', encoding='utf-8') as arquivo:
    # Podemos utilizar o argumento indent, para indentarmos nossos dados em JSON. Ao passarmos o valor True,
    # informarmo que queremos indentar nosso JSON sem espaçamentos. Podemos também passar um
    # número inteiro como valor, indicando quantos espaços queremos em nossa indentação.
    # Convertendo um objeto Pyhton em JSON e adicionando em um arquivo JSON:
    json.dump(dados_alunos, arquivo, indent=4)
    arq_texto = 'Esse é um arquivo contendo um texto qualquer'
    arq_texto_JSON = json.dumps(arq_texto)
    print(arq_texto_JSON)
    print('-'*90)
    arquivo.seek(0, 0)
    # Ao convertermos nosso arquivo JSON em um objeto Python, os dados se tornam um dicionário:
    print(json.load(arquivo))
    # Convertendo a string JSON para um objeto Python:
    print(json.loads(arq_texto_JSON))
