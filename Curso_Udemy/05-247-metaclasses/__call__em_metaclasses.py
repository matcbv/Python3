def my_repr(teste):
    print(type(teste))
    return f'{type(teste).__name__}, {teste.__dict__}'


class Meta(type):
    def __new__(mcs, name, base, dct):
        print('Criando nossa metaclasse')
        classe = super().__new__(mcs, name, base, dct)
        classe.attr = 'Valor do nosso atributo'
        classe.__repr__ = my_repr
        if 'exibir' not in classe.__dict__ and not callable(classe.__dict__['falar']):
            raise NotImplementedError('Implemente o método falar')
        return classe

    # Quando chamamos __call__ em metaclasses, estamos tratando dos argumentos de nossa classe
    # durante sua chamada, criando nossas instâncias e retornando-as. Ex.: instancia = ClasseQualquer('valor').
    def __call__(cls, *args, **kwargs):
        print('Criando nossa instância...')
        instancia = object.__call__(cls)
        return instancia


class ClasseQualquer(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Criando nossa instância')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, valor):
        self.valor = valor

    def exibir(self):
        print('O valor passado para a instância foi:', self.valor)


obj = ClasseQualquer('Valor qualquer')
print(obj.valor)
print(obj.attr, ClasseQualquer.attr)
print(obj)
