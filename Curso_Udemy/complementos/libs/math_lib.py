import math

number = 10.23

# --------- ceil() ---------

# Arredonda determinado número para cima
print(math.ceil(number))

# --------- floor() ---------

# Arredonda determinado número para baixo
print(math.floor(number))

# --------- trunc() ---------

# Não arredonda o valor, eliminado os dígitos após a vírgula.
print(math.trunc(number))

# --------- pow() ---------

# Calcula determinada potência de um número. Especificamos a potência nos parâmetros.
print(math.pow(number, 2))

# --------- sqrt() ---------

# Calcula a raíz quadrada de um número
print(math.sqrt(number))

# --------- factorial ---------

# Calcula o fatorial de determinado número.
# Obs.: Só é possível calcular o fatorial de um número inteiro.
print(math.factorial(math.floor(number)))
