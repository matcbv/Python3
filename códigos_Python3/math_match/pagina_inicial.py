from funcoes_math_match.funcoes_verif import *
from funcoes_math_match.funcoes_game import *
from funcoes_math_match.cadastro import *
from time import sleep

i = 0
print()
print('-='*10, 'MATH MATCH', '-='*10)
print('\nBem-vindo a MATH MATCH, o jogo matemático!')
ans = yerOrNo(input('\nVocê já possui cadastro no MATH MATCH: (Sim/Não) '))
if ans:
    print()
    print('Ótimo! Vamos começar...')
else:
    break_line()
    register()

initialValue = 10
last_value = 0
sleep(3)

break_line()
while True:
    game_choice = games_list(last_value)
    if i == 0:
        if game_choice == 1:
            WorC = plus()
            last_value = bank_account(initialValue, 1, WorC)
        elif game_choice == 2:
            pass
        elif game_choice == 3:
            WorC = prime_number()
            last_value = bank_account(initialValue, 1, WorC)
        else:
            WorC = mmc()
            last_value = bank_account(initialValue, 1, WorC)
    else:
        if game_choice == 1:
            WorC = plus()
            last_value = bank_account(last_value, 1, WorC)
        elif game_choice == 2:
            pass
        elif game_choice == 3:
            WorC = prime_number()
        else:
            WorC = mmc()
            last_value = bank_account(initialValue, 1, WorC)
    keep_play = input('Gostaria de continuar jogando? (Sim/Não) ').lower()
    yerOrNo(keep_play)
    break_line()
    if keep_play == 'nao':
        break
