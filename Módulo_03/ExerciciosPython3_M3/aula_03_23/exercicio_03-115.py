from funcoes.funcoesArmazenamento import *
from funcoes.funcoesInterface import *
arq = 'dadosPessoas.txt'
titulo('\033[32mSISTEMA DE CADASTRO\033[0m')
while True:
    escolha = validacao()
    if escolha == 1:
        addDados(arq)
    elif escolha == 2:
        listarDados(arq)
    elif escolha == 3:
        sn = input(f'Deseja mesmo apagar os dados contidos no banco de dados \033[33m{arq}\033[0m? [S/N] ').upper()[0]
        while sn not in 'SN':
            print('\033[31mRespota inválida!\033[0m')
            sn = input(f'Deseja mesmo apagar os dados contidos no banco de dados \033[33m{arq}\033[0m? [S/N] ').upper()[0]
        if sn == 'S':
            delDados(arq)
        else:
            print('Exclusão de dados cancelada!')
    else:
        print('PROGRAMA ENCERRADO!')
        break
