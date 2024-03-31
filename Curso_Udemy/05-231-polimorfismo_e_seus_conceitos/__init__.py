# Neste exemplo, colocaremos em prática o polimorfismo.
from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, msg):
        self.mensagem = msg

    # Através do ícone ->, indicamos ao desenvolvedor e ao Python, que o tipo esperado de retorno
    # seja do tipo boolean. O Python em si não realizada nenhuma ação com tal informação, sendo
    # algo principalmente didático.
    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail:', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS:', self.mensagem)
        return True


# Através do símbolo :, conseguimos indicar ao Python o tipo que nosso parâmetro deveria ser,
# por mais que caso passemos elementos de outros tipos, não gerará nenhum erro.
# O polimorfismo em nosso código se encontra no parâmetro notificacao, através da função notificar.
def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    # Nesta verificação, caso o valor retornado pelos métodos fosse diferente de um boolean,
    # acabaria ocasionando um mau funcionamento em nossa aplicação. Por isso a importância de
    # sempre retornar valores de mesmo tipo.
    if notificacao_enviada:
        return print('Notificação enviada!')
    return print('Notificação NÂO enviada!')


# Como podemos ver abaixo, nossa aplicação funcionou de maneira adequada, independente da subclasse
# utilizada. Isso se enquadra corretamente no Princípio da Substituição de Liskov.
mensagem_01 = NotificacaoSMS('Uma mensagem qualquer...')
notificar(mensagem_01)
mensagem_02 = NotificacaoEmail('Uma mensagem qualquer...')
notificar(mensagem_02)
