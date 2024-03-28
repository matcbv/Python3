# Em Python, também temos a chamada herança múltipla. Nas heranças múltiplas, uma mesma classe pode herdar mais de
# uma classe. Temos que ter cuidado ao utilizarmos a herança múltipla, para que nosso código não acabe ficando muito
# complexo e confuso.

# Veremos agora um exemplo de herança múltipla. Trabalharemos com as classes A, B, C e D, realizando as seguintes
# heranças: D(B, C) - C(A) - B(A) - A
#
#           A
#         /   \
#        B     C
#         \   /
#           D

# Podemos lidar com casos em que há uma situação parecida com a de cima. Caso as classes B e C ou até então B, C e A
# possuírem métodos de mesmo Python 3 usa C3 superclass linearization para gerar o MRO.

# Para saber a ordem de chamada dos métodos, utilizamos o método de classe mro(), como vimos anteriormente, ou o
# atributo especial __mro__.

# Veremos o exemplo acima em prática a seguir:

class A:
    def quem_sou_eu(self):
        print(self.__class__.__name__)


class B(A):
    def quem_sou_eu(self):
        print(self.__class__.__name__)


class C(A):
    def quem_sou_eu(self):
        print(self.__class__.__name__)


# A ordem dos parâmetros irá afetar diretamente na ordem do MRO. O primeiro parâmetro virá primeiro e assim
# sucessivamente.
class D(B, C):
    def quem_sou_eu(self):
        print(self.__class__.__name__)


obj = D()
obj.quem_sou_eu()
# Aqui conseguimos visualizar o MRO da classe D.
print(D.mro())
