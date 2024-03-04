# -------# Empacotamento #-------
# O empacotamento é o processo de preencher iteráveis com diversos dados em uma única atribuição. Ex.:
dicionario = {'Nome': 'Matheus', 'sobrenome': 'Cerqueira', 'Idade': 21}

# -------# Desempacotamento (*args e **Kwargs [keyword arguments ou argumentos nomeados]) #-------
# O desempacotamento é o nome dado ao processo de retirar os dados contidos em iteráveis.
# Lembrando que os kwargs só funcionam em dicionários com argumentos já nomeados. Para lidarmos com
# listas ou tuplas, devemos utilizar os *args, por se tratarem de elementos não nomeados. Ex.:
print('-'*30)
nome, sobrenome, idade = dicionario.items()
print(nome, sobrenome, idade)

# Ex. 2:
print('-'*30)
nome, sobrenome, idade = dicionario.values()
print(nome, sobrenome, idade)

# Ex. 3:
print('-'*30)
(chave_nome, nome), (chave_sobrenome, sobrenome), (chave_idade, idade) = dicionario.items()
print(chave_nome, nome)
print(chave_sobrenome, sobrenome)
print(chave_idade, idade)
print('-'*30)

# Ex. 4:
# Criaremos um dicionário com mais alguns dados que queremos adicionar em nosso dicionário.
# Para isso utilizaremos os kwargs, que funcionam para argumentos já nomeados.
mais_dados = {'Peso': 55, 'Altura': 1.74}
dicionario.update({**mais_dados})
print(dicionario)

# Obs.: Também podemos estar adicionando outros dois dicionários em um novo:
print('-'*30)
dicionario_completo = {**dicionario, **mais_dados}
print(dicionario_completo)
print('Como podemos ver, obtivemos o mesmo resultado, porém em um novo dicionário.')


# Funções com Kwargs:
def mostrar_dados(*args, **kwargs):
    print('Dados não nomeados recebidos:', args)
    print('Dados nomeados recebidos:', kwargs)


mostrar_dados(1, 2, 'texto', **dicionario_completo)
