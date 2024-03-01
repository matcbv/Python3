# Na composição, a relação entre as classes é ainda mais forte do que na agregação,
# onde uma classe é composta por uma ou mais instâncias de outras classes,
# e essas instâncias são geralmente criadas e gerenciadas internamente pela classe dominante.
# A composição implica uma relação de todo-parte
# aonde as partes não existem independentemente do todo.
class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def apresentar(self):
        print(f"Nome: {self.nome}, Cargo: {self.cargo}")


class Empresa:
    def __init__(self, nome, funcionarios=None):
        self.nome = nome
        if funcionarios is None:
            self.funcionarios = []
        else:
            self.funcionarios = funcionarios

    def contratar(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"Funcionários da empresa {self.nome}:")
        for funcionario in self.funcionarios:
            funcionario.apresentar()


# Criando alguns funcionários
funcionario1 = Funcionario("João", "Desenvolvedor")
funcionario2 = Funcionario("Maria", "Designer")
funcionario3 = Funcionario("Pedro", "Analista")

# Criando uma empresa e contratando funcionários
empresa = Empresa("Minha Empresa")
empresa.contratar(funcionario1)
empresa.contratar(funcionario2)
empresa.contratar(funcionario3)

# Listando os funcionários da empresa
empresa.listar_funcionarios()

# Neste exemplo, a classe Empresa é composta por uma lista de funcionários.
# A existência dos funcionários está diretamente ligada à existência da empresa.
# Se a empresa deixar de existir, os funcionários associados a ela também deixarão de existir.
# Isso demonstra a composição de classes, onde uma classe é composta por instâncias de outras classes,
# e a existência das instâncias compostas está intrinsecamente ligada à existência da classe dominante.
