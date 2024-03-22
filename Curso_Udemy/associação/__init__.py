class Associar:
    def __init__(self):
        self.msg = 'Estamos associado classes!'


class ClasseQualquer:
    def __init__(self):
        self.txt = None


instanciaQualquer = ClasseQualquer()
# Ao atribuirmos uma 05-198-classes (Associar()) a um atributo de uma instância (txt) de outra 05-198-classes,
# esse atributo recebe todos os métodos e atributos da 05-198-classes associada:
instanciaQualquer.txt = Associar()
print(instanciaQualquer.txt.msg)
