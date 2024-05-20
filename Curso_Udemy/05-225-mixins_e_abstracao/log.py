# Abstração é o ato de tornarmos uma classe e seus elementos abstratos, ou seja, criamos
# uma classe "genérica" que pode ser implementada por outras classes e ter seus métodos reutilizados,
# permitindo diferentes comportamentos em cada uma das subclasses. Nesse caso, estamos abstraindo
# a superclasse Log, tornando-a acessível por meio das subclasses LogFileMixin e LogPrintMixin.

path = "/05-225-mixins_e_abstracao/text_model.txt"


class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método logs.txt')

    def log_error(self, msg=None):
        print('-' * 60)
        print(f'O self é: {self}, da classe {self.__class__.__name__}')
        print(f'Erro! {msg}')

    def log_success(self, msg=None):
        print('-'*60)
        print(f'O self é: {self}, da classe {self.__class__.__name__}')
        print(f'Sucesso! {msg}')


# --------- * IMPORTANTE * ---------
# Criando as classes LogError e LogSuccess, definimos diferentes comportamentos
# para o método _log da superclasse Log. Para termos este comportamento, a assinatura
# do método deve ser a mesma para todas as chamadas. A assinatura do método consiste
# em seu nome e parâmetro(s). Diferente da assinatura, podemos alterar o corpo do método
# da maneira que nos for conveniente.

# Um mixin é uma classe responsável por oferecer funcionalidades adicionais de forma modular
# a outras classes. Essas funcionalidades serão reutilizadas por outras classes por meio de herança múltipla.
# Nesse caso, utilizamos uma combinação entre classe abstrata e mixin, onde as classes mixin
# LogFileMixin e LogPrintMixin herdaram a classe Log, modificando o método _log. Essas classes
# poderão ser herdadas por outras classes para terem seus métodos e o métodos da classe Log reutilizados.
class LogFileMixin(Log):
    def _log(self, msg):
        try:
            with open(path, 'a', encoding='utf-8') as arquivo:
                arquivo.write(msg)
                arquivo.write('\n')
        except FileNotFoundError:
            self.log_error('Arquivo não encontrado!')
            print()
        else:
            self.log_success(msg)


class LogPrintMixin(Log):
    def _log(self, msg):
        print('-'*60)
        print(f'O self é: {self}, da classe {self.__class__.__name__}')
        print(msg)
