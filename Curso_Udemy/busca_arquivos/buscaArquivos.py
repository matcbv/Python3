import os

caminho = "H:\\GitHub\\Python3\\Udemy\\banco_de_dados"
arqProc = 'texto.txt'

for diretorio_atual, subdiretorios, arquivos in os.walk(caminho):
    for arquivo in arquivos:
        caminho_completo = os.path.join(diretorio_atual, arquivo)
        arqAtual, ext = os.path.splitext(arquivo)
        if arqAtual == arqProc:
            print('O diretório atual é:', diretorio_atual)
            print('O nome do arquivo é:', arqAtual)
            print('Extensão do arquivo:', ext)
            print('Tamanho em bytes:', os.path.getsize(caminho_completo))
