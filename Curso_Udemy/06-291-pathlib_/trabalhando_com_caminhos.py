# Podemos trabalhar com caminhos utilizando a classe Path:
import pathlib
from pathlib import Path

# Ao instanciarmos a classe Path sem passar nenhum valor por parâmetro, será criado um objeto que
# representa o diretório atual (diretório, e não aquivo). Esse objeto é uma instância do nossa classe Path.
# A representação dele se dá por um ponto (.), retornado pelo método __repr__.
caminho_diretorio_atual = Path()
print(caminho_diretorio_atual, type(caminho_diretorio_atual))

# Obtendo o caminho absoluto de forma explícita:
caminho_explicito = caminho_diretorio_atual.absolute()
print(caminho_explicito)
print()

# Para obtermos o caminho absoluto do nosso arquivo atual, devemos instânciar nossa classe Path,
# passando por parâmetro o atributo especial __file__.:
caminho_arquivo_atual = Path(__file__)
print(caminho_arquivo_atual)
print(caminho_arquivo_atual.absolute())
print()

# Obtendo o caminho pai com o método getter parent:
arquivo_pai = caminho_arquivo_atual.parent
print(arquivo_pai)
# Podemos continuar utilizando o parente sucessivamente, caso quisermos:
print(arquivo_pai.parent.parent)
