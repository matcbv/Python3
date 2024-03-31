# Utilizaremos ad classe do tópico 05-225 para darmos continuidade neste tópico.
# Para definirmos nossa classe como abstrata, precisamos importar a classe ABC do módulo abc.
from abc import ABC, abstractmethod


# Nossa classe Log irá herdar a classe ABC:
class Log(ABC):
    # Para transformarmos nosso método Log em abstrato, devemos utilizar o decorador @abstractmethod.
    @abstractmethod
    # Iremos eliminar seu corpo, mantendo somente sua assinatura.
    def _log(self, msg): ...  # Obs.: As reticências substituem a palavra-chave pass.

    def log_error(self, msg=None):
        print('-' * 60)
        print(f'O self é: {self}, da classe {self.__class__.__name__}')
        print(f'Erro! {msg}')

    def log_success(self, msg=None):
        print('-' * 60)
        print(f'O self é: {self}, da classe {self.__class__.__name__}')
        print(f'Sucesso! {msg}')


class LogPrintMixin(Log):
    # Quando uma subclasse herda de uma classe abstrata, ele é obrigada a implementar todos os métodos
    # abstratos contidos em tal classe, adicionando corpo a eles.
    def _log(self, msg):
        print('-'*60)
        print(f'O self é: {self}, da classe {self.__class__.__name__}')
        print(msg)

# Agora, caso tentarmos utilizar _log diretamente da classe Log, teremos um erro, conseguindo
# utilizá-la somente nas subclasses que o implementaram (nesse exemplo, a LogPrintMixin).
