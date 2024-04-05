# Utilizaremos uma função como decorador para estar adicionando um objeto ao nosso método especial __repr__.
# Isso também será feito por meio de uma função.

# Função que irá retornar nosso objeto para o método especial __repr__:
def my_repr(self):
    class_name = self.__class__.__name__
    # O método especial __dict__ retorna um dicionário que contém os atributos de um objeto.
    # As chaves serão os nomes dos atributos e o valor das chaves serão os respectivos valores desses atributos.
    clas_dict = self.__dict__
    class_repr = f'{class_name}: {clas_dict}'
    return class_repr


# Nossa função decoradora:
def add_repr(cls):
    # Podemos definir a função que irá retornar para __repr__ dentro ou fora da nossa função decoradora.
    # O resultador será o mesmo em ambas as situações.
    # def my_repr(self):
    #     class_name = self.__class__.__name__
    #     clas_dict = self.__dict__
    #     class_repr = f'{class_name}: {clas_dict}'
    #     return class_repr
    cls.__repr__ = my_repr
    return cls


# Agora, utilizaremos nossa função add_repr como decorador. Dessa maneira, ela é chamada automaticamente
# recebendo a classe Times, e retornando a classe cls. Essa classe será a utilizada quando nos referirmos
# à classe Times.
@add_repr
class Times:
    def __init__(self, nome):
        self.nome = nome


@add_repr
class Selecoes:
    def __init__(self, nome):
        self.nome = nome


time01 = Times('Flamengo')
time02 = Times('Corinthians')

print(time01, time02, sep=', ')

selecao01 = Selecoes('Brasil')
selecao02 = Selecoes('Argentina')

print(selecao01, selecao02, sep=', ')
