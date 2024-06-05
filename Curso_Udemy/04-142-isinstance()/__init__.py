# A função isinstance() é uma função embutido do Python responsável por verificar se um objeto pertence
# a uma determinada classe. Ex.:

lista = [1, 1.1, 'texto', {'chave': 'valor'}, (1, 'a'), [1, 2]]

for c in lista:
    if isinstance(c, (int, float)):
        print('Número:', c)
    elif isinstance(c, str):
        print('Texto:', c)
    elif isinstance(c, dict):
        print('Dicionário:', c)
    elif isinstance(c, tuple):
        print('Tupla:', c)
    elif isinstance(c, list):
        print('Lista:', c)
    else:
        print('Tipo não identificado!')

