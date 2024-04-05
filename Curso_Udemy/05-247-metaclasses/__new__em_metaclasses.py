def my_repr(teste):
    print(type(teste))
    return f'{type(teste).__name__}, {teste.__dict__}'


# Para criarmos uma metaclasse, devemos criar uma classe que herda de type:
class Meta(type):
    # Com o método especial __new__ em nossa metaclasse, estaremos criando uma instância do tipo Meta,
    # que será nossa classe ClasseQualquer.
    def __new__(mcs, name, base, dct):
        print('Criando nossa metaclasse')
        classe = super().__new__(mcs, name, base, dct)
        # Assim como __new__ em classes, também podemos criar atributos de classe para nossas
        # classes do tipo Meta. Eles estarão disponíveis para nossa classe e suas instâncias.
        classe.attr = 'Valor do nosso atributo'
        # Podemos definir métodos durante a criação da nossa classe, como no exemplo abaixo,
        # onde definimos o método __repr__
        classe.__repr__ = my_repr
        # Outro exemplo de uso para as metaclasses seria a verificação de métodos
        # implementados ou não. Abaixo, verificamos se nosso método exibir está presente no
        # dicionário da classe criada e se ele é chamável. Caso contrário, uma exceção será levantada.
        if 'exibir' not in classe.__dict__ and not callable(classe.__dict__['falar']):
            raise NotImplementedError('Implemente o método falar')
        return classe


# Assim como object, nossa classe também herda a metaclasse type por padrão. Ex.: ClasseQualquer(metaclass=type).
# No caso abaixo estaremos utilizando a metaclasse Meta, criada acima.
class ClasseQualquer(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Criando nossa instância')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, valor):
        self.valor = valor

    # Caso comentarmos o método exibir abaixo, uma exceção seria levantada.
    def exibir(self):
        print('O valor passado para a instância foi:', self.valor)


obj = ClasseQualquer('Valor qualquer')
print(obj.valor)
print(obj.attr, ClasseQualquer.attr)
print(obj)
