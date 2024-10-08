# Também podemos criar um context manager através da função contextmanager, da classe contextlib:
from contextlib import contextmanager


# Usaremos o contextmanager como decorador em nossa função:
@contextmanager
def my_context_manager(path, open_mode):
    # Caso nosso context manager levante alguma exceção, com o uso do decorador, não temos
    # acesso a ela, e não seria possível fechar nosso arquivo, já que seu fechamento se
    # encontra após o yield. Para realizarmos o tratamento de exceções, utilizaremos o bloco
    # try e finally, como já vimos anteriormente.
    try:
        print('Abrindo arquivo...')
        arq = open(path, open_mode, encoding='utf-8')
        # Através do decorador contextmanager, nossa função passa a ser tratada como um gerador.
        # Ele realiza a tratativa de nossa função utilizando os métodos especiais
        # __enter__ e __exit__ internamente, facilitando o uso do context manager.
        # O yield, em context generators, é responsável por marcar um ponto de interrupção
        # entre o início e o fim do bloco with. Ele também pode retornar um objeto nessa situação.
        # Nosso código após o yield, será tratado depois da execução do bloco with.
        yield arq
    # Tratar ou não a exceção nesse caso é opcional.
    except Exception as e:
        print('Ocorreu um erro inesperado! Tente novamente. Erro:', e)
    finally:
        print('Dando continuidade ao context manager')
        print('Fechando arquivo.')
        arq.close()


with my_context_manager('text_model.txt', 'w') as arquivo:
    arquivo.write('Texto qualquer')
    print('FIM')
