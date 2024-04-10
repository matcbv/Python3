from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo=0):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor_saque): ...

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        self.movimentacoes(f'(DEPÓSITO R${valor_deposito:.2f})')

    def movimentacoes(self, operacao=''):
        print(f'O seu saldo atual é de R${self.saldo:.2f} {operacao}')


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo=1000):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor_saque):
        if self.saldo < valor_saque:
            print('Saque negado! Saldo insuficiente.')
            return self.movimentacoes()
        self.saldo -= valor_saque
        self.movimentacoes(f'(SAQUE R${valor_saque:.2f})')


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo=1500):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor_saque):
        if self.saldo < valor_saque:
            print('Saque negado! Saldo insuficiente.')
            self.movimentacoes()
            resposta = input('Deseja acionar o cheque especial? ')
            if resposta in 'sim':
                self.saldo -= valor_saque
                return self.movimentacoes(f'(SAQUE R${valor_saque:.2f})')
        self.saldo -= valor_saque
        self.movimentacoes(f'(SAQUE R${valor_saque:.2f})')
