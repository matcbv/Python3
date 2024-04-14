from pathlib import Path

# O método glob é responsável por determinar quais arquivos serão selecionados em nossa busca.
# * - Para realizarmos filtragens com vários caracteres.
# ? - Simboliza um caractere único.

# Abaixo veremos um exemplo com o método glob:
with open() as arquivo:
    pass

# Abaixo, criaremos nossa própria função para remoção recursiva:
# Iremos definir dois parâmetro, um para receber a pasta contendo nossa árvore de caminhos,
# e um booleano, que irá informar se devemos ou não deletar nosso diretório.
def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_file():
            file.unlink()
        else:
            rmtree(file, False)
            file.rmdir()
    if remove_root:
        root.rmdir()
