soma = 0

for i in range(0, 6):
    num = int(input('Informe um número qualquer: '))
    if num % 2 == 0:
        soma += num

print('A soma dos números pares informados acima é:', soma)
