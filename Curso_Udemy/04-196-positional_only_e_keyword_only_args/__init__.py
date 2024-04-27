# Ao criarmos nossas funções, podemos especificar os tipos de argumentos que aceitaremos.
# Os dois tipos padrão que temos são os:
# *args - Aceita número ilimitado de argumentos posicionais, formando uma tupla com os valores passados.
# **Kwargs - Aceita número ilimitado de argumentos nomeados, formando uma tupla com os valores passados.

# Caso quisermos que só elementos posicionais sejam aceitos, devemos utilizar o símbolo / em nossa função.
# Todos os elementos anteriores à / deverão ser posicionais.
# Caso desejemos que somente elementos nomeados sejam fornecidos, devemos utilizar o símbolo * na função.
# Todos os elementos após o * devem ser nomeados.
# Ex.:

def funcao_exemplo(a, b, /, c):
    print(a, b, c)


# No exemplo acima, os elementos a e b devem ser posicionais, mas c pode ser nomeado normalmente.

def funcao_exemplo_02(a, b, *, c):
    print(a, b, c)


# No exemplo acima, o elemento c deve ser nomeado.

def funcao_exemplo_03(a, b, /, *, c):
    print(a, b, c)
# Por último, temos as duas filtragens ocorrendo simultaneamente. Os elementos a e b devem ser posicionais, e c
# deve ser nomeado.
