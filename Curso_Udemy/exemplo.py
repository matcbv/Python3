from abc import ABC, abstractmethod


class PostoGasolina(ABC):
    def __init__(self):
        self.litros_disponiveis = 1000
        self.faturamento = 0

    @abstractmethod
    def reabastecer_bomba(self): ...


class Bomba(PostoGasolina):
    def __init__(self, carro):
        super().__init__()
        self.reabastecer = False
        self.capacidade_bomba = 100
        self.carro = carro

    def abastecer_carro(self, litros_comprados):
        self.litros_disponiveis -= litros_comprados
        if self.litros_disponiveis < 0:
            print('Combustível insuficiente. Por favor, reabasteça a bomba.')
            self.reabastecer = True
        print(f'O carro {self.carro} foi abastecido com sucesso.')
        if self.reabastecer:
            self.reabastecer_bomba()

    def reabastecer_bomba(self):
        if self.litros_disponiveis > 100:
            self.capacidade_bomba += 100
            self.litros_disponiveis -= 100
            return
        self.capacidade_bomba = self.litros_disponiveis
        self.litros_disponiveis = 0
        return

    def realizar_pagamento(self, valor, pagamento):
        troco = pagamento - valor
        if troco < 0:
            print('Valor insuficiente!')
            resposta = input('Deseja realizar nova tentativa de pagamento? [sim/não]').lower()
            if resposta == 'sim':
                pagamento = float(input('Pagamento: R$'))
                return self.realizar_pagamento(valor, pagamento)
            return 'Pagamento não realizado'
        self.faturamento = pagamento - troco
        return troco


while True:
    carro_cliente = Bomba(input('Modelo do carro a ser abastecido: '))
    carro_cliente.abastecer_carro(int(input('Quantos litros deseja abastecer?')))
    troco_carro_01 = carro_cliente.realizar_pagamento(float(input('Qual o valor do abastecimento? R$')),
                                                      float(input('Pagamento: R$')))
    print(f'O troco a ser entregue é de: R${troco_carro_01:.2f}')
