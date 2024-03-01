def dadosProd(val, a, d):
    aumentar = val*(100+a)/100
    diminuir = val*100/(100-d)
    dobrar = val*2
    metade = val/2

    def moeda(valFim):
        conversao = f'R${valFim:.2f}'.replace('.', ',')
        return conversao
    return moeda(val), moeda(aumentar), moeda(diminuir), moeda(dobrar), moeda(metade)
