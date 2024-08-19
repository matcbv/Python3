# --------- del dict[i] ---------

# Deletamos determinado elemento contido no dicionário em questão.
random_dict = {'nome': 'Matheus', 'lastname': 'Cerqueira', 'idade': 22}
del random_dict['idade']

# --------- update() ---------

#  Adiciona ou atualiza informações contidas em um dicionário por meio de iteráveis de conjuntos de palavra-chave.
#  Caso a informação não exista, cria um índice com um valor, caso contrário, atualiza o valor do índice existente.
random_dict.update({'cpf': '12345678910'})
random_dict.update([('altura', '175')])
print(random_dict)
# Obs.: O método update aceita dicionários ou listas de tuplas.

# --------- values() ---------

# Com values, obtemos os valores contidos em nosso dicionário.
dict_values = random_dict.values()
for value in dict_values:
    print(value)
# Obs.: O método values nos retorna um objeto do tipo dict_values, que pode ser iterado.

# --------- keys() ---------

# O método keys nos retorna somente as chaves de nosso dicionário.
dict_keys = random_dict.values()
for key in dict_keys:
    print(key)
# Obs.: Assim como values, é retornado um objeto do tipo dict_keys.

# --------- items() ---------

# O método items retorna um par chave e valor contendo as chaves e os valores do dicionário.
dict_items = random_dict.items()
for key, value in dict_items:
    print(key, value)
# Com items, obtemos um objeto do tipo dict_items.

# --------- pop() ---------

# Elimina e retorna determinada chave do dicionário retornando seu respectivo valor.
cpf = random_dict.pop('cpf')
print(cpf)
print(random_dict)

# Podemos passar um valor padrâo para ser retornado caso a chave em questão não seja encontrada.
# Caso

# --------- popitem() ---------

# Elimina e retorna a última chave do dicionário.

last_value = random_dict.popitem()
print(last_value)
print(random_dict)

# --------- get() ---------

# Obtém o respectivo valor de uma chave em questão.
nome = random_dict.get('nome')
print(nome)

# --------- setdefault() ---------

# Com setdefault, definimos um valor padrão para uma determinada chave.
# Caso a chave existe, o valor contido nela é retornado, caso contrário, a chave é criada e o valor padrão é utilizado.

random_dict.setdefault('peso', 60)
print(random_dict)

# --------- copy() ---------

# Realiza a cópia de um dicionário para outro.
new_random_dict = random_dict.copy()
print(new_random_dict)
