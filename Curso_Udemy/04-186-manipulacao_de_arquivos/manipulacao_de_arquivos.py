# O Python nos oferece algumas funções de manipulação de arquivos. Essas funções são:

# open(‘nomeArquivo.txt’, ‘modo de abertura’) - Abre um arquivo no modo especificado por parâmetro.

# read(tamanho) - Lê um arquivo. Podemos passar um parâmetro para indicar a quantidade de caracteres a ser exibido.
# Tal parâmetro pode ser em texto(t) ou bytes(b). Caso um parâmetro não seja passado, irá o arquivo por completo.

# readline( ) - Lê uma linha inteira do arquivo. Cada chamada da função irá ler uma linha em seguida,
# começando a primeira e indo até a última.

# readlines( ) - Lê todas as linhas do arquivo, colocando cada uma como um elemento numa lista.

# write( ) - Escreve dados no arquivo.

# writelines(lista) - Escreve, dentro do arquivo, cada um dos elementos contidos em um iterável (menos dicionários)
# passado por parâmetro.

# close( ) - Fecha o arquivo, liberando os recursos associados a ele.

# seek(offset, whence) - Move o ponteiro de leitura/escrita para uma determinada posição.
# O primeiro parâmetro (offset) indica quantos bytes devem ser pulados antes de realizar a leitura/escrita.
# Já o segundo (whence), indica a posição inicial que o primeiro parâmetro irá começar a atuar.
# O parâmetro whence pode ter os seguintes valores: 0 (padrão): Significa que o deslocamento é relativo ao
# início do arquivo; 1: Significa que o deslocamento é relativo à posição atual do ponteiro de arquivo.
# 2: Significa que o deslocamento é relativo ao final do arquivo.

# tell( ) - Retorna à posição atual do cursor de leitura/escrita no arquivo.

# flush( ) - Garante que os dados contidos no buffer sejam gravados no disco, armazenando-os no arquivo.

# Também temos os modos de abertura para os arquivos. Cada um deles possui um papel e deve ser utilizado
# em situações diferentes:
# r (read) - Responsável pela leitura do arquivo.
# w (write) - Responsável pela escrita no arquivo. Reescreve o conteúdo já existente. Se utilizado quando o
# arquivo não existir, irá criá-lo em seguida.
# a (attach) - Também responsável pela escrita no arquivo, porém mantém o conteúdo já existente nele.
# Também criará o arquivo caso ele não exista.
# Obs.: Ao escrevermos algo em nosso arquivos, o ponteiro de leitura/escrita é posicionado no final do arquivo
# por padrão, sendo necessário utilizar o seek() caso desejarmos lê-lo em sequência.
# t (text) - Indica que o arquivo deve ser tratado como texto.
# b (binary) - Indica que o arquivo deve ser tratado como binário.

caminho = "H:\\GitHub\\Python3\\Curso_Udemy\\04-186-manipulacao_de_arquivos\\banco_de_dados\\dados"

# Exemplo com algumas das funções citadas anteriormente:
# Obs.: IMPORTANTE!!! Sempre utilize o UTF-8 através do argumento encondig, para que o arquivo seja aberto em
# formato UTF-8, aceitado acentuações, etc.
with open(caminho, 'w+', encoding='utf-8') as arquivo:
    arquivo.write('Olá, mundo!\n')
    arquivo.writelines(('Este ', 'e ', 'um ', 'iterável ', 'contendo ', 'strings '))
    arquivo.seek(0, 0)
    print(arquivo.read())
    arquivo.seek(0, 0)
    conteudo_dados = arquivo.readlines()
    print(conteudo_dados)
