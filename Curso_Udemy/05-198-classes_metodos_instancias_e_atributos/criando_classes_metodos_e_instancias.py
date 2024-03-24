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
    # Ele é iniciado instantaneamente assim que chamamos nossa classe. Com ele, definimos os atributos presentes nas
    # instâncias.
    def __init__(self, nome, sobrenome):
        # Obs.: O parâmetro self é utilizado para referenciar a própria instância criada. Cada instância de uma classe
        # em Python tem seu próprio self. Quando você cria uma nova instância de uma classe, o Python aloca memória
        # para armazenar os atributos e métodos dessa instância específica.

        # Quando você chama um método em uma instância, como objeto.método(), o Python automaticamente passa a própria
        # instância como o primeiro argumento para o método, e esse argumento é referenciado como self dentro do método.
        # Assim, cada método opera nos atributos específicos da instância à qual ele pertence, usando self para acessar
        # esses atributos
        # A estrutura será a seguinte: self.nome_do_atributo = valor recebido por parâmetro
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = 21  # Quando definimos um atributo com um valor que não é passado nos parâmetros, chamamos de
        # Hard coded. Esse valor serão os mesmo para todas as instâncias.

    def metodo(self):
        # Podemos chamar nossa instância e seus atributos em qualquer método de nossa classe com self.atributo.
        print(f'{self.nome} {self.sobrenome} tem {self.idade}')


# Podemos criar instâncias de uma classe criando um objeto e fazendo-o receber a execução de nossa classe. Ex.:
instancia = Classe('Matheus', 'Cerqueira')
instancia.metodo()
# Também podemos estar criando atributos associados a uma instância em particular de nossa Classe.
# Esses atributos não estarão disponíveis para outras instâncias dessa classe. Ex:
instancia.nome = "Uma instância qualquer"
