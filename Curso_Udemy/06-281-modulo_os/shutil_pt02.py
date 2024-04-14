import os
import shutil

path_01 = 'H:/GitHub/Python3/Curso_Udemy/06-281-modulo_os/pasta_para_exemplo'
path_02 = 'H:/GitHub/Python3/Curso_Udemy/06-281-modulo_os/pasta_para_exemplo_02'
path_03 = 'H:/GitHub/Python3/Curso_Udemy/06-281-modulo_os/pasta_para_exemplo_03'
path_04 = 'H:/GitHub/Python3/Curso_Udemy/06-281-modulo_os/pasta_para_exemplo_04'
path_para_excluir = 'H:/GitHub/Python3/Curso_Udemy/06-281-modulo_os/pasta_para_ser_excluida'

os.makedirs(path_03, exist_ok=True)


def trabalhando_com_arquivos():
    # Excluindo o diretório path_para_excluir:
    shutil.rmtree(path_para_excluir, ignore_errors=True)
    # Copiando o diretório path_02 para o path_03:
    shutil.copytree(path_02, path_03, dirs_exist_ok=True)
    # Renomeando o diretório path_02:
    shutil.move(path_02, path_02 + '_nova')
    # Voltando path_02 ao nome original:
    shutil.move(path_02 + '_nova', path_02.replace('_nova', ''))
    # Copiando um único arquivo de path_03 para path_04:
    shutil.copy(path_03 + '/arquivo01.txt', path_04)
    # Copiando apenas o conteúdo de um arquivo para outro:
    shutil.copyfile(path_01 + '/arquivo_qualquer.txt', path_04 + '/arquivo01.txt')


trabalhando_com_arquivos()
