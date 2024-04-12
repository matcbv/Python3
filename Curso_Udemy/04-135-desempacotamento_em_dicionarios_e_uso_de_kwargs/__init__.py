# Desempacotamento em dicionário e utilização de kwargs (keyword arguments)
# Podemos realizar o desempacotamento em dicionários de diversas maneiras, utilizando os métodos
# items e values dos dicionários.
# Os kwargs trabalham com argumentos nomeados, sendo representados por dois asteriscos unidos (**)

dicionario = {'Nome': 'Matheus', 'Sobrenome': 'Cerqueira', 'Idade': 21}

# Quando usamos os métodos embutidos values() e keys(), estaremos criando listas
# do tipo dict_values e dict_keys, respectivamente. Já com o método items(), criamos
# uma tupla contendo as duplas: chave e valor.

# Ex.:
print('-'*30)
nome, sobrenome, idade = dicionario.items()
print(nome, sobrenome, idade)

# Ex. 2:
print('-'*30)
nome, sobrenome, idade = dicionario.values()
print(nome, sobrenome, idade)

# Ex. 3:
print('-'*30)
# Aqui, estaremos criando tuplas com os valores presentes no dicionário, após desempacotá-lo
# através do método items.
(chave_nome, nome), (chave_sobrenome, sobrenome), (chave_idade, idade) = dicionario.items()
print(chave_nome, nome)
print(chave_sobrenome, sobrenome)
print(chave_idade, idade)
print('-'*30)

# Ex. 4:
# Criaremos um dicionário com mais alguns dados.txt que queremos adicionar em nosso dicionário.
# Para isso, utilizaremos os kwargs, junto do método update, passando os dados.txt desempacotados do
# dicionário mais_dados.
print(4)
mais_dados = {'Peso': 55, 'Altura': 1.74}
dicionario.update(**mais_dados)
print(dicionario)

# Obs.: Também podemos estar adicionando outros dois dicionários em um novo:
print('-'*30)
dicionario_completo = {**dicionario, **mais_dados}
print(dicionario_completo)
print('Como podemos ver, obtivemos o mesmo resultado, porém em um novo dicionário.')
print('-'*30)


# Funções com Kwargs:
# Na função abaixo, iremos receber e empacotar os dados.txt de args e kwargs.
def mostrar_dados(*args, **kwargs):
    # Os args serão empacotados em um tuplas, já os kwargs em um dicionário.
    print('Dados não nomeados recebidos:', args)
    print('Dados nomeados recebidos:', kwargs)


# Como vimos anteriormente nos args, ao lidarmos com argumentos nomeados, devemos enviar os dados.txt
# desempacotados.
mostrar_dados(1, 2, 'texto', **dicionario_completo)
