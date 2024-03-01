num1 = int(input('Digite a seguir, o primeiro número: '))
num2 = int(input('Digite a seguir, o segundo número: '))
num3 = int(input('Digite a seguir, o terceiro número: '))
maior = num1
menor = num1

if maior < num2:
    maior = num2

if maior < num3:
    maior = num3

print(f'O maior número entre os três é: {maior}')

if menor > num2:
    menor = num2

if menor > num3:
    menor = num3

print(f'O menor número entres os três é: {menor}')
