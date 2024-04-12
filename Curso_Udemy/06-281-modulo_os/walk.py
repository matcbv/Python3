import os
# Importando o método count para utilizarmos um contador na iteração dos arquivos:
from itertools import count
contador = count()
caminho = 'C:/Users/Suporte/Documents/GitHub/Python3/Curso_Udemy/06-281-modulo_os'

# Através da estrutura de repetição for, podemos utilizar o método walk.
# Ele realizará uma busca pelo caminho informado, passando por todos os itens contido nele.
# Casa esses itens também sejm diretórios, ele irá adentrá-los também, e assim sucessivamente.
# Tal função retorna três listas informando o caminho, os subdiretórios e os arquivos presentes no diretório atual,
# respectivamente. Ao utilizá-lo teremos algo do tipo: for path, subdir, files in os.walk(caminho)

for root, directory, file in os.walk(caminho):
    # Abaixo veremos uma contagem do diretório atual, junto de seu caminho:
    print(next(contador), '- Diretório atual:', root)
    # Abaixo veremos os subdiretórios do diretório atual:
    print('Subdiretórios:', directory)
    # Abaixo veremos os arquivos contidos no diretório atual:
    print('Arquivos:', file)
    print()
