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
# time01.nome_time(), isso é equivalente a nome_time(self), logo nome_time(time01)

# Como nome_time pertence a um decorador, logo: nome_time = mostra_time(nome_time),
# portanto: mostra_time(nome_time)(time01).

# Como mostra_time retorna uma função (interna), teremos: interna(time01). Logo, o parâmetro valor
# receberá a instância time01.

# Em interna(time01), temos nosso objeto resultado. Ele receberá o resultado da função metodo.
# metodo é a função nome_time que foi passada por parâmetro para a função decoradora.
#
# Por parâmetro, passaremos para metodo a instância time01 que foi passada para valor na função interna.

# Isso resultará na f string retornada por nome_time, que por fim, será exibido na tela.

time01.nome_time()
time02.nome_time()

