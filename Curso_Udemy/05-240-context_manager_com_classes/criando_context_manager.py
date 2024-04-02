# Um exemplo de context manager no Python é o with open():
# Ex.:
# with open('texto', 'w') as arquivo:

# Iremos reproduzí-lo utilizando o context manager:
class MyContextManager:
    def __init__(self, path, open_mode):
        self.path = path
        self.open_mode = open_mode
        self._file = None

    def __enter__(self):
        print('Abrindo arquivo')
        # O que retornarmos do __enter__ será atribuído ao objeto criado com with (neste caso arquivo).
        # Iremos retornar nosso aquivo através da função open():
        self._file = open(self.path, self.open_mode, encoding='utf-8')
        return self._file

    # O método __exit__ receberá a classe de exceção, a exceção e o traceback. Se ele retornar True,
    # a exceção no with será suprimida.
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo')
        self._file.close()


instancia = MyContextManager('banco_de_dados', 'w+')
with instancia as arquivo:
    print(arquivo)
    arquivo.write('Estamos adicionado um texto ao nosso arquivo.')
    arquivo.seek(0, 0)
    print(arquivo.read())
