# Podemos simplificar o exemplo anterior com o uso de decoradores. Veja a seguir:

def funcao_decoradora(funcao):
    def closure():
        print('Execução da closure que irá executar a função decorada.')
        resultado = funcao()
        print('Final da execução da closure e retorno do resultado retornado pela função decorada')
        return resultado
    return closure


# O uso dos decoradores se dá ao especificarmos qual a função decoradora por antecedência de um @.
@funcao_decoradora
def funcao_decorada():
    # Se notar, o nome da função decorada passa a ter o nome da função interna (closure).
    # Isso ocorre, pois a função decorada não é mais executada diretamente, e sim através da closure.
    print(f'Nome da função decorada: {funcao_decorada.__name__}')
    return 'Eu sou a função decorada e estou sendo executada...'


# Agora podemos executar diretamente a função decorada, tendo o mesmo resultado de antes.
result = funcao_decorada()
print(result)
