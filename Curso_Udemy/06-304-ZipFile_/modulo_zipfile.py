import os
from pathlib import Path
from zipfile import ZipFile
from itertools import count

root_path = Path(__file__).parent
dir_path = root_path / 'pasta_para_compactar'
zipped_dir_path = root_path / 'pasta_compactada.zip'
unzipped_dir_path = root_path / 'pasta_descompactada'

dir_path.mkdir(exist_ok=True)


# Abaixo, iremos criar nossos arquivos a serem zipados:
def criar_arquivos(qtd: int, path: Path):
    for i in range(qtd):
        texto = f'arquivo_{i}'
        with open(path / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(10, dir_path)

# Através do construtor with, iremos compactar determinado objeto, que no nosso caso,
# será a pasta criada acima.
with ZipFile(zipped_dir_path, 'w') as zip_:
    for root, dirs, files in os.walk(dir_path):
        contador = count()
        for file in files:
            # Para que somente o arquivo seja adicionado ao nosso arquivo compactado,
            # devemos utilizar o parâmetro chamado arcname. Podendo ser utilizado na
            # função write, ele é usado para especificar o nome que você deseja atribuir
            # ao arquivo dentro do arquivo zip. Quando você especifica o arcname, ele
            # adiciona apenas o nome do arquivo dentro do zip, sem incluir o caminho completo.
            zip_.write(Path.joinpath(dir_path, file), arcname=file)

# Para extrairmos nosso arquivo compactado, iremos utilizar o método extractall, passando
# um caminho de destino por parâmetro:
with ZipFile(zipped_dir_path, 'r') as zip_:
    zip_.extractall(unzipped_dir_path)
