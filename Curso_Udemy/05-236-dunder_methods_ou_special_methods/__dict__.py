# O método dict é responsável por retornar um dicionário com o par chave e valor de um objeto.
class Foo:
    # Abaixo iremos criar uma docstring par documentação de nossa classe
    """
    Está é uma função de exemplo para o uso do método especial __dict__
    """
    def __init__(self, nome):
        self.nome = nome

    def metodo(self):
        print('Olá, mundo! Meu nome é', self.nome)


obj = Foo('Matheus')
# Ao utilizarmos __dict__ em nossa instância, será retornado um par chave e valor como vimos anteriormente.
print(obj.__dict__)
# Ja em nossa classe, vemos um dicionários contente diversos elementos de nossa classe.
print('-'*60)
print(Foo.__dict__)

# O resultado acima é o seguinte:
# {
#   '__module__': '__main__',
#   '__doc__': '\n    Está é uma função de exemplo para o uso do método especial __dict__\n    ',
#   '__init__': <function Foo.__init__ at 0x00000252FE579E40>,
#   'metodo': <function Foo.metodo at 0x00000252FE579EE0>,
#   '__dict__': <attribute '__dict__' of 'Foo' objects>,
#   '__weakref__': <attribute '__weakref__' of 'Foo' objects>
# }
#
# __module__ é um método especial que indica o módulo a que essa classe pertence. Nesse caso __main__.
# __doc__ é um método especial que contém a docstring da nossa classe.
# __init__ é método especial para inicialização da nossa instância. O valor será a própria representação
# da função __init__
# metodo é nosso método criado em nossa classe. O valor será sua representação na classe.
# __dict__ é o próprio método __dict__ que utilizamos. Ele mesmo também é adicionado.
# __weakreaf__ é um atributo especial que fornece suporte para referências fracas (weak references)
# à instância da classe.
