# O método partial permite criarmos uma nova função por meio de outra, pré-definindo seus argumentos.
# Isso permite uma chamada mais coesa da função, principalmente quando existem muitos parâmetros nela.
# Caso seja necessário alterar o valor de algum dos parâmetros, basta alterarmos na função criada pelo
# método partial.
from functools import partial


def func_calc_juros(val_inicial, num_parcelas, juros_parcela, entrada):
    valor_com_entrada = val_inicial - entrada
    val_final = valor_com_entrada + (num_parcelas * (valor_com_entrada * juros_parcela / 100))
    return round(val_final, 2)


calc_juros = partial(func_calc_juros, juros_parcela=1.2, entrada=0)
print('R$', calc_juros(30000, 48), sep='')
