# --------- replace(x, y) ---------

# Com o método replace, substituímos todas as aparições de determinado valor por outro especificado.
random_phrase = 'Essa é uma frase aleatória criada como exemplo'
replaced_phrase = random_phrase.replace(' ', '-')
print(replaced_phrase)

# --------- upper(i) ---------

# Com o método upper, transformamos determinado objeto para letras maiúsculas
uppercase_phrase = random_phrase.upper()
print(uppercase_phrase)
# Obs.: Também conseguimos passar um índice por parâmetro para que somente ele fique em maiúsculo.

# --------- lower(i) ---------

# Ao contrário de upper, lower converte determinado objeto para letras minúsculas.
lowercase_phrase = random_phrase.lower()
print(lowercase_phrase)

# --------- capitalize() ---------

# Transforma todas as letras de um objeto em minúsculas com exceção do primeiro índice.
capitalized_phrase = random_phrase.capitalize()
print(capitalized_phrase)

# --------- title() ---------

# Transforma toda o objeto para letras minúsculas, com exceção da primeira letra após cada espaço.
titled_phrase = random_phrase.title()

# --------- strip() ---------

spacing_phrase = '   Essa frase possui   espaços sobressalentes   '

# Elimina todos os espaços desnecessários contidos na string, isso é, os espaços sobressalentes do início e do final.
striped_phrase = random_phrase.strip()

# --------- rstrip() e lstrip() ---------

# Elimina todos os espaços sobressalentes contidos no início do objeto:
left_striped_phrase = random_phrase.lstrip()
print(left_striped_phrase)

# Elimina todos os espaços sobressalentes contidos no final do objeto:
right_striped_phrase = random_phrase.rstrip()
print(right_striped_phrase)

# --------- insert(position, value) ---------

# Insere determinado valor no índice especificado
number_list = [1, 2, 3, 5]
number_list.insert(3, 4)
print(number_list)
# Obs.: Funciona somente em listas.
