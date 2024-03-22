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
# Ainda podemos nos referênciar a maior 05-198-classes_metodos_instancias_e_atributos de exceções existente no Python, para generalizarmos a
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
except (TypeError, ValueError):
    print('É necessário que valores para o dividendo e o divisor sejam definidos.')
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
except ZeroDivisionError as error:  # Aqui, definimos o nome da variável que iremos armazenas a instância.
    print('Não é possível realizar uma divisão por 0.')
    print('Erro:', error)
