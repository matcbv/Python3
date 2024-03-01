num1 = int(input('Digite o primeiro valor a ser comparado: '))
num2 = int(input('Digite o segundo valor a ser comparado: '))

if num1 > num2:
    print(f'O primeiro valor ({num1}) é maior.')
elif num2 > num1:
    print(f'O segundo valor ({num2}) é maior.')
else:
    print('Não existe valor maiior pois os valores são iguais.')
