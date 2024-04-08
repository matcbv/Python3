from banco import Banco
import contas
from cliente import Cliente


Caixa_Economica = Banco(195)
conta_caixa = contas.ContaPoupanca(195, 123456789, 1000)
conta_itau = contas.ContaCorrente(205, 2468013579, 1500)
cliente_caixa = Cliente('Matheus', 21, conta_caixa, conta_itau)
Caixa_Economica.adicionar_cliente(cliente_caixa)
Caixa_Economica.solicitar_saque(195, 123456789)
