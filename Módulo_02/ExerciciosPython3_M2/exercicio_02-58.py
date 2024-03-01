from random import randint

numAleat = randint(0, 10)
acertou = False
c = 1

while not acertou:
    num = int(input('Tente advinhar qual foi o número, entre 0 e 10, que foi escolhido pela máquina: '))
    if num > 10 or num < 0:
        print('Palpite inválido! Informe um palpite válido: ')
    else:
        if numAleat == num:
            print('Parabéns! Você acertou na tentativa número', c)
            acertou = True
        else:
            if num > numAleat:
                print('Menor...tente novamente!')
            else:
                print('Maior...tente novamente!')
        c += 1
