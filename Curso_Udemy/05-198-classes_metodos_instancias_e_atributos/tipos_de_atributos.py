# Como vimos anteriormente, podemos criar atributos para nossas instâncias, contendo valores quaisquer.
# Esses são chamados de atributos de instância, porém também podemos criar atributos de classe, sendo globais dentro da
# classe que estamos lidando.
class Classe:
    # Atributo de classe
    atb_classe = 'valor global'

    def __init__(self, valor, valor_02):
        # Atributos de instância
        self.atb_instancia = valor
        # Note que também podemos criar um atributo de instância com mesmo nome que nosso atributo global.
        self.atb_classe = valor_02

    def executar(self):
        # Podemos chamar nosso atributo global através do self ou do nome de nossa classe. Entretanto, caso tenhamos
        # um atributo de instância de mesmo nome, como é esse o caso, caso utilizarmos o self, ele sempre irá
        # preferenciar o atributo de instância.
        print(self.atb_classe)
        # Ao especificarmos nossa classe, ele mostra o resultado do atributo global. Lembrando que caso o atributo de
        # instância de mesmo nome não existisse, a chamada self.atb_classe faria referência ao atributo da classe, já
        # que as instâncias também tem acesso aos atributos de classe.
        print(Classe.atb_classe)


obj = Classe('teste', 'teste_02')
obj.executar()
