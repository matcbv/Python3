# O setter é mais um dos usos do método especial @property. Por meio de um setter, conseguimos
# aplicar um valor para os atributos de nossa classe.

class ClasseComSetter:
    def __init__(self, name):
        # Ao lidarmos com getters e setters, é uma prática comum que os atributos utilizados
        # por eles sejam antecedidos por um ou dois underlines (_ ou __) por convenção.
        # Isso significa que esses atributos são protegidos, e não devem ser acessados diretamente.
        # Com o atributo name, iremos chamar diretamente nosso setter na criação das instâncias e ele será
        # responsável por definir nosso atributo _nome e atribuir um valor a ele.
        self.name = name
        # Para obtermos a idade, iremos utilizar um método diferente. Não iremos chamar diretamente nosso
        # setter, nos referindo diretamente ao _age atributo. 
        self._age = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


instancia = ClasseComSetter('Matheus')
print(instancia.name)
# Como podemos ver a seguir, através do setter, conseguimos atribuir valores para nossos atributos.
instancia.name = 'Mariana'
print(instancia.name)
# Definiremos agora, um valor para o atributo _age, através do setter age.
instancia.age = 29
print(instancia.age)
