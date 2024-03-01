from random import choice

print('\nJOKENPÔ\n')
escolhas = ['pedra', 'papel', 'tesoura']

jogoM = choice(escolhas)
jogoP = input('Escolha entre: Pedra, Papel e Tesoura. ').lower()

if jogoM == jogoP:
    print('Deu empate!')
elif jogoM == 'pedra' and jogoP == 'tesoura' or jogoM == 'papel' and jogoP == 'pedra' or jogoM == 'tesoura' and jogoP == 'papel':
    print(f'Que pena! A máquina escolheu {jogoM}, você perdeu.')
else:
    print(f'Parabéns! A máquina escolheu {jogoM}, você venceu.')
