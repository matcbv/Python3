from copy import deepcopy


def verif_desconto():
    val_desc = float(input('Quanto de desconto deseja atribuir para os produtos? '))
    while not isinstance(val_desc, (int, float)):
        print('Valor de desconto inválido!')
        val_desc = float(input('Quanto de desconto deseja atribuir para os produtos? '))
    return val_desc


def como_ordena():
    opc_filtro = int(input('Escolha qual filtro quer utilizar [1 - Preco ou 2 - Nome]: '))
    while not isinstance(opc_filtro, int) and opc_filtro > 2:
        print('Filtro inválido')
        opc_filtro = int(input('Escolha qual filtro quer utilizar [1 - Preco ou 2 - Nome]: '))
    return opc_filtro


def caucula_preco(prod, desc):
    for d in prod:
        for c, v in d.items():
            if isinstance(v, (int, float)):
                d[c] = v * (100 + desc) / 100
    return deepcopy(prod)


def ordena_preco(novos_prod):
    novos_prod.sort(key=lambda v: v['preco'], reverse=True)
    return novos_prod


def ordena_nome(novos_prod):
    novos_prod.sort(key=lambda k: k['nome'], reverse=True)
    return novos_prod


def exibir_lista(prod):
    for d in prod:
        for k, v in d.items():
            print(f'{k}:', v, sep=' - ')


produtos = [{'nome': 'fraldinha', 'preco': 50},
            {'nome': 'biscoito', 'preco': 10},
            {'nome': 'tomate', 'preco': 15},
            {'nome': 'alface', 'preco': 5},
            {'nome': 'pao', 'preco': 5}]

desconto = verif_desconto()
novos_produtos = caucula_preco(produtos, desconto)
filtro = como_ordena()
print()
if filtro == 1:
    novos_produtos = ordena_preco(novos_produtos)
    exibir_lista(novos_produtos)
else:
    novos_produtos = ordena_nome(novos_produtos)
    exibir_lista(novos_produtos)
