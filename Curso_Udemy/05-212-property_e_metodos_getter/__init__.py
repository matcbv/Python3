# @property é um decorador especial que faz com que um método se comporte como um atributo, sendo
# mais específico, um atributo de propriedade.
# Uma propriedade é um método que permite que você acesse, modifique e delete valores de um objeto
# de uma maneira controlada, sem a necessidade de chamar métodos getter e setter explicitamente,
# sendo chamada em forma de atributo. Uma propriedade pode ser criada através do decorador
# @property ou da função property(). Ex.:

class ClasseComGetter:
    def __init__(self):
        self.valor = 'valor qualquer'

    @property
    def get_value(self):
        print('getter foi acessado!')
        return self.valor


# ----------------------------------------------
# Código cliente (Código em que nosso código é utilizado):

instancia = ClasseComGetter()
print(instancia.get_value)

# As vantagens de utilizar uma propriedade são:
# - Manter código cliente em funcionamento: caso precisarmos alterar algo em nosso atributos, como
# seu nome, por exemplo, podemos alterá-lo em nosso getter e o funcionamento será mantido.
# - Criação de getters e setters: podemos criar getters e setters para obtermos e aplicarmos
# valores, respectivamente.
# - Realizar ações ao lidar com atributos: antes de retornarmos o valor do atributo, podemos
# realizar as ações que nos forem convenientes.
