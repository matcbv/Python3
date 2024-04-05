class Somar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            return func(*args, **kwargs)*self._multiplicador
        return interna

# Quando chamamos nossa função, estamos realizando os seguintes passos:
# Nossa função se tornará uma instância de soma, assim como no exemplo anterior:
# soma = Soma(10)(soma) - O (soma) ao final é feito de maneira automática pelo Python,
# como adicionamos o parâmetro (10), a função a ser decorada foi adicionada seguidamente.

# Isso irá criar uma instância da classe Soma, e chamando-a logo em seguida, passando a função
# soma como argumento para o método especial __call__.

# __call__ por sua vez, retornará a função interna. Quando chamarmos soma(2, 2) ao final de
# nosso código, estaremos passando (2, 2) como argumento *args para a função interna, que
# resultará no retorno do resultado da chamada de func (soma).

# Por trás dos bastidores, seria algo como:
# soma = object.__new__(Somar)
# soma = __init__(10)
# soma(soma) = interna


@Somar(10)
def soma(x, y):
    return x + y


resultado = soma(2, 2)
