# Uma função decoradora é aquela que decora uma função passada a ela por parâmetro
# em outra função interna a ela (closure).
def funcao_decoradora(funcao):
    def closure():
        print('Execução da closure que irá executar a função decorada.')
        # Aqui estaremos atribuindo a uma variável o resultado da função que foi decorada,
        # e logo em seguida, retornando esse resultado.
        resultado = funcao()
        print('Final da execução da closure e retorno do resultado retornado pela função decorada')
        return resultado
    # Por último, como sempre, estaremos retornando a função interna para formar um closure.
    return closure


def funcao_decorada():
    print(f'Nome da função decorada: {funcao_decorada.__name__}')
    return 'Eu sou a função decorada e estou sendo executada...'


# Iremos passar por parâmetro para a função decoradora, a função a ser decorada, mas sempre nos
# referenciando a própria função sem executá-la (funcao_decorada e não funcao_decorada()).
executa_funcao = funcao_decoradora(funcao_decorada)
result = executa_funcao()
print(result)
