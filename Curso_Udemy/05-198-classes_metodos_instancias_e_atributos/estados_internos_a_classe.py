# Quando trabalhamos com classes, podemos manter o estado de um determinado atributo durante a execução de nosso
# programa. Veja um exemplo a seguir:

class Estado:
    def __init__(self, v_ou_f=False):
        self.v_ou_f = v_ou_f


mudando_estado = Estado()
print(mudando_estado.v_ou_f)
if not mudando_estado.v_ou_f:
    mudando_estado.v_ou_f = True
print(mudando_estado.v_ou_f)

# Dessa forma, conseguimos manter o estado de nossos atributos ao longo da execução de nosso código.
