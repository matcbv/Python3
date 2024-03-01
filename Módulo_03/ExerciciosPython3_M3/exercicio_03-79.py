numeros = []
# FORMA FEITA POR MIM:
# c = 0
# while True:
#     numeros.append(int(input('Informe a seguir um número qualquer: ')))
#     if c != 0 and numeros[c] in numeros[:len(numeros)-1]:
#         numeros.pop()
#     else:
#         c += 1
#     cond = input('Deseja continuar adicionando números à lista? ')
#     while cond not in 'SimsimNãoNaonãonao':
#         cond = input('Resposta inválida. Informe uma resposta válida: ')
#     if cond in 'NãoNaoNn':
#         break

# FORMA INDICADA:
while True:
    num = int(input('Informe a seguir um número qualquer: '))
    if num not in numeros:
        numeros.append(num)
    else:
        print('Esse número já se encontra na lista!')
    cond = input('Deseja continuar adicionando números a lista? ')
    while cond not in 'SimsimNãonãoNaonao':
        cond = input('Resposta Inválida! Deseja continuar adicionando números a lista? ')
    if cond in 'NãonãoNaonao':
        break
numeros.sort()
print('\nA lista com os valores informados anteriormente, em ordem crescente, é:')
for pos, c in enumerate(numeros):
    print(f'{pos+1}º - ', c, sep='')
