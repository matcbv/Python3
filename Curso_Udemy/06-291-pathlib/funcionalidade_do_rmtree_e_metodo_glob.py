import glob
from pathlib import Path

dir_path = Path().absolute()
dir_path = dir_path / 'pasta_para_filtragem'
# O método glob é responsável por determinar quais arquivos/diretórios serão selecionados em nossa busca.
# Podemos utilizá-lo de duas formas: com o módulo glob ou com a class Path do módulo pathlib.
# No módulo glob, temos três funções que podemos utilizar:

# glob.glob - Retorna uma lista com todos os arquivos/diretórios encontrados pelo padrão informado.
# Caso nenhum arquivo seja encontrado, uma lista vazia é retornado.

# glob.glob0 - Tem a mesma função de glob.glob, porém caso nada seja encontrado, a exceção glob.GlobError
# é levantada.

# glob.glob1 - Busca por arquivos e diretório contidos no diretório passado a ele,
# sem entrar em subdiretórios.

# Elementos importantes na filtragem com o glob:
# / - Significa diretórios.
# * - Significa todos.
# ? - Simboliza um caractere único.

# Abaixo veremos exemplos com o método glob:

# Através da classe Path:
# Utilizado o método glob da classe Path, o formato deve ser: 'caminho'.glob('str')
# Aqui iremos buscar todos os arquivos com o formato passado por parâmetro.
# Podemos notar que o arquivo arquivo004.txt não foi adicionado a lista,
# pois não bate com o padrão informado.
model_files = dir_path.glob('arquivo??.txt')
for file in model_files:
    print(file)

# Através do módulo glob:
# Utilizado o método glob do módulo glob, o formato deve ser: globX.glob('str_do_caminho'), sendo X, 0 ou 1.
# Aqui iremos buscar todos os arquivos do formato txt.
txt_path = str(dir_path / '*.txt')
# Passaremos uma string contento o caminho, junto do padrão para o método glob.
# No caso abaixo, poderíamos só passar o padrão desejado ('*.txt'), já que, por padrão,
# o método glob realiza a busca no diretório atual.
model_files_txt = glob.glob(txt_path)
for file in model_files_txt:
    print(file)


# Abaixo, criaremos nossa própria função para remoção recursiva:
# Iremos definir dois parâmetro, um para receber a pasta contendo nossa árvore de caminhos,
# e um booleano, que irá informar se devemos ou não deletar nosso diretório.
def rmtree(root: Path, remove_root=True):
    for file_ in root.glob('*'):
        if file_.is_file():
            file_.unlink()
        else:
            rmtree(file_, False)
            file_.rmdir()
    if remove_root:
        root.rmdir()
