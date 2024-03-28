class Superclasse:
    def __init__(self):
        self.valor = 'Um texto qualquer'
        self.numero = 11

    # O método abaixo irá informar o nome da classe que em ação:
    def mostrar_nome_classe(self):
        print(self.__class__.__name__)


# Para uma classe herdar outra, iremos especificar o nome da superclasse por parênteses. Esta subclasse
# herdará todos os elementos da superclasse especificada.
class Subclasse(Superclasse):
    ...


obj = Subclasse()
# Ao chamar o método mostrar_nome_classe, vemos que o nome da subclasse é exibido, já que estamos chamando
# a função através dela. O método passa a também ser pertencente a ela.
obj.mostrar_nome_classe()
print(obj.valor, obj.numero, sep='\n')
print('-'*30)

# Em heranças, trabalhamos com o chamado "Method Resolution Order (MRO)". Isso define a ordem de busca
# que o Python irá seguir durante a herança. Podemos encontrar o MRO através da função help ou do
# método mro:

print(Subclasse.mro())
print('-'*30)


# Por padrão, o Python sempre segue a seguinte ordem: subclasse -> superclasse -> builtins.object
# Ex.:
class Principal:
    texto = 'valor da classe principal'


# Para uma classe herdar outra, iremos especificar o nome da superclasse por parênteses. Esta subclasse
# herdará todos os elementos da superclasse especificada.
class Secundaria(Principal):
    texto = 'valor da classe secundária.'


obj_02 = Secundaria()
# Como podemos ver, ele exibiu o texto da classe secundária, pois essa vem primeiro no MRO.
print(obj_02.texto)
