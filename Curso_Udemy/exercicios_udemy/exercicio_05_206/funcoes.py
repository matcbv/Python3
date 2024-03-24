import json


def converter_para_JSON(dados):
    try:
        with open("banco_de_dados", 'w') as arquivo:
            json.dump(dados, arquivo, indent=True)
        print('Dados convertidos e salvos com sucesso!')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except Exception:
        print('Ocorreu um erro inesperado!')


def reverter_JSON():
    with open('banco_de_dados', 'r') as arquivo:
        dados = json.load(arquivo)
        return dados
