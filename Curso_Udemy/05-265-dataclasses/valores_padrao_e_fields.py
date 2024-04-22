from dataclasses import dataclass, field, fields


@dataclass
class Pessoa:
    # Conseguimos definir valores padrão para nossos atributos, assim como no método __init__:
    nome: str = 'Matheus'
    sobrnome: str = 'Cerqueira'
    idade: int = 0
    # Em dataclasses, não conseguimos criar valores padrão mutáveis. Para isso, utilizamos a
    # função field. Com tal função conseguimos definir as configurações do atributo que
    # estamos criando.
    # Através da propriedade default_factory, conseguimos chamar uma função quando
    # nenhum valor é fornecido à aquele atributo durante a instanciação. No exemplo abaixo
    # estaremos passando a função list, que retornará uma lista vazia, porém, também podemos
    # criar nossa própria função e passá-las como argumento.
    enderecos: int = field(default_factory=list)
    # Também temos as mesmas propriedades que podemos habilitar e desabilitar em nossas
    # dataclasses para aquele atributo em específico, como repr, init, compare, etc.


pessoa_01 = Pessoa()
print(pessoa_01)
# Com a função fields, conseguimos ver todas as configurações aplicadas para aquele atributo
# em específico:
print(fields(pessoa_01))
print(pessoa_01.enderecos)
