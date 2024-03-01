from random import randint
num = 0
total = []
numeros = []
numJogos = int(input('Quantos jogos deseja que sejam sorteados? '))

for cont in range(0, numJogos):
    for i in range(0, 6):
        num = randint(1, 60)
        while num in numeros:
            num = randint(1, 60)
        numeros.append(num)
    total.append(numeros[:])
    numeros.clear()

for jogos in total:
    print(jogos)
