class MyException(Exception):
    ...


class MyContextManager:
    def __init__(self, path, open_mode):
        self.path = path
        self.open_mode = open_mode
        self._file = None

    def __enter__(self):
        self._file = open(self.path, self.open_mode, encoding='utf-8')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        # Quando uma exceção é gerada em nosso context manager, temos acesso a alguns atributos dessa
        # exceção em nosso método especial __exit__:
        # O tipo (classe) da nossa exceção
        print('Classe do exceção:', exc_type)
        # A instância da nossa exceção:
        print('Instância do exceção:', exc_val)
        # O traceback da nossa exceção:
        print('Traceback da exceção:', exc_tb)
        # Quando retornamos o boolean True em nosso context manager, as exceções são "ignoradas", não
        # interrompendo nosso código. Isso pode ser utilizado em caso de ciência do problema que está
        # ocorrendo. Lembrando que erros não devem ser silenciosos e sim explícitos em nosso código.
        # return True ---- COMENTADO PARA VERMOS O FUNCIONAMENTO DA EXCEÇÃO ----
        # Ao invés de retornarmos True, podemos levantar uma exceção para exibí-la da maneira que preferirmos
        raise MyException('Minha mensagem de erro')


instancia = MyContextManager('banco_de_dados.txt', 'w+')

with instancia as arquivo:
    print('Instância de TextIoWrapper:', arquivo)
    # Por mais que logo abaixo tenhamos um problema em nosso código, o erro não seria gerado
    # caso o return True não estivesse comentado.
    arquivo.write('Estamos adicionado um texto ao nosso arquivo.', 'Outro valor qualquer')
