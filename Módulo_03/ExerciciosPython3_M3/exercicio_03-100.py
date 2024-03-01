def sorteia(lst):
    from random import randint
    for c in range(0, 5):
        lst.append(randint(0, 100))
    print('Os números sorteados foram: ', lst)


def somaPar(lstSort):
    soma = 0
    for c in lstSort:
        if c % 2 == 0:
            soma += c
    print('A soma dos números pares sorteados é: ', soma)


numeros = []
sorteia(numeros)
somaPar(numeros)
