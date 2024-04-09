def add_repr(cls):
    def my_repr(self):
        class_name = self.__class__.__name__
        clas_dict = self.__dict__
        class_repr = f'{class_name}: {clas_dict}'
        return class_repr
    cls.__repr__ = my_repr
    return cls


# Iremos receber o método nome_time em nossa função decoradora abaixo:
def mostra_time(metodo):
    # Iremos utilizar o conceito de closure, adiando a chamada da função interna
    # contendo o resultado da chamada de metodo, que é a função nome_time que foi
    # passada por parâmetro.
    def interna(valor, *args, **kwargs):
        resultado = metodo(valor, *args, **kwargs)
        return resultado
    return interna


@add_repr
class Times:
    def __init__(self, nome):
        self.nome = nome

    @mostra_time
    def nome_time(self):
        return f'Nome: {self.nome}'


time01 = Times('Flamengo')
time02 = Times('Corinthians')

# Quando chamamos a função nome_time, os seguintes passos são chamados:
# A função nome_time é passada por parâmetro para a função decoradora mostra_time

# A função mostra mostra_time retorna a função interna, logo, ao nos referirmos a nome_time,
# a função interna será chamada.

# Ao passarmos nossa instância por parâmetro, interna o receberá em seu parâmetro valor.

# A função interna retornará o objeto resultado, cujo valor será o retorno de método,
# recebendo o parâmetro valor proveniente da unção interna. metodo é a função nome_time
# que foi passada por parâmetro para a função decoradora, e valor, a instância que passamos para interna.

# Logo, interna retornára o objeto resultado, contendo a f string retornada por nome_time, que por fim,
# será exibido na tela.

time01.nome_time()
time02.nome_time()

