# Na herança de classes, uma 05-198-classes_metodos_instancias_e_atributos herda todos os métodos e atributos da
# outra. A 05-198-classes_metodos_instancias_e_atributos herdeira é chamada de subclasse, enquanto a que fornece os
# métodos e atributos é chamada de superclasse. É importante frisar que as subclasses podem possuir métodos e
# atributos próprios. A superclasse será a 05-198-classes_metodos_instancias_e_atributos que possuir os objetos mais
# generalizados, e nunca irá herdar nada das subclasses, somente prover.


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def caminhar(self):
        print(f'{self.nome} está caminhando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'O aluno {self.nome} está estudando...')


class Empregado(Pessoa):
    def trabalhar(self):
        print(f'O empregado {self.nome} está trabalhando...')


estudante = Aluno('Matheus', 21)
estudante.caminhar()
estudante.estudar()
print('-'*40)
trabalhador = Empregado('Lucas', 18)
trabalhador.caminhar()
trabalhador.trabalhar()

# No exemplo acima, percebemos que a 05-198-classes_metodos_instancias_e_atributos ‘Aluno’ e ‘Empregado’
# herdam os métodos e atributos da 05-198-classes_metodos_instancias_e_atributos ‘Pessoa’,
# porém ainda possuem seus próprios métodos (‘estudar’ e ‘trabalhar’).
