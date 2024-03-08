def soma(x):
    def recebe_y(y):
        return x + y
    return recebe_y


def multiplica(x):
    def recebe_y(y):
        return x * y
    return recebe_y


def executa_funcao(funcao):
    if funcao == m:
        return funcao(int(input('Escolhe um valor para ser multiplicado: ')))
    else:
        return funcao(int(input('Escolhe um valor para ser somado: ')))


m = multiplica(5)
s = soma(10)

print(executa_funcao(s))
print(executa_funcao(m))
