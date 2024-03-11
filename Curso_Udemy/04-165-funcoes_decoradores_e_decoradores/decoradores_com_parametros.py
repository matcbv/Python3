# Caso desejemos passar valores para serem utilizados em nossos decoradores, podemos realizar tal ação
# com o auxílio de uma função externa a nossa função decoradora. Veja a seguir:

# O valor pode ser utilizado em qualquer escopo interno da funcao_recebe_parametro
def funcao_recebe_parametro(valor):
    def funcao_decoradora(funcao):
        def closure():
            print('Execução da closure que irá executar a função decorada.')
            resultado = funcao()
            print('Final da execução da closure e retorno do resultado retornado pela função decorada')
            return resultado
        return closure
    return funcao_decoradora


# Ao utilizar uma função externa como decorador, podemos estar passando parâmetros
# que podem ser utilizados pelas demais funções interna a qualquer momento.
# Tal decorador irá retornar nossa função decoradora (funcao_decoradora) logo em seguida.
# Obs.: É possível termos mais de um decorador para uma mesma função.
# A ordem de execução dos decoradores será sempre do mais próximo da função para cima.
# funcao_recebe_parametro('mais um valor') - Esse decorador seria o segundo a ser executado.
@funcao_recebe_parametro('valor qualquer')
def funcao_decorada():
    print(f'Nome da função decorada: {funcao_decorada.__name__}')
    return 'Eu sou a função decorada e estou sendo executada...'


# Para que nossa funcão interna (closure) seja retornada,
# devemos nos referenciar a própria função funcao_recebe_parametro, passando por parâmetro
# determinado valor, e por fim, a função que queremos que seja decorada. Essa será utilizada
# pela função decoradora que será retornada.
executa = funcao_recebe_parametro('outro valor')(funcao_decorada)
# Por último, iremos chamar nosso closure, que irá nos exibir o resultado.
print(executa())
