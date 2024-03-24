class BancoDeDados:
    def __init__(self):
        self.dados = {}

    def add_dados(self, nome, idade):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {nome: idade}
        else:
            self.dados['clientes'].update({nome: idade})
        print('Cliente cadastrado com sucesso!')

    def del_dados(self, nome):
        del self.dados['clientes'][nome]

    def list_dados(self):
        for v in self.dados.values():
            for n, i in v.items():
                print('Nome:', n)
                print('Idade:', i)
                print()


bd = BancoDeDados()

while True:
    bd.add_dados(input('Qual o nome do cliente: '), input('Qual a idade do cliente: '))
    print(bd.dados)

    cont = input('Deseja adicionar mais dados?').lower()
    while cont != 'sim' and cont != 'não':
        print('Resposta inválida!')
        cont = input('Deseja adicionar mais dados?').lower()

    if cont == 'não':
        break

while True:
    erase = input('Deseja apagar algum dado cadastrado?').lower()
    while erase != 'sim' and erase != 'não':
        print('Resposta inválida!')
        erase = input('Deseja apagar algum dado cadastrado?').lower()
    if erase == 'sim':
        bd.del_dados(input('Informe o nome do cliente que deseja apagar: '))
        print(bd.dados)
    else:
        break

show = input('Deseja que os dados cadastrados seja exibidos?').lower()
while cont != 'sim' and cont != 'não':
    print('Resposta inválida!')
    show = input('Deseja que os dados cadastrados seja exibidos?').lower()

if show == 'sim':
    bd.list_dados()
