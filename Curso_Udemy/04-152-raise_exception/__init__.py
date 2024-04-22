# Através da palavra-chave raise, conseguimos lançar uma exceção a qualquer momento em nosso código,
# passando também uma mensagem personalizada para esse erro. Ex.:
# raise ValueError('Valor não aceito!')

# Podemos retornar exceções por meio de funções também:
def diferente_de_zero(n):
    if n == 0:
        raise ZeroDivisionError('Não é possível dividir um valor por zero.')
    # Caso a exceção não seja acionada, um boolean True será retornado.
    # Em certos casos é bom retornar algo por questão de didática, mesmo não sendo necessário.
    return True


def int_ou_float(*args):
    lista_numerica = [*args]
    for n in lista_numerica:
        if not isinstance(n, (int, float)):
            raise TypeError(f'Os valores devem ser numéricos. Você passou um valor do tipo "{type(n)}"')


def dividir(n, d):
    int_ou_float(n, d)
    diferente_de_zero(d)
    return n/d


result = dividir(10, 0)
print(f'O resultado da divisão entre {10} e {0} é: {result}')

# Esse foi um exemplo de utilização de raise exception.
