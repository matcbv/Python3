from os import walk
from zipfile import ZipFile
from pathlib import Path

to_zip_path = Path().absolute() / 'to_zip_files'
empty_dir_path = Path().absolute() / 'empty_dir'
to_zip_path.mkdir(exist_ok=True)
empty_dir_path.mkdir(exist_ok=True)


def criar_arquivos(qtd: int, path: Path):
    for i in range(qtd):
        texto = f'arquivo_{i}'
        with open(path / f'{texto}.txt', 'w') as arquivo:
            arquivo.write(texto)


criar_arquivos(10, to_zip_path)

with ZipFile(empty_dir_path, 'w') as file:
    for file_, dir_, path_ in walk(to_zip_path):
        file.write(Path.joinpath(to_zip_path, file_), arcname=file_)
