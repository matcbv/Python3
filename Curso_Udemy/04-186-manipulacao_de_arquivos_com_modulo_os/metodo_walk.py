import os

caminho = "H:\\GitHub\\Python3\\Curso_Udemy\\04-186-manipulacao_de_arquivos_com_modulo_os"
arqProc = 'dados.txt'

# Através do iterador for, utilizaremos o método walk. O método walk retorna três elementos, na respectiva ordem:
# O diretório atual; os subdiretórios contidos no diretório atual; os arquivos contidos no diretório atual.
for diretorio_atual, subdiretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        arqAtual, ext = os.path.splitext(arquivo)
        if arqAtual == arqProc:
            print('O diretório atual é:', diretorio_atual)
            print('O nome do arquivo é:', arqAtual)
            print('Extensão do arquivo:', ext)
            caminho_completo = os.path.join(diretorio_atual, arquivo)
            print('Tamanho em bytes:', os.path.getsize(caminho_completo))
