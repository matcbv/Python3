from os import path
# Alguns dos métodos mais utilizados do módulo path são:
# splitext - Gera uma tupla contendo o nome do arquivo e sua respectiva extensão, como primeiro e segundo valor.
# split - Divide um caminho de arquivo em duas partes: o diretório pai e o nome do arquivo.
# join - Unifica diferentes partes de caminhos de diretório em um só caminho.
# exists - Verifica se o caminho existe na máquina.
# isdir - Verifica se o caminho é referente a um diretório.
# isfile - Verifica se o caminho é referente a um arquivo.
# abspath - Retorna o caminho absoluto de um local.
# isabs - Verifica se determinado caminho é absoluto.
# basename - Retorna o nome da base do caminho.
# dirname - Retorna o diretório de um arquivo.
# expanduser - Retorna o caminho para nossa pasta de usuário.

caminho = 'H:/GitHub/Python3/Curso_Udemy/06-281-modulo_os/modulo_path.py'

# No exemplo abaixo, o diretório será o caminho com exceção do arquivo modulo_path.py.
# Já o arquivo, será exatamente o modulo_path.py.
diretorio_pai, arquivo = path.split(caminho)
print(f'Diretório: {diretorio_pai}\n'
      f'Arquivo: {arquivo}')
print()

# Unificado caminhos:
caminho_unificado = path.join(diretorio_pai, arquivo)
print('Caminho unificado:', caminho_unificado)
print()

# Separando o nome da extensão do arquivo obtido acima:
nome_arquivo, extensao_arquivo = path.splitext(arquivo)
print(f'Nome do arquivo: {nome_arquivo}\n'
      f'Extensão do arquivo: {extensao_arquivo}')
print()

# Verificando se um determinado caminho existe em nossa máquina:
print('Existe?', path.exists(caminho))
print()

# Verificando se um caminho é se refere a um diretório (pasta) ou a um arquivo:
print('O destino é um diretório?', path.isdir(caminho))
print('O destino é um arquivo?', path.isfile(caminho))
print()

# Obtendo o caminho absoluto (caminho completo) de um determinado diretório ou arquivo.
# Devemos passar o nome de tal item por parâmetro:
# Obs.: Passando um ponto (.) como parâmetro para o método abspath, ele retorna o caminho absoluto
# do diretório atual.
absoluto = path.abspath('.')
# Passando o atributo especial file, é retornado o caminho absoluto do arquivo atual.
# Obs.: __file__ sempre irá conter o caminho do arquivo atual em que estamos trabalhando.
absoluto_com_atual = path.abspath(__file__)
# Obtendo o base name de um determinado caminho:
base = path.basename(caminho)
print(f'Caminho absoluto: {absoluto}\n'
      f'Caminho absoluto com o arquivo atual: {absoluto_com_atual}\n'
      f'Local base: {base}')
print()

# Obtendo o nome do diretório do arquivo atual:
diretorio = path.dirname(caminho)
print('Nosso diretório é:', diretorio)

# Através do método expanduser, do módulo path, conseguimos obter o caminho para nossa pasta
# de usuário. Passando somente o til, irá obter o usuário sendo utilizado no momento.
# Obs.: Podemos criar um caminho com um nome de usuário diferentes com ~nome_do_usuario.
user = path.expanduser('~')
print(user)
