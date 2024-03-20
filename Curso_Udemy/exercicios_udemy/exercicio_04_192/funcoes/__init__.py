import os

path = "H:\\GitHub\\Python3\\Curso_Udemy\\exercicios_udemy\\exercicio_04_192\\banco_de_dados"
historico_respostas = []


def chama_funcao(resp):
    match resp:
        case 'listar':
            listar_dados()
        case 'refazer':
            refazer_dados()
        case 'desfazer':
            desfazer_dados()
        case 'excluir':
            excluir_dados()
        case 'limpar':
            limpar_tela()


def adicionar_dados(dados):
    historico_respostas.append(dados)
    with open(path, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{dados}\n')
        print(dados, 'foi adicionado ao banco de dados.')


def refazer_dados():
    if not historico_respostas:
        print('Não a nada a ser refeito.')
    else:
        dado = historico_respostas.pop()
        with open(path, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{dado}\n')


def desfazer_dados():
    if not historico_respostas:
        print('Não a nada a ser desfeito.')
    else:
        with open(path, 'r', encoding='utf-8') as arquivo:
            lista_dados = arquivo.readlines()
            ultimo_dado = lista_dados.pop()
            historico_respostas.append(ultimo_dado)

        with open(path, 'w', encoding='utf-8') as arquivo:
            arquivo.writelines(lista_dados)


def listar_dados():
    if not historico_respostas:
        print('O banco de dados está vazio.')
    else:
        with open(path, 'r', encoding='utf-8') as arquivo:
            print()
            print(arquivo.read())


def excluir_dados():
    dado = input('informe o dado a ser excluído: ')
    dado += '\n'
    with open(path, 'r', encoding='utf-8') as arquivo:
        lista_dados = arquivo.readlines()
        if not lista_dados:
            print('O bando de dados está vazio.')
        else:
            try:
                lista_dados.remove(dado)
            except ValueError:
                print('Dado não encontrado no banco de dados.')

    with open(path, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(lista_dados)


def limpar_tela():
    os.system('cls')
