class MyException(Exception):
    pass


def levantar_excecao(msg):
    excecao = MyException(msg)
    # Podemos criar nota para nossas exceções através da função add_note:
    excecao.add_note('Podemos criar notas para nossa exceção!')
    raise excecao

try:
    numero_01 = 'texto'
    numero_02 = 3
    result = numero_01 + numero_02
except TypeError as error:
    print('-' * 80)
    print('O valor não é numérico. Erro:', error)
    try:
        # Aqui criamos uma instância da classe MyException, passando uma mensagem como argumento.
        # Também iremos indicar que a exceção é proveniente de error (TypeError).
        raise levantar_excecao('Verifique os elementos que está tentando concatenar.') from error
    # Iremos acessar nossa instância através do objeto complement.
    except MyException as complement:
        print(complement)
        print('-'*80)
        # Aqui, iremos relançar a exceção que está sendo tratada no momento.
        raise
