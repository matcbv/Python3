from funcoes_mercado.interfaceVisual import *
from datetime import date
anoAtual = date.today().year
mesAtual = date.today().month
diaAtual = date.today().day


def novoCadastro():
    while True:
        sn = input('Deseja realizar um novo cadastro? [S/N] ').upper()[0]
        pularLinha()
        if sn not in 'SN':
            print('Resposta inválida! Responda com S (Sim) ou N (Não).')
            pularLinha()
        else:
            return sn


def exibirDados(n, dn, cpf, cep, c):
    while True:
        mostrar = input('Deseja exibir os dados da pessoa cadastrada [S/N]? ').upper()[0]
        pularLinha()
        if mostrar not in 'SN':
            print('Resposta inválida! Responda com S (Sim) ou N (Não).')
        else:
            if mostrar == 'S':
                print(f'Dados cadastrados da pessoa número {c}:')
                print(f'''
                Nome: {n}
                Data de nascimento: {'/'.join(dn)}
                CPF: {cpf}
                CEP: {cep}
                ''')
            break


def verifNome():
    while True:
        nome = input('\nInforme a seguir, o nome completo da pessoa: ').title().strip().split()
        pularLinha()
        if len(nome) <= 1:
            print('Nome inválido! Por favor, informe seu nome e seu(s) sobrenome(s).')
        else:
            return ' '.join(nome)


def verifNasc():
    while True:
        data = input('Informe a data de nascimento da pessoa separando o dia, mês e ano por espaços: ').strip().split()
        pularLinha()
        if len(data) != 3:
            print('Data de nascimento inválida! Informe valores válidos, separando-os por espaço.\n')
        else:
            dia = int(data[0])
            mes = int(data[1])
            ano = int(data[2])
            if 1900 < ano <= anoAtual and 0 < mes <= 12 and 0 < dia <= 31:
                return data
            else:
                print('Data de nascimento inválida! Informe valores válidos, separando-os por espaço.\n')


def verifCadastro():
    while True:
        cpf = input('Informe o seu CPF, sem separá-lo por caracteres especiais: ')
        pularLinha()
        if cpf.isdecimal() and len(cpf) == 11:
            break
        else:
            print('CPF inválido!')
    while True:
        cep = input('Informe seu CEP sem separá-lo com caracteres especiais: ')
        pularLinha()
        if cep.isdecimal() and len(cep) == 8:
            break
        else:
            print('CEP inválido!')
    print('Cadastro concluído!')
    return cpf, cep
