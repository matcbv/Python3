from datetime import datetime


def get_time(self):
    self.hour = datetime.now().time()
    self.date = datetime.today()


def break_line():
    print()
    print('-=' * 26)
    print()


def games_list(val):
    gl = {'1º': 'Jogo da soma', '2º': 'Jogo da divisão', '3º': 'Jogo do número primo', '4º': 'Jogo do MMC'}
    for i, v in gl.items():
        print(i, '-', v)
    print()
    print(f'Você possui {val} pontos.')
    value = int(input('\nQual jogo gostaria de jogar? '))
    verification(value)
    return value


def verification(val):
    while val != 1 and val != 2 and val != 3 and val != 4:
        print('Opção inválida! Informe 1, 2, 3 ou 4.')
        answer = int(input('Qual jogo gostaria de jogar? '))
        return answer


def bank_account(init_val, val, answer):
    if answer == 'w':
        new_value = init_val - val
        print()
        print('Poxa vida! Não foi dessa vez... -1 ponto')
        print()
        return new_value
    else:
        new_value = init_val + val
        print()
        print('Parabéns! Você é muito bom nisso... +1 ponto')
        print()
        return new_value


def yerOrNo(answer):
    answer[0].lower()
    while answer != 'sim' and answer != 'não' and answer != 'nao':
        print('Resposta inválida!')
        answer = input('Vamos tentar outra vez! Responda com sim ou não: ')
    if answer == 'sim':
        return True
    else:
        return False
