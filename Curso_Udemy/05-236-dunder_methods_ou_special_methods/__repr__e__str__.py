class Coordenadas:
    def __init__(self, x, y, z='Referência'):
        self.x = x
        self.y = y
        self.z = z

    # Com o método especial __repr__, definimos a representação de nossos objetos. Com ele, informamos a
    # estrutura de nosso objeto, como uma forma de documentação para quando for exibido. Esse método é
    # muito utilizado para auxiliar outros desenvolvedores ao trabalharem com o código.
    def __repr__(self):
        class_name = self.__class__.__name__
        # É aconselhado utilizarmos f strings com a especificação para o tipo __repr__.
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'
        # Como podemos ver, notamos diferença no parâmetro z. Como ele é do tipo string, aspas foram
        # adicionadas em sua formatação.

    # Com o método especial __str__, definiremos o que será retornado quando nosso objeto for requisitado
    # em formato de string. Por padrão, o método __str__ é utilizado sempre que definido. Caso contrário, é feito um
    # fallback, direcionando a execução para o método __repr__, caso tenha sido definido.
    # Obs.: fallback é uma abordagem proativa para lidar com possíveis falhas ou problemas, garantindo que haja uma
    # solução alternativa ou plano de contingência disponível.
    def __str__(self):
        return f'(x={self.x}, y={self.y})'


coordenada_01 = Coordenadas(123, 321)
print(coordenada_01)
# Mesmo com um método __str__ definido, ainda conseguimos chamar nosso método __repr__:
# Primeira opção:
print(repr(coordenada_01))
# Segunda opção:
print(f'{coordenada_01!r}')
# No caso acima, !s significa __string__ e !r __repr__.
