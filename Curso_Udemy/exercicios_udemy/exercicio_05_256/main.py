from banco import Banco
import contas
from cliente import Cliente
from random import randint


Caixa_Economica = Banco()

while True:
    resp = input('Você já possui uma conta bancária? ').lower()[0]
    if resp == 'n':
        nome = input('Informe seu nome e sobrenome: ')
        idade = int(input('Informe sua idade: '))
        tipo_conta = input('Deseja abrir qual tipo de conta? Poupança ou Corrente?').lower()[0]
        numero_conta = randint(100000000, 999999999)
        if tipo_conta == 'p':
            conta_caixa = contas.ContaPoupanca(195, numero_conta)
        else:
            conta_caixa = contas.ContaCorrente(205, numero_conta)
        cliente_caixa = Cliente(nome, idade, conta_caixa)
        Caixa_Economica.adicionar_cliente(cliente_caixa)
        print(f'Sua conta foi aberta com sucesso! Sua agência e conta são: 195 e {numero_conta}, respectivamente.')

    operacao = input('Deseja realizar alguma operação? ').lower()[0]
    if operacao == 's':
        operacao = int(input('Digite [1] para saques e [2] para depósitos: '))
        agencia = int(input('Informe o número de agência da sua conta: '))
        numero_conta = int(input('Informe o número de sua conta: '))
        if operacao == 1:
            Caixa_Economica.solicitar_saque(agencia, numero_conta)
        else:
            valor_deposito = float(input('Informe o valor a ser depositado: '))
            if Caixa_Economica.checar_conta(agencia, numero_conta):
                conta_cliente = Caixa_Economica.obter_conta(numero_conta)
                contas.Conta.depositar(conta_cliente, valor_deposito)