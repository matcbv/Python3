import shutil
from os import walk
from zipfile import ZipFile
from itertools import count
from pathlib import Path

to_zip_path = Path().absolute() / 'to_zip_files'
empty_dir_path = Path().absolute() / 'empty_dir'

counter = count()

to_zip_path.mkdir(exist_ok=True)
empty_dir_path.mkdir(exist_ok=True)

with open(to_zip_path, 'a') as file:
    while next(counter) < 10:
        file_name = f'file_{next(counter)}'
        mew_file_path = Path.joinpath(to_zip_path, file_name)
        Path.touch(mew_file_path)


with ZipFile(empty_dir_path, 'a') as file:
    for file_, dir_, path_ in walk(to_zip_path):
        ZipFile.write(file, file_, arcname=file_name)
