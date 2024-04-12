import os

# Através do módulo stat, conseguimos obter informações sobre o status de um determinado
# arquivo, como: tamanho, data da criação,

import os
from itertools import count
contador = count()
path = 'C:/Users/Suporte/Documents/GitHub/Python3/Curso_Udemy/06-281-modulo_os'

for root, directories, files in os.walk(path):
    print(next(contador), '- Diretório atual:', root)
    if files:
        for file in files:
            file_path = os.path.join(root, file)
            # Para obtermos o tamanho de nossos arquivos em bits, podemoS utilizar
            # dois métodos. O método stat, do módulo os, ou o método getsize, do
            # módulo path.
            # Com o método stat:
            size_file = os.stat(file_path).st_size
            # Com o método path:
            size_file = os.path.getsize(file_path)
            print('     ', file, size_file)
    print('Subdiretórios:', directories)
    print()
