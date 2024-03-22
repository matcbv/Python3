from datetime import datetime


# Em Python, uma classe é uma estrutura que representa um tipo de objeto. Ela é como um modelo para criar
# objetos (instâncias), definindo os atributos (características) e métodos (ações) que os objetos desse tipo podem ter.
#
# Para criar uma classe em Python, usamos a palavra-chave class, seguida pelo nome da classe.
#
# Obs.: Cada nome de uma classe deve começar com letra maiúscula por questões de padronização.
class Classe:
    # Para criarmos um método (função atrelada a uma classe), devemos criar nossa função no escopo da classe em
    # questão.

    # O _ _init_ _ é um método especial, também chamado de construtor, utilizado para a inicialização de uma instância.
    # Através dele, definimos os atributos presentes nas instâncias.
    def __init__(self, nome):  # Obs.: O parâmetro self é utilizado para referenciar a própria instância criada.
        # A estrutura será a seguinte: self.nome_do_atributo = valor recebido por parâmetro
        self.nome = nome

    def metodo(self):
        pass


# Podemos criar instâncias de uma classe criando um objeto e fazendo-o receber a execução de nossa classe. Ex.:
instancia = Classe()

# Também podemos estar criando atributos associados a uma instância em particular de nossa Classe.
# Esses atributos não estarão disponíveis para outras instâncias dessa classe. Ex:
instancia.nome = "Uma instância qualquer"
