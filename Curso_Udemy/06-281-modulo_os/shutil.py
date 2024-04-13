import os
# Através do módulo shutil, conseguimos arquivar e copiar arquivos e diretórios em nosso host.
import shutil

path_ = 'H:/Pasta_Para_Copia'
# Iremos criar nosso novo caminho, contendo a pasta a ser criada:
base_name = os.path.basename(path_)
new_path = path_.replace('Pasta_Para_Copia', 'Pasta_Nova')
# Para criarmos um diretório, utilizaremos o método makedir do módulo os:
os.makedirs(new_path,  exist_ok=True)
# Através parâmetro exist_ok, conseguimos definir se será ou não levantada
# uma exceção caso oo arquivo sendo criado já existe. Passando o valor True,
# iremos garantir que nenhuma exceção seja levantada.

for root, directories, files in os.walk(path_):
    # Para copiarmos nossos arquivos para nosso novo diretório, devemos criar
    # as respectivas pastas contidas em nosso diretório original.
    for dir_ in directories:
        new_dir_path = os.path.join(root.replace(path_, new_path), dir_)
        os.makedirs(new_dir_path, exist_ok=True)
    for file in files:
        file_path = os.path.join(root, file)
        new_file_path = os.path.join(root.replace(path_, new_path), file)
        shutil.copy(file_path, new_file_path)
