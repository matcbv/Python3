from aula_03_23.funcoes.funcoesInterface import *
from time import sleep


def validacao():
    sleep(1)
    opc = input('\033[34m[1] - Adicionar pessoa'
                '\n[2] - Listar pessoa(s)'
                '\n[3] - Apagar banco de dados'
                '\n[4] - Sair do programa\033[0m'
                '\n\nQual das opções acima deseja executar? ')
    linha()
    sleep(1)
    while opc not in '1234':
        print('\033[31mResposta inválida!\033[0m')
        opc = input('Informe uma opção válida \033[33m[1, 2, 3 ou 4]\033[0m: ')
    opc = int(opc)
    return opc


def verifArquivo(nome):
    try:
        with open(nome, 'r') as txt:
            txt.read()
    except FileNotFoundError:
        criarArquivo(nome)
    finally:
        nome.close()


def criarArquivo(arquivo):
    txt = open(arquivo, 'w')
    txt.close()
    print(f'\033[33mArquivo de nome {arquivo} criado.\033[0m\n')


def listarDados(arquivo):
    verifArquivo(arquivo)
    with open(arquivo, 'rt') as txt:
        print(txt.read())


def addDados(arquivo):
    verifArquivo(arquivo)
    lst = [input('\033[33mInforme o nome do cliente: '), ' - ', input('Informe a idade do cliente: \033[0m'), '\n']
    linha()
    with open(arquivo, 'a') as dados:
        dados.writelines(lst)


def delDados(arquivo):
    verifArquivo(arquivo)
    dados = open(arquivo, 'w')
    dados.close()
    sleep(1)
    print('Dados apagados com sucesso.\n')
