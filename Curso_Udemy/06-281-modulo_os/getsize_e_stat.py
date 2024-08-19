import os

# Através do módulo stat, conseguimos obter informações sobre o status de um determinado
# arquivo, como: tamanho, data da criação,

import os
from itertools import count
contador = count()
path = '/media/matcbv/hd/GitHub/Python3/Curso_Udemy/06-281-modulo_os'

for root, directories, files in os.walk(path):
    print(next(contador), '- Diretório atual:', root)
    if files:
        for file in files:
            file_path = os.path.join(root, file)
            # Para obtermos o tamanho de nossos arquivos em bits, podemos utilizar
            # dois métodos. O método stat, do módulo os, ou o método getsize, do
            # módulo path.
            # Com o método stat:
            os_size_file = os.stat(file_path).st_size
            # Com o método path:
            getsize_size_file = os.path.getsize(file_path)
            print('     ', file, getsize_size_file)
    print()
    print('Subdiretórios:', directories)
    print()
