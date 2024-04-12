import os

caminho = 'H:/GitHub/Python3/Curso_Udemy/06-281-modulo_os/pasta_para_exemplo/arquivo_exemplo.txt'
directory, file = os.path.split(caminho)

arq, ext = os.path.splitext(file)
print(ext)
