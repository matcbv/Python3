numSeq = int(input('Informe o número de termos da Sequência de Fibonacci a serem exibidos: '))
termo1 = 0
termo2 = 1
soma = 0
i = 0

while i < numSeq:
    if i < 2:
        print(soma)
        soma = termo1 + termo2
        i += 1
    else:
        soma = termo1 + termo2
        print(soma)
        termo1 = termo2
        termo2 = soma
        i += 1
