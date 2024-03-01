from random import randint

escolha = int(input('Escolha um número de 0 a 5 e veja se acerta a resposta! '))
resp = randint(0, 5)

if escolha == resp:
    print('Parabéns! Você acertou.')
else:
    print(f'Poxa vida! Não foi dessa vez. O número correto era {resp}')
