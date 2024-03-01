lista = []
x = [1, 2, 3]
y = x
y[1] = 4
print(x, y)
print('*' * 20)
while True:
    lista.append(input('Digite uma letra qualquer: '))
    cond = input('Gostaria de continuar preenchendo a lista?')
    if cond in 'NãoNaoNn':
        break
    elif cond not in 'SimsimSs':
        cond = input('Resposta inválida. Gostaria de continuar preenchendo a lista?')
print(lista)
