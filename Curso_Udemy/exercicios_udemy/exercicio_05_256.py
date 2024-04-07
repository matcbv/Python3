from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito

    @abstractmethod
    def sacar(self, valor_saque): ...


class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor_saque):
        if self.saldo < valor_saque:
            print('Valor para saque insuficiente')
        else:
            self.saldo -= valor_saque


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo):
        super().__init__(agencia, numero_conta, saldo)

    def sacar(self, valor_saque):
        if self.saldo < valor_saque:
            resposta = input('Deseja acionar o cheque especial?')
            if resposta in 'sim':
                self.saldo -= valor_saque
        else:
            self.saldo -= valor_saque


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.obter_nome = nome
        self.obter_idade = idade

    @property
    def obter_nome(self):
        return self._nome

    @obter_nome.setter
    def obter_nome(self, nome):
        self._nome = nome

    @property
    def obter_idade(self):
        return self._idade

    @obter_idade.setter
    def obter_idade(self, idade):
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta


class Banco:
    def __init__(self, agencia, numero_conta):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.conta_cliente = None

    def checar_dados(self, conta_cliente):
        self.conta_cliente = conta_cliente
        if self.conta_cliente.agencia == self.agencia and self.conta_cliente.numero_conta == self.numero_conta:
            print('Saque autorizado')
            valor_saque = int(input('Informa o valor a ser sacado: R$'))
            self.conta_cliente.sacar(valor_saque)
            return print('Após o saque, seu saldo atual é de: R$', conta_cliente.saldo)
        print('Dados cadastrais inválidos!')


Caixa_Economica = Banco(195, 123456789)
conta_caixa = ContaPoupanca(195, 123456789, 1000)
cliente_caixa = Cliente('Matheus', 21, conta_caixa)
Caixa_Economica.checar_dados(conta_caixa)
