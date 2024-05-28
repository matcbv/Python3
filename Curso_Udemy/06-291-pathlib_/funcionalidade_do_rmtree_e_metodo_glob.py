import glob
from pathlib import Path

dir_path = Path().absolute() / 'pasta_para_filtragem'
# O método glob é responsável por determinar quais arquivos/diretórios serão selecionados em nossa busca.
# Podemos utilizá-lo de duas formas: com o módulo glob ou com a classe Path do módulo pathlib.

# Elementos importantes na filtragem com o glob:
# / - Significa diretórios.
# * - Padrão de correspondência para todos.
# ** - Padrão de correspondência para recursão.
# ? - Simboliza um caractere único.

# Abaixo veremos exemplos com o método glob:

# Através da classe Path:
# Utilizado o método glob da classe Path, o formato deve ser: 'caminho'.glob('str')
# Aqui iremos buscar todos os arquivos com o formato passado por parâmetro.
# Podemos notar que o arquivo arquivo004.txt não foi adicionado a lista,
# pois não bate com o padrão informado.
print('\nEncontrando asrquivos .txt pela classe Path:')
model_files = dir_path.glob('arquivo_??.txt')
for file in model_files:
    print(file)
print()

# Através do módulo glob:

# O método glob do módulo glob possui duas propriedades. Essas são recursive e include_hidden:

# recursive - Permite uma busca recursiva, trabalhando em conjunto com o padrão **.
# include-hidden - Permite que o método glob identifique arquivos ocultos.

print('\nEncontrando asrquivos .txt pelo módulo glob:')
# Utilizado o método glob do módulo glob, o formato deve ser: glob.glob('str_do_caminho').
# Aqui iremos buscar todos os arquivos do formato txt.
txt_path = str(dir_path / '*.txt')
# Passaremos uma string contendo o caminho, junto do padrão para o método glob.
# No caso abaixo, poderíamos só passar o padrão desejado ('*.txt'), já que, por padrão,
# o método glob realiza a busca no diretório atual.
model_files_txt = glob.glob(txt_path)
for file in model_files_txt:
    print(file)

# Neste último exemplo, estaremos realizando uma busca recursiva:
print('\nEncontrando arquivos .txt de forma recursiva pelo módulo glob:')
another_txt_path = Path().absolute() / 'pasta_para_recursao'
txt_path = str(another_txt_path / '**/*.txt')
another_model_files_txt = glob.glob(txt_path, recursive=True)
for file in another_model_files_txt:
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
