class CallMe:
    def __init__(self, phone_number):
        self.phone_number = phone_number

    # Podemos fazer com que instâncias de nossa classe sejam chamáveis através do método especial
    # __call__. Através da função criada por ele, podemos realizar diversas ações, como receber
    # vários argumentos, retornar um objeto e modificar o próprio valor do atributo da nossa instância.
    def __call__(self, *args, **kwargs):
        print(f'Agora a instância é chamável.')
        valor = args[0]
        print(valor)
        self.phone_number = next(iter(kwargs.values()))
        print(self.phone_number)
        return


call = CallMe(24981002374)
call('valor qualquer', novo_numero=24980014732)
