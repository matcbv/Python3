def escreva(frase):
    tam = len(frase)
    print('-'*tam)
    print(frase)
    print('-' * tam)


while True:
    escreva(input('\nEscreva uma frase qualquer: '))
    cond = input('\nDeseja inserir uma nova frase? [S/N] ').upper()[0]
    while cond not in 'SN':
        print('Resposta inválida.')
        cond = input('\nDeseja inserir uma nova frase? [S/N] ').upper()[0]
    if cond == 'N':
        break
