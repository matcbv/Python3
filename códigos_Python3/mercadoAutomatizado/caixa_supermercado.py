import subprocess
from funcoes_mercado.verificacoes.caixa import *
compra = {'Produto': [], 'Preço': []}
arq = 'registroCompras.txt'
quantProd = 0

print('---------------SUPERMERCADO COMPRA FÁCIL---------------')
while True:
    if quantProd == 0:
        resposta = temCadastro()
        if resposta == 'N':
            subprocess.run(['python', 'validacaoCadastral.py'])
    quantProd += 1
    listaCompra = addProd(compra, arq)
    valCompra = exibir(listaCompra)
    troco = calcPag(valCompra)
    nf(troco)
