numeros = []
c = 1

while True:
    numeros.append(int(input(f'Informe o {c}º número da lista: ')))
    cond = input('Deseja continuar adicionando números em sua lista? ')
    while cond not in 'SimsimNãoNaonãonao':
        cond = input('Resposta inválida! Deseja continuar adicionando números em sua lista? ')
    if cond in 'NãoNaonãonaoNn':
        break
    else:
        c += 1

print('A quantidade de números digitados foi', len(numeros))
numerosDec = numeros[:]
numerosDec.sort(reverse=True)
print('A lista informada acima, em ordem decrescente, é: ', numerosDec)
if 5 in numeros:
    print('O número 5 aparece nas posições: ', end='')
    for i, c in enumerate(numeros):
        if c == 5:
            print(i, end='...')
else:
    print('O número 5 não se encontra na lista!')
