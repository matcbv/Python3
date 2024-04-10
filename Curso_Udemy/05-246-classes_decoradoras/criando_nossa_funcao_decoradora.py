# Quando utilizamos uma classe como decoradora, o método/função a ser decorado,
# passa a ser uma instância dessa classe, e o verdadeiro método/função se torna um
# atributo dessa instância (no exemplo abaixo, o atributo func).
class Somar:
    def __init__(self, func):
        # func passa a ser a função soma.
        self.func = func

    # Para conseguirmos tornar nossa instância chamável, utilizaremos o método especial
    # __call__, visto anteriormente:
    def __call__(self, *args, **kwargs):
        # Agora conseguimos chamar nossa função que está contida no atributo func:
        return self.func(*args, **kwargs)


@Somar
# soma passa a ser uma instância de Somar.
def soma(x, y):
    return x + y


# Quando chamamos soma, estamos chamando uma instância da classe Somar.
# Caso não tivéssemos implementado o método __call__, teríamos que chamar nossa
# função da seguinte maneira: soma.func(2, 2). Entretanto, __call__ torna nossa
# instância chamável.
resultado = soma(2, 2)
print(resultado)
