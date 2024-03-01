import json

caminho = r'H:\OneDrive\Estudos\Programação\Python\Módulo_04\Banco de Dados_Exercicios\Arquivo JSON.txt'
arq = 'bancoDeDadosJSON'

dicionario = {'Pessoa 1': 'Matheus',
              'Idade 1': '21',
              'Pessoa 2': 'Lucas',
              'Idade 2': '32'}

with open(caminho, 'w') as arquivo:
    json.dump(dicionario, arquivo, indent=True)


with open(caminho, 'r') as arquivo:
    arquivo_py = json.load(arquivo)

with open(arq, 'w') as banco_py:
    for i, e in dicionario.items():
        banco_py.write(i)
        banco_py.write(' ')
        banco_py.write(e)
        banco_py.write('\n')
