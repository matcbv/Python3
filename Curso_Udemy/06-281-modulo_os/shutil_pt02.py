# shutil.copytree - Realiza a cópia de uma árvore de arquivos recursivamente.
# shutil.rmtree - Apaga uma árvore de arquivos recursivamente.
# shutil.move ou os.rename - Move/Renomeia diretórios e arquivos.
import shutil

path_ = 'C:/Users/mathe/Documents/pasta_qualquer'
path_02 = 'C:/Users/mathe/Documents/pasta_qualquer'


def trabalhando_com_arquivos():
    shutil.rmtree(path_, ignore_errors=True)
    shutil.copytree(path_, NOVA_PASTA)
    # shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')
    shutil.rmtree(NOVA_PASTA, ignore_errors=True)
