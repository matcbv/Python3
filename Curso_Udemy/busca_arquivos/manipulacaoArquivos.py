# Especificando o caminho do arquivo de texto, conseguimos realizar ações sobre ele:
caminho = "H:\\GitHub\\Python3\\Udemy\\Python3_Udemy-S4\\busca_arquivos\\banco_de_dados\\dados.txt"
# Com o método open(), conseguimos abri o arquivo, passando o caminho acima, junto do modo de
# abertura. Nesse caso, foi utilizado o a(attach):
# Obs.: Caso o arquivo em questão não exista, será criado logo em seguida.
with open(caminho, 'a') as arquivo:
    arquivo.write('Ola, mundo!\n')
# Neste caso, foi utilizado o r(read) para ler e exibir o conteúdo do arquivo na tela.
with open(caminho, 'r') as arquivo:
    print(arquivo.read())
