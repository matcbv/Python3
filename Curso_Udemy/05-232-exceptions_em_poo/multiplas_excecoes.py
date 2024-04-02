class MyError(Exception):
    pass


class MyOtherError(Exception):
    pass


def levantar():
    excecao = MyError('Erro 01', 'Erro 02', 'Erro 03')
    # Podemos levantar instâncias pertencentes a classes de exceção:
    raise excecao


try:
    # resultado = 1/0
    levantar()
    # Podemos também tratar mais de uma exceção. O except irá retornar a primeira exceção que for
    # detectada. No caso acima, o ZeroDivisionError seria identificado primeiro, mas iremos
    # comentá-lo para demonstrarmos os elementos desse tópico.

    # A palavra-chave as é responsável por armazenar a instância da exceção que foi criada pela função levantar.
    # Neste caso, iremos chamá-la de error. Com tal objeto, podemos ver seu tipo (type(error)) ou convertê-lo
    # para uma string e exibí-lo na tela (str(error)).
except (MyError, ZeroDivisionError) as error:
    # Utilizar .args em uma exceção, irá retornar os argumentos que passamos para aquela exceção ao criarmos
    # sua instância.
    print(f'Ocorreram os erros: {error.args}\nExceção: {error.__class__.__name__}')
    # Utilizando raise dentro de nosso except, estaremos relançando nossa exceção por meio de outra.
    # Nesse exemplo, criamos outra exceção para demonstrar essa ação:
    excecao_02 = MyOtherError('Erro 04', 'Erro 05', 'Erro 06')
    # Com a palavra-chave from, indicamos que a exceção que estamos levantando, é proveniente de outra
    # exceção. Isso será indicado em nosso terminal quando a exceção for levantada.
    raise excecao_02 from error
    # Obs.: Podemos utilizar somente a palvra-chave raise, para relançar a exceção que está sendo tratada no momento.
    # Relançar uma função pode ser útil quando desejamos adicionar mais informações ou contexto a uma
    # determinada exceção.
