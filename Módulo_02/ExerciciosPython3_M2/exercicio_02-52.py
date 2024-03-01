cont = 0
num = int(input('Informe um número a ser verificado se é ou não primo: '))

for i in range(1, num + 1):
    if num % i == 0:
        print('\33[33m', end='')
        cont += 1
    else:
        print('\33[31m', end='')
    print(i, end='')

if cont > 2:
    print('\nO número informado não é primo.')
else:
    print('O número informado é primo.')
