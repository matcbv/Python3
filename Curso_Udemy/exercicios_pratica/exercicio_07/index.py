from functools import reduce

class Client:
    def __init__(self, name, lastname, cpf, address):
        self.name = name
        self.lastname = lastname
        self.cpf = cpf
        self.address = address


def check_cpf(cpf, multiplier=10, i=0):
    result = reduce(lambda acumulator, digit: acumulator + digit, cpf, 0)

    for d in cpf:
        if not d.isdigit():
            return 'CPF inválido!'
        counter += int(d) * multiplier
        multiplier -= multiplier
    new_cpf +=
    i += 1
    if i > 1:
        return
    return check_cpf(cpf + str(counter), multiplier=11)


class Banco:
    def __init__(self, numberAccount, agencyNumber):
        self.numberAccount = numberAccount
        self.agencyNumber = agencyNumber

class Caixa:
    def

class Itau:
    pass

class Bradesco:
    pass