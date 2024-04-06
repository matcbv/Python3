def my_repr(teste):
    return f'{type(teste).__name__}, {teste.__dict__}'


class Meta(type):
    def __new__(mcs, name, base, dct):
        print('Criando nossa metaclasse...')
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
        # super() estará se referindo a metaclasse pai de Meta, que é type.
        # Ao chamarmos __call__ de type, estaremos instânciando nossa classe.
        # O método __call__ irá chamar __new__ e __init__, para criar e inicializar nossa classe,
        # encerrando o processo após a execução dos dois métodos.
        instancia = super().__call__(cls)
        return instancia


class ClasseQualquer(metaclass=Meta):
    def __new__(cls, *args, **kwargs):
        print('Iniciado o método __new__ chamados pelo __call__')
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, valor):
        self.valor = valor

    def exibir(self):
        print('O valor passado para a instância foi:', self.valor)


obj = ClasseQualquer('Valor qualquer')
print(obj.valor)
print(obj.attr, ClasseQualquer.attr)
print('Representação da nossa instância:', obj)
