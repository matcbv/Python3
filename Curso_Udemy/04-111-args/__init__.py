# Podemos também realizar o empacotamento e desempacotamento em funções com argumentos nomeados e não nomeados:
# Utilizando o * em nosso parâmetro da função, iremos empacotar os itens recebidos em tupla.
def recebe_empacotamento(*args):
    # Valores empacotados:
    print(args)
    # Valores desempacotados:
    print(*args, sep=', ')


# Argumentos não nomeados (posicionais):
recebe_empacotamento(1, 2, 3, 4, 5)

# Argumentos nomeados:
print('-'*15)
lista = (1, 2, 3, 4, 5)
# Ao passarmos argumentos nomeados sendo iteráveis, devemos enviá-los desempacotados. Caso contrários,
# teremos uma tupla dentro de outra tupla.
recebe_empacotamento(*lista)
