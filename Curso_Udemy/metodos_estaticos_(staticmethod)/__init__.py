# Métodos estáticos são métodos contidos dentro de classes, mas que não tem acesso direto nem as
# instâncias e nem a própria classe. Ou seja, não faz referências aos parâmetros self e cls.
class ClasseComMetodoEstatico:
    @staticmethod
    def metodo_estatico():
        print('Sou um método estático!')


# Podemos chamar nossos métodos estáticos através das instâncias ou da própria classe:
instancia = ClasseComMetodoEstatico()
instancia.metodo_estatico()
ClasseComMetodoEstatico.metodo_estatico()
