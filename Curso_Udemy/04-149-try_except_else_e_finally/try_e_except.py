# Para realizarmos tratamento de erros em Python, devemos utilizar as palavras-chave:
# try, except, else e finally.

# Com try, iremos realizar a tentativa de executar determinados comandos.
# Caso alguma exceção seja retornada, conseguir realizar uma tratativa de erros com a palavra-chave except.
from time import sleep

dividendo = 18
divisor = 0

try:
    print('Cauculando...')
    sleep(1)
    result = dividendo/divisor  # A execução é interrompida aqui, exatamente onde a exceção foi retornada.
    print(f'O resultado é: {result}')
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0.')
print('-'*60)

# Podemos tratar várias exceções com vários excepts ou tratar mais de uma exceção em um único except.
# Ainda podemos nos referênciar a maior classe de exceções existente no Python (Exception), para generalizarmos a
# nossa tratativa de erros. Veja no exemplo abaixo:
dividendo = 18
divisor = None

try:
    print('Cauculando...')
    sleep(1)
    result = dividendo/divisor
    print(f'O resultado é: {result}')
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0.')
    # A palavra-chave as é utilizada para associar o resultado de uma expressão a um nome.
except TypeError as e:  # Aqui, estamos definindo o nome da variável que a instância da exceção será armazenada.
    # Tal instância pode possuir valores como:
    # - args: uma tupla contendo os argumentos passados para a exceção. Em muitos casos, a mensagem de erro está
    # contida neste atributo.
    # - strerror: uma representação de string do erro.
    # - errno: se a exceção estiver relacionada a operações de E/S (entrada/saída), esse atributo pode conter
    # o número de erro associado à falha.
    # - filename: exceções específicas, como FileNotFoundError e FileExistsError, contém o atributo filename,
    # que carrega o nome do arquivo que não pôde ser encontrado.
    print(e.args)
except Exception:
    print('Erro desconhecido! Revise os valores informados e tente novamente.')

# Por último, conseguimos capturar instâncias das classes de erro e exibí-las na tela:
dividendo = 18
divisor = 0

try:
    print('Cauculando...')
    sleep(1)
    result = dividendo/divisor
    print(f'O resultado é: {result}')
except ZeroDivisionError as error:
    print('Não é possível realizar uma divisão por 0.')
    # A instância possui valores
    print('Erro:', error)
