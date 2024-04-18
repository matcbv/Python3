# dir(obj) - Responsável por mostrar os atributos disponíveis num objeto.
# hasattr(obj, atributo) - Responsável por verificar se o objeto possui um atributo em específico.
# getattr(obj, atributo) - Responsável por executar um atributo contido num objeto.

var = 'texto'
metodo = 'upper'

# Abaixo, estaremos verificando se o atributo passado por parâmetro existe com o hasattr.
# Caso exista, estaremos executando-o através do getattr.
if hasattr(var, metodo):
    print(f'O atributo {metodo} existe.')
    print(getattr(var, metodo))

# Podemos estar verificando todos os atributos para aquele objeto com o dir.
print()
print(dir(var))
