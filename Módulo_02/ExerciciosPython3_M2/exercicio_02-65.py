resp = 'S'
soma = i = maiorNum = menorNum = 0

while resp == 'S':
    num = int(input('Informe um número a ser somado feita a média: '))
    soma += num
    if i == 0:
        maiorNum = menorNum = num
    else:
        if num > maiorNum:
            maiorNum = num
        if num < menorNum:
            menorNum = num
    i += 1
    resp = input('Deseja continuar somando? (S / N) ').upper().strip()[0]

print(f'A média da soma dos números informados acima é {soma / i}, onde o maior foi {maiorNum} e o menor {menorNum}')
