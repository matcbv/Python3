from log import LogPrintMixin, LogFileMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False


# --------- * IMPORTANTE * ---------
# Sempre dê preferência a utilizar composição à herança. Utilizaremos herança em nosso exemplo
# para estarmos demonstrando o funcionamento das dinâmicas desse tópico.
# A classe Smartphone irá herdar todos os métodos e atributos da classe Eletronico e LogPrintMixin.
class Smartphone(Eletronico, LogPrintMixin):
    # Como importamos a classe LogPrintMixin (ou LogFileMixin, caso quisermos), os métodos _log,
    # log_error e log_success estarão disponíveis para a classe Smartphone, já que foram herdados
    # pelas classes LogPrintMixin e LogFileMixin da classe abstrata Log.
    def ligar(self):
        if self._ligado:
            msg = f'{self._nome} já está ligado.'
            self.log_error(msg)
        else:
            msg = f'{self._nome} ligou!'
            self.log_success(msg)
            super().ligar()

    def desligar(self):
        if not self._ligado:
            msg = f'{self._nome} já está desligado.'
            self.log_error(msg)
        else:
            msg = f'{self._nome} desligou!'
            self.log_success(msg)
            super().desligar()

    def escrever_na_tela(self):
        # Aqui chamamos o método _log, passando uma mensagem para ser exibida na tela.
        msg = f'{self._nome} está escrevendo na tela...'
        self._log(msg)
