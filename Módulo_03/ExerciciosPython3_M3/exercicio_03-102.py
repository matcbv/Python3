def fatorial(num, show=False):
    resp = num
    if show:
        for c in range(num-1, 0, -1):
            print(f'{resp} x {c} = ', end='')
            resp *= c
            print(resp)
    else:
        for c in range(num-1, 0, -1):
            resp *= c
    print('O fatorial do número informado é:', resp)


#Programa principal
numInit = int(input('Informe o número a ser calculado o fatorial: '))
cond = input('Deseja que o processo de calculo seja exibido? [S/N] ').upper()[0]
while cond not in 'SN':
    print('Resposta inválida!')
    cond = input('Deseja que o processo de calculo seja exibido? [S/N] ').upper()[0]
print()
if cond == 'S':
    fatorial(numInit, show=True)
else:
    fatorial(numInit, show=False)
