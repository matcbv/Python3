from time import sleep
cores = ('\033[0m',  # 0 - Nenhum
         '\033[7m',  # 1 - Branco
         '\033[0;30;41m',  # 2 - Vermelho
         '\033[0;30;42m',  # 3 -Verde
         '\033[0;30;43m',  # 4 - Amarelo
         '\033[0;30;44m'  # 5 - Azul
         )


def titulo(msg, cor=0):
    print(cores[cor], end='')
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))
    print(cores[0], end='')


def manual(obj):
    titulo(f'Buscando informações sobre \'{duvida.lower()}\'', 5)
    sleep(1)
    print(cores[1], end='')
    help(obj)
    print(cores[0], end='')


while True:
    titulo('Manual do Python', 3)
    titulo('Quando quiser encerrar o programa, digite "FIM"', 2)
    duvida = input('Informe o objeto a ser explicado: ').lower()
    if duvida == 'fim':
        titulo('ATÉ LOGO!', 4)
        break
    else:
        manual(duvida)
