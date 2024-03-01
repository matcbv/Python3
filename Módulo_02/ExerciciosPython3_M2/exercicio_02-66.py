from time import sleep
num = soma = c = 0

while True:
    num = int(input('Informe um número a ser somado: '))
    if num == 999:
        break
    soma += num
    c += 1

print('...')
sleep(1)
if c == 0:
    print('Nenhum número foi informado.')
elif c == 1:
    print(f'Não existe soma de um só número.')
else:
    print(f'A soma dos {c} números informados acima é: {soma}')
