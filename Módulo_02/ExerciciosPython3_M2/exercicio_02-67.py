num = int(input('Informe o número a ser cauculada a taboada: \n'))
print('=~' * 7)

while True:
    if num < 0:
        break
    else:
        for cont in range(1, 11):
            print(f'{num} x {cont} =', num * cont)
    print('=~' * 7)
    num = int(input('Informe o número a ser cauculada a taboada: '))

print('Programa encerrado.')
