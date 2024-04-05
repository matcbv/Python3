# Quando utilizamos uma classe como decoradora, o método a ser decorado passa a ser uma
# instância dessa classe, e a função se torna um atributo dessa instância.
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
def soma(x, y):
    return x + y


resultado = soma(2, 2)
print(resultado)
