class Associar:
    def __init__(self):
        self.msg = 'Estamos associado classes!'


class ClasseQualquer:
    def __init__(self):
        self.txt = None


instanciaQualquer = ClasseQualquer()
# Ao atribuirmos uma classe (Associar()) a um atributo de uma instância (txt) de outra classe,
# esse atributo recebe todos os métodos e atributos da classe associada:
instanciaQualquer.txt = Associar()
print(instanciaQualquer.txt.msg)
