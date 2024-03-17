from funcoes_mercado.verificacoes.cadastro import *
c = 0

print('=-' * 10)
print(f'VALIDAÇÃO CADASTRAL')
print('=-' * 10)

while True:
    c += 1
    nome = verifNome()
    dataNasc = verifNasc()
    idade = anoAtual - int(dataNasc[2])
    if idade >= 18:
        dados = verifCadastro()
        cpf = dados[0]
        cep = dados[1]
        exibirDados(nome, dataNasc, cpf, cep, c)
    else:
        print(f'Idade insuficiente! Faltam {18 - idade} anos para o cadastrante se tornar maior de idade.\n')
    resp = novoCadastro()
    if resp == 'N':
        print('Programa encerrado.')
        break
