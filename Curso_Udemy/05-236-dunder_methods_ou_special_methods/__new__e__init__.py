# Os métodos especiais __new__ e __init__ são responsáveis por criar e retornar um novo objeto e
# inicializar uma instância, respectivamente.

# Em nosso método __new__, devemos passar a referência a classe (cls), já que será responsável por criar
# a instância referente à aquela classe.
#
# Um método __new__ deve retornar um objeto, enquanto __init__ não deve retornar nada (None).

# Nossas classes herdam por padrão da classe object. Essa é uma classe mais ao topo, sendo responsável
# pela criação de nossas instâncias.
class NossaClasse:

    # O método new costuma não ser utilizado geralmente, porém, uma de suas possíveis
    # utilidades, é a execução de ações antes ou depois da criação do nosso objeto.
    # Por padrão, passamos args e kwargs para não nos preocuparmos com a quantidade de parâmetros recebidos.
    def __new__(cls, *args, **kwargs):
        print('Mensagem antes de criar a instância.')
        # É recomendado utilizarmos o super() ao invés de object ao criarmos nossas instâncias em __new__.
        instancia = super().__new__(cls)
        print('Mensagem depois de criar a instância.')
        # Podemos inclusive criar atributos para nossa instância. Dessa forma, todas as instâncias criadas
        # terão esse atributo:
        instancia.valor = 'texto qualquer'
        # Retornando nosso objeto:
        return instancia

    def __init__(self, x):
        self.x = x
        print('__init__ está sendo acionado...')


# Quando criamos uma instância, os seguintes passos são executados:
# obj = object.__new__(NossaClasse)
# obj.__init__()
# print(obj)

obj = NossaClasse(11)
print(obj.valor)
print(obj.x)
