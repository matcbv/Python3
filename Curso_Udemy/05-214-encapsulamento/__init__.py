# Quando falamos de encapsulamento em linguagens de programação, estamos nos referindo
# ao uso de modificadores de acesso nos atributos e métodos de nossa classe. Eles podem
# ser dos tipos: public, protected e private.
# Em Python, não temos os chamados modificadores, porém os utilizamos por convenção.

# public (sem underline): Podemos acessar tal atributo ou método de qualquer local de nosso código.
# protected (um underline: _): O atributo ou método só deve ser acessado em sua classe, ou suas subclasses.
# private (dois underlines: __): O atributo ou método só deve ser acessado em sua classe. Nesse caso
# ocorre o chamado "name mangling".

# Obs.: Também podemos criar classes protegidas ou privadas, as quais não devem ser utilizadas fora
# de módulo em que está contida.

class Encapsulamento:
    def __init__(self):
        self.public = 'Este atributo é público'
        self._protected = 'Este atributo é protegido'
        self.__private = 'Este atributo é privado'

    def metodo_publico(self):
        # Os métodos e atributos protegidos e privados podem ser utilizados dentro de métodos públicos.
        print('Esse é um método público.')
        print(self._protected, self.__metodo_privado())
        self._metodo_protegido()
        self.__metodo_privado()

    def _metodo_protegido(self):
        print('Esse é um método protegido.')

    def __metodo_privado(self):
        print('Esse é um método privado.')


# Ao criarmos um atributo ou método privados, ocorre o chamado name mangling. Esse, realiza uma mudança na
# forma de acesso a esses elementos. Ex.:

obj = Encapsulamento()
# Para acessarmos método privador devemo utilizar a estrutura: instância._Classe__nome_método()
obj._Encapsulamento__metodo_privado()
