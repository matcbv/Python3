# Os métodos de classe (class methods) são métodos que se referem a própria classe (por meio do parâmetro especial cls),
# ao contrário dos métodos padrão, que se referem as instâncias.
# Nos métodos de classe, não temos acesso direto as instâncias através do parâmetro especial self, já
# que nos referênciamos a própria classe através do parâmetro especial cls. Entretanto, conseguimos
# ter acesso às instâncias caso as referênciarmos em nosso método de classe. Ex.:
class ClasseComMetodos:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Através dos métodos de classe, podemos criar as chamadas fábricas (factories). Nesse caso em
    # específico, um método fábrica. Essa fábrica em nosso exemplo, será uma fábrica de instâncias.
    @classmethod
    def fabrica_de_instancias(cls, idade):
        # Estaremos fixando um nome, e passando a idade por parâmetro. Iremos retornar a execução
        # da classe (cls() = ClasseComMetodos()).
        return cls('Matheus', idade)

    @classmethod
    def acessando_instancias(cls, inst):
        # Podemos acessar uma instância já criada nos referenciando a ela, seja passando-a por
        # parâmetro, ou acessando-a diretamente caso essa esteja em um escopo acessível.
        print(inst.nome, inst.idade)
        print(instancia_02.nome, instancia_02.idade)


instancia = ClasseComMetodos.fabrica_de_instancias(21)
instancia_02 = ClasseComMetodos.fabrica_de_instancias(25)
ClasseComMetodos.acessando_instancias(instancia)
