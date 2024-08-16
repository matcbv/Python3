# dir(obj) - Responsável por mostrar os atributos disponíveis num objeto.
# hasattr(obj, atributo) - Responsável por verificar se o objeto possui um atributo em específico.
# getattr(obj, atributo) - Responsável por executar um atributo contido num objeto.

class MyClass:
    def __init__(self):
        self.name = 'Matheus'
        self.lastname = 'Cerqueira'


me = MyClass()

# Abaixo, estaremos verificando se o atributo passado por parâmetro existe com o hasattr.
# Caso exista, estaremos executando-o através do getattr.
# Obs.: Os atributos passados para hasattr e getattr devem ser em formato de string.
if hasattr(me, 'name'):
    print(f'O atributo name existe.')
    print(getattr(me, 'name'))

# Podemos estar verificando todos os atributos para aquele objeto com o dir.
print()
print(dir(me))
