# A associação, é um tipo de relação onde dois objetos são relacionados em um sistema. Dentro da associação,
# ainda temos os subconjuntos de agregação e composição. Ex.:

class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaParaEscrita:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Matheus')
caneta = FerramentaParaEscrita('Caneta tinteiro')
# Conseguimos realizar uma associação ao atribuirmos uma instância caneta, da classe FerramentaParaEscrita,
# com o atributo ferramenta, da classe Escritor. Com isso, podemos acessar os atributos e métodos da classe
# FerramentaParaEscrita, através do atributo ferramenta, da classe Escritor.
escritor.ferramenta = caneta

# Dessa maneira, podemos continuar acessando o método pela instância caneta, e pelo atributo ferramenta.
print(caneta.escrever())
print(escritor.ferramenta.escrever())
