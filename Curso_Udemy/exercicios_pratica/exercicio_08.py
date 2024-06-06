class MainClass:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return f'{self.name!s} {self.lastname!s}'

    def __repr__(self):
        return f'{self.name!r} {self.lastname!r}'


obj = MainClass('Matheus', 'Cerqueira')
print(obj.__str__())
print(obj.__repr__())


class SecClass:
    def __init__(self, job):
        self.job = job
        self.person = MainClass('Lucas', 'Silva')


class ThirdClass:
    def __init__(self):
        self.