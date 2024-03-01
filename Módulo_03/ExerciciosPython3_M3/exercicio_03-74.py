from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10), randint(1, 10))
# maiorNum = menorNum = 0

for cont in range(0, 5):
    print(f'{cont + 1}ª - {numeros[cont]}')
# Primeira opção para exibir o maior e menor valor:
#     if numeros[cont] > maiorNum:
#         maiorNum = numeros[cont]
#     if menorNum > numeros[cont] or cont == 0:
#         menorNum = numeros[cont]
#
# print('O maior número entre os cinco acima é:', maiorNum)
# print('O menor número entre os cinco acima é:', menorNum)

# Segunda opção:
print('O maior número entre os cinco acima é:', max(numeros))
print('O menor número entre os cinco acima é:', min(numeros))
