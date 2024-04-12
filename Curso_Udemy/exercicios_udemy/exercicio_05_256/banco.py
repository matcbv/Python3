import contas


class Banco:
    def __init__(self, cliente_banco=None):
        self.agencias = [195, 200, 205]
        self.cliente = cliente_banco
        self.contas = []
        self._tipo_conta = None

    def adicionar_cliente(self, conta_cliente):
        self.cliente = conta_cliente
        for conta in conta_cliente.contas:
            self.contas.append(conta)

    def checar_conta(self, agencia, numero_conta):
        if agencia in self.agencias:
            for conta in self.contas:
                if conta.numero_conta == numero_conta:
                    return True
            return False
        return False

    def obter_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                self._tipo_conta = conta.__class__.__name__
                return conta

    def solicitar_saque(self, agencia, numero_conta):
        if self.checar_conta(agencia, numero_conta):
            valor_saque = float(input('Qual o valor que deseja sacar? R$'))
            conta_cliente = self.obter_conta(numero_conta)
            if self._tipo_conta is contas.ContaCorrente:
                contas.ContaCorrente.sacar(conta_cliente, valor_saque)
            else:
                contas.ContaPoupanca.sacar(conta_cliente, valor_saque)
        else:
            print('Verifique os dados.txt de sua conta e tente novamente.')
