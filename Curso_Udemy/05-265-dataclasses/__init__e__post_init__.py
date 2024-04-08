from dataclasses import dataclass


@dataclass
class ClasseComDataclasses:
    nome: str
    sobrenome: str

    # O método especial __post_init__ é um método acionado após a finalização de __init__.
    def __post_init__(self):
        print('O __init__ acabou, vou dar continuidade agora...')
        self.nome_completo = f'{self.nome} {self.sobrenome}'


pessoa = ClasseComDataclasses('Matheus', 'Cerqueira')
print(pessoa.nome_completo)
print('-' * 30)

# Caso quisermos, podemos definir nosso __init__ normalmente em dataclasses, entretanto,
# não poderemos mais utilizar o __post_init__.
# Ex.:
# Para desativarmos o __init__ automático, ou outros métodos, devemos passar o valor false
# a eles. Isso deve ser informado nos argumentos da chamada do decorador dataclass:
@dataclass(init=False)
class ClasseComInit:
    # Ainda podemos definir a tipagem e/ou valores padrão para nossos atributos for do __init__.
    # Obs.: Fica como opcional definir tais características fora ou no próprio __init__.
    val01: int
    val02: int

    def __init__(self, val01, val02):
        self.val01 = val01
        self.val02 = val02

    def somar(self):
        return self.val01 + self.val02


valores = ClasseComInit(1, 4)
print(valores.somar())
