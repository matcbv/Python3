import os

caminho = 'H:/GitHub/Python3/Curso_Udemy/06-281-modulo_os'
# O método listdir irá retornar uma lista contendo todos os arquivo contidos no arquivo base
# do caminho informado. Neste exemplo, utilizaremos a pasta do exercício 06-281.
print(os.listdir(caminho))

# Abaixo, iremos iterar tal lista:
for pasta in os.listdir(caminho):
    # Iremos utilizar o método join para
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo_pasta):
        # Com a palavra-chave continue, iremos dar continuidade em nossa iteração, pulando para
        # o próximo objeto do iterável.
        continue
    for arquivo in os.listdir(caminho_completo_pasta):  # Também poderíamos iterar com: os.listdir(pasta).
        print('     ', arquivo)
