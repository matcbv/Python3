from datetime import datetime


class Player:
    def __init__(self, nome, data_nasc, pais):
        self.nome = nome
        self.data = data_nasc
        self.idade = data_nasc[2] - datetime.today().year
        self.pais = pais


def register():
    print('Ok! Vamos realizar seu cadastro. Prometo que vai ser bem rapidinho!')
    print()
    nome = input('Me informe seu nome e sobrenome: ')
    nome_lista = nome.split(' ')
    while len(nome_lista) <= 1:
        print('\nParece que você errou ao digitar seu nome...')
        nome = input('Me informe seu nome e sobrenome: ')
        nome_lista = nome.split(' ')
    data_nasc = verif_data(input('Informe a data de nascimento, separando as datas por / ou espaço: '))
    pais = input('Informe o seu país de origem: ').title()
    jogador = Player(nome, data_nasc, pais)
    date_bank(jogador)


def date_bank(dados):
    pass

def verif_data(data_nasc):
    while len(data_nasc) != 10:
        print('Data de nascimento inválida! Informe uma data válida.\n')
        data_nasc = input('Informe sua data de nascimento: ')
    if '/' in data_nasc:
        data_list = data_nasc.split('/')
    elif ' ' in data_nasc:
        data_list = data_nasc.split(' ')
    for i, c in enumerate(data_list):
        data_list[i] = int(c)
    while True:
        if not 0 < data_list[0] <= 31:
            print('O ano é inválido!')
            data_list[0] = int(input('Informe novamente o ano: '))
        elif not 0 < data_list[1] <= 12:
            print('O mês é inválido!')
            data_list[1] = int(input('Informe novamente o mês: '))
        elif not 1900 <= data_list[2] <= 2024:
            print('O ano é inválido!')
            data_list[2] = int(input('Informe novamente o ano: '))
        else:
            break
    return data_list
