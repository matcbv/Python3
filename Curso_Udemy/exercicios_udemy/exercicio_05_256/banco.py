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

    def checar_agencia(self, agencia):
        if agencia in self.agencias:
            return True
        return False

    def checar_numero_conta(self, numero_conta):
        print(self.contas)
        for conta in self.contas:
            print(conta)
            if conta.numero_conta == numero_conta:
                self._tipo_conta = conta.__class__.__name__
                return True
        return False

    def solicitar_saque(self, agencia, numero_conta):
        if self.checar_agencia(agencia) and self.checar_numero_conta(numero_conta):
            valor_saque = float(input('Qual o valor que deseja sacar? R$'))
            conta_cliente = self.obter_conta(numero_conta)
            if self._tipo_conta is contas.ContaCorrente:
                contas.ContaCorrente.sacar(conta_cliente, valor_saque)
            else:
                contas.ContaPoupanca.sacar(conta_cliente, valor_saque)

    def obter_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta

    def __repr__(self):
        return f'{self.contas}'
