
def commit(self):
    try:
        dados = metodo
        with open('banco_de_dados', 'a') as arquivo:
            arquivo.write(dados)
    except ValueError:
        print('Tente inicializar uma instância da classe ColetaDeDados.')
    else:
        print('Dados salvos com sucesso!')


class ColetaDeDados:
    def __init__(self, dados):
        self.dados = dados

    @commit
    @property
    def envia_dados(self):
        return self.dados


obj = ColetaDeDados('valor qualquer')
obj.envia_dados()
