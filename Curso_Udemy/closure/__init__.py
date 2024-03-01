# Um closure é uma função, contida dentro de outra função, armazenada em um objeto chamável.
# Esse objeto, quando chamado em forma de função, irá retornar o resultado da função armazenada,
# mantendo as variáveis que recebeu da função pai 'vivas'.

def chamadaFila(id, nome):
    def chamar():
        return f'Paciente {nome} de código {id}, favor comparecer ao consultório.'
    return chamar


# Ao armazenarmos nossa função chamar() nos objetos paciente01 e paciente 02, ela será gravada
# na memória RAM da máquina, contendo as informações passadas por parâmetro abaixo. Dessa forma,
# podemos executá-la quando bem entendermos.
paciente01 = chamadaFila(1, 'Daniel')
paciente02 = chamadaFila(2, 'Matheus')
# Executando a função chamar() com os valores acima:
print(paciente01())
print(paciente02())

# Obs.: Podemos inclusive adiar o recebimento de um dos parâmetros:


def bom_dia(nome):
    def saudacao(hora):
        return f'Bom dia, {nome}! São {hora} no momento.'
    return saudacao


h1 = bom_dia('Matheus')
print(h1('8:30h'))
