# O método argv faz parte do módulo sys em Python e é uma lista que contém os argumentos
# passados para o script Python quando ele é executado a partir da linha de comando.
from sys import argv

argumentos = argv
quantidade_argumentos = len(argumentos)
# O primeiro argumento é sempre o nome do próprio script.
# Isso ocorre porque quando você executa um script Python a partir da linha de comando,
# você especifica o nome do script como o primeiro argumento para o interpretador Python.
print('Argumentos:', argumentos,
      'Quantidade de argumentos:', quantidade_argumentos)


# Exemplo de uma verificação através do método argv:
if quantidade_argumentos < 1 or quantidade_argumentos > 2:
    print('Quantidade de argumentos inválida!')
else:
    print(f'Você passou os argumentos {argumentos[1:]}')
    print(f'O argumento {argumentos[1]} tem a função X')
    print(f'O argumento {argumentos[2]} tem a função Y')
