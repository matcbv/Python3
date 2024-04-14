from pathlib import Path

caminho_diretorio_atual = Path().absolute()
# Através do símbolo de barra (/), conseguimos concatenar strings para formarmos caminhos:
caminho_para_novo_arquivo = caminho_diretorio_atual / 'arquivo_para_exemplo'
print(caminho_para_novo_arquivo)

# Com touch, criamos um arquivo caso esse não exista ou, caso contrário, atualizamos sua timestamp.
# Obs.: timestamp são informações contidas nos diretórios/arquivos como data e hora de sua criação,
# modificação ou último acesso.
# Criando nosso arquivo com o caminho obtido acima:
caminho_para_novo_arquivo.touch()

# Para operações mais simples de escrita e leitura, podemos utilizar os métodos write_text e read_text:
caminho_para_novo_arquivo.write_text('Olá, mundo!', encoding='utf-8')
print(caminho_para_novo_arquivo.read_text(encoding='utf-8'))
# Para mudarmos o modo de abertura e adicionarmos mais de uma informação em nosso arquivo,
# devemos utilizar a declaração with, como já vimos anteriormente. Os métodos acima só podem
# se utilizados antes ou após o with.

# Apagando o arquivo criado acima:
caminho_para_novo_arquivo.unlink()
# Obs.: Caso queira ver o arquivo sendo criado e seu conteúdo, basta comentar essa linda e executar o código.

# Podemos também criar diretórios, assim com vimos anteriormente no módulo os:
caminho_para_novo_diretorio = caminho_diretorio_atual / 'pasta_para_exemplo'
caminho_para_novo_diretorio.mkdir(exist_ok=True)

# Caso esse diretório esteja vazio, também podemos apagá-lo:
caminho_para_novo_diretorio.rmdir()
# Caso nosso diretório não esteja vazio, devemos apagar nossos métodos de forma recursiva.
# Isso pode ser feito através do método rmtree do módulo shutil ou com o método walk, do módulo os.
