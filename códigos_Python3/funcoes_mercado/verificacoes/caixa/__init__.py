from funcoes_mercado.interfaceVisual import *


def temCadastro():
    while True:
        resp = input('O cliente possui cadastro com o Supermercado Compra Fácil? [S/N] ').upper()[0]
        pularLinha()
        if resp not in 'SN':
            print('Resposta inválida! Responda com S (Sim) ou N (Não).')
        else:
            return resp


def verifArquivo(arq):
    try:
        with open(arq, 'r') as dados:
            dados.read()
    except FileNotFoundError:
        dados = open(arq, 'w')
        dados.close()
        print('Banco de dados criado com sucesso!')


def addDados(c, a):
    for n, i in c.items():
        with open(a, 'a') as dados:
            dados.writelines(i)
            dados.write(' ')


def addProd(compra, arq):
    while True:
        compra['Produto'].append(input('Informe o nome do item: '))
        compra['Preço'].append(input('Informe o preço do item: R$'))
        linha()
        verifArquivo(arq)
        addDados(compra, arq)
        while True:
            cont = input('Deseja adicionar mais produtos? [S/N] ').upper()[0]
            if cont not in 'SN':
                print('Reposta inválida!')
            else:
                break
        if cont == 'N':
            return compra


def exibir(compra, valTotal=0):
    for e, (n, i) in enumerate(compra.items()):
        if n == 'Preço':
            for c in i:
                valTotal += float(c)
                print(f'{n.title()}:{c}')
        else:
            for c in i:
                print(f'{n.title()}:{c}')
    linha()
    return valTotal


def calcPag(val):
    print(f'O valor total da compra é de: R${val:.2f}')
    pularLinha()
    while True:
        pagamento = float(input('Qual o valor entregue pelo comprador para realizar o pagamento? R$'))
        pularLinha()
        if pagamento < val:
            print('Valor insuficiente! Por favor, informe um valor maior ou igual ao da compra.')
        else:
            break
    troco = pagamento - val
    print(f'O troco a ser entregue para o comprador é de: R${troco:.2f}')
    return troco


def nf(t):
    while True:
        while True:
            cond = input('O cliente deseja receber a nota fiscal da compra? [S/N] ').upper()[0]
            if cond not in 'SN':
                print('Resposta inválida! Responda com S (Sim) ou N (Não).')
            else:
                break
        if cond == 'S':
            linha()
            print('Nome: Matheus Cerqueira')
            print('CPF: 144.203.477-75')
            print(f'Valor da compra: R${t:.2f}')
            linha()
            break
        else:
            break
