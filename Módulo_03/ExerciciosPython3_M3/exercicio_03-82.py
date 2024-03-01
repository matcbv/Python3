numeros = []
numerosPar = []
numerosImpar = []

while True:
    numeros.append(int(input('Informe um número a ser adicionado na lista: ')))
    cond = input('Deseja continuar adicionando números a lista? ')
    while cond not in 'SimsimNãoNaonãonao':
        cond = input('Resposta Inválida. Deseja continuar adicionando números a lista? ')
    if cond in 'NãoNaoNn':
        break
for c in numeros:
    if c % 2 == 0:
        numerosPar.append(c)
    else:
        numerosImpar.append(c)

print(numeros)
print(numerosPar)
print(numerosImpar)
