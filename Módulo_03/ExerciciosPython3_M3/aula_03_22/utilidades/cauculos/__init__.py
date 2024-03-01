def aumentar(val, porc):
    valFim = (val*porc/100) + val
    formatar = input('Deseja que o valor seja formatado em forma de moeda? [S/N] ').upper()[0]
    if formatar == 'N':
        formatar = False
    else:
        formatar = True
    return valFim, formatar


def diminuir(val, porc):
    porc = 100 - porc
    valFim = val*porc/100
    formatar = input('Deseja que o valor seja formatado em forma de moeda? [S/N] ').upper()[0]
    if formatar == 'N':
        formatar = False
    else:
        formatar = True
    return valFim, formatar


def dobro(val):
    valFim = val*2
    formatar = input('Deseja que o valor seja formatado em forma de moeda? [S/N] ').upper()[0]
    if formatar == 'N':
        formatar = False
    else:
        formatar = True
    return valFim, formatar


def metade(val):
    valFim = val/2
    formatar = input('Deseja que o valor seja formatado em forma de moeda? [S/N] ').upper()[0]
    if formatar == 'N':
        formatar = False
    else:
        formatar = True
    return valFim, formatar


def moeda(val, vf=False):
    valFim = f'R${val:.2f}'.replace('.', ',')
    return valFim if vf else val
