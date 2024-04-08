from dataclasses import dataclass


@dataclass
class ClasseComDataclasses:
    nome: str
    sobrenome: str

    # Podemos criar métodos normalmente em nossas dataclasses, incluindo getters e setter:
    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


pessoa_01 = ClasseComDataclasses('Matheus', 'Cerqueira')
print(pessoa_01.nome_completo)
pessoa_01.nome_completo = 'Mariana Veiga Tavares'
print(pessoa_01.nome_completo)
