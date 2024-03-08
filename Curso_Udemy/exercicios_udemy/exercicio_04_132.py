def repetidos(lst):
    nums_repetidos = []
    for n in lst:
        quant = lst.count(n)
        if quant >= 2 and n not in nums_repetidos:
            nums_repetidos.append(n)
    return nums_repetidos


def primeira_rep(lst):
    maior_indice = 0
    for n in lst:
        if lst.count(n) >= 2:
            lst.index(n)
            if lst.index(n) > maior_indice:
                maior_indice = lst.index(n)
    if maior_indice == 0:
        return -1
    else:
        return lst[maior_indice]
# -------------------------//--------------------//-------------------------


# Código Principal

lista = []
while True:
    lista.append(int(input('Adicione um número a lista: ')))
    continuar = input('Deseja continuar adicionando números na lista? [S/N] ').lower()[0]
    while continuar not in 'sn':
        print('Resposta inválida!')
        continuar = input('Deseja continuar adicionando números na lista? [S/N] ').lower()[0]
    if continuar == 'n':
        break

lista_repetidos = repetidos(lista)
primeiro = primeira_rep(lista)
print(f'A lista {lista} possui {len(lista_repetidos)} números repetidos. A repetição deu início com o número {primeiro}.')
print('Os números repetidos foram:')
for i in lista_repetidos:
    print(i, end='...')
