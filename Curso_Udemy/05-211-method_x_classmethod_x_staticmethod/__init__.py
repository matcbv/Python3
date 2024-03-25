class GeradorDeLogin:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def get_auth(cls, user, password):
        login = cls()
        login.user = user
        login.password = password
        return login

    @staticmethod
    def log():
        print('Um novo login foi gerado.')


# No exemplo abaixo, estaremos criando uma instância e atribuindo valores a ela por meio de métodos
# de instância:
novo_login = GeradorDeLogin()
novo_login.set_user('matheus')
novo_login.set_password('12345')

# Já agora, utilizaremos um método de classe, que terá o mesmo resultado:
gerador_de_login = GeradorDeLogin.get_auth('matcbv', '123321')

print(novo_login.user, novo_login.password)
print(gerador_de_login.user, gerador_de_login.password)
