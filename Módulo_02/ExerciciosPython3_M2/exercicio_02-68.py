from random import randint

print('-' * 15)
print(' PAR OU ÍMPAR')
print('-' * 15)

cont = 0

while True:
    escolha = input('\nDeseja jogar como par ou ímpar? ').lower()
    while escolha != 'par' and escolha != 'ímpar' and escolha != 'impar':
        escolha = input('\nPpção inválida! Deseja jogar como par ou ímpar? ').lower()
    if escolha == 'par':
        print('A máquina jogará como ímpar!\n')
    else:
        print('A máquina jogará como par!\n')
    num = int(input('Escolha um número de 0 a 10: '))
    while num > 10 or num < 0:
        num = int(input('Opção inválida! Escolha um número de 0 a 10: '))
    numMaq = randint(0, 11)
    soma = num + numMaq

    if soma % 2 == 0 and escolha == 'par':
        print('Parabéns! Você venceu! O número escolhido pela máquina foi', numMaq)
        cont += 1
    elif soma % 2 != 0 and escolha == 'ímpar':
        print('Parabéns! Você venceu! O número escolhido pela máquina foi', numMaq)
        cont += 1
    else:
        print('\nPoxa vida! A máquina venceu. O número escolhida pela máquina foi', numMaq)
        break

print('\nO número de vezes que você venceu a máquina foi:', cont)
