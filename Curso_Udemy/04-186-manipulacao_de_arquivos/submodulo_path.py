# Através do submódulo path, podemos realizar a manipulação de caminhos externos ao nosso projeto.
from os import path
# Estaremos trabalhando com o diretório atual para o aprendizado.
# Obs.: Em Python, o caminho deve ser informado separando os diretórios por barras duplas.
caminho_completo = "H:\\GitHub\\Python3\\Curso_Udemy\\04-186-manipulacao_de_arquivos\\submodulo_path.py"

arq_atual = "submodulo_path.py"
# No módulo os, existem métodos responsáveis para manipular arquivos e diretórios.
# Cada um dos métodos possuem diferentes funções. Alguns deles são:

# splitext( ) - Separa o nome do arquivo de sua extensão, dividindo-os em duas variáveis, a primeira
# com o nome e a segunda com a extensão.
print(path.splitext(arq_atual))
print('-'*90)

# split( ) - Gera uma tupla dividindo um caminho de arquivo em duas partes: o diretório pai e o nome do arquivo.
diretorio_pai, arquivo_filho = path.split(caminho_completo)
print(diretorio_pai, arquivo_filho, sep=' --*--*-- ')
print('-'*90)

# join( ) - Unifica diferentes partes de caminhos de diretório em um só caminho.
print(path.join(diretorio_pai, arquivo_filho))
print('-'*90)

# exists( ) - Verifica se o caminho existe na máquina, retornando um boolean com True ou False.
print(path.exists(caminho_completo))
print('-'*90)

# isdir( ) - Verifica se o caminho é referente a um diretório, retornando um boolean com True ou False.
print(path.isdir(caminho_completo))
print('-'*90)
''
# isfile( ) - Verifica se o caminho é referente a um arquivo.
print(path.isfile(caminho_completo))
