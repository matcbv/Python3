import sys
from abc import ABC, abstractmethod
from contextlib import contextmanager
from functools import reduce, partial
from itertools import groupby, count
from enum import Enum
from dataclasses import dataclass
from pathlib import Path
from os import path
from datetime import datetime
from calendar import Calendar
from time import sleep


class Opcoes(Enum):
    opc01: str = 'Email'
    opc02: str = 'SMS'
    opc03: str = 'Ligação'


contador = count()
caminho = Path().absolute() / 'banco_de_dados'

@contextmanager
def gerador_de_contexto(modo_abertura):
    print('Abrindo arquivo...')
    sleep(2)
    try:
        arquivo = open(caminho, modo_abertura)
        yield arquivo
    except FileNotFoundError:
        print('Arquivo não encontrado! Tente criá-lo novamente.')
    else:
        print('Fechando arquivo...')
        arquivo.close()


def gerar_arquivo(nome_arquivo: str):
    nome_dir = Path().absolute() / nome_arquivo
    nome_dir.touch(exist_ok=True)
    print('Arquivo gerado!')
    return nome_dir


def obter_horario():
    hora = datetime.today()
    hora_formatada = datetime.strftime(hora, '%d-%m-%Y %h:%m:%s')
    return f'Adicionado em {hora_formatada}'


class ClasseQueGrava:
    def __init__(self, msg):
        self.msg = msg
        self.caminho = caminho

    @abstractmethod
    def gravar_msg(self): ...


class Email(ClasseQueGrava):
    def __init__(self, msg: str, assunto: str, remetente: str, destinatario: str):
        super().__init__(msg)
        self.assunto = assunto
        self.remetente = remetente
        self.destinatario = destinatario

    def gravar_msg(self):
        hora = obter_horario()
        with gerador_de_contexto('a') as arquivo:
            arquivo.write(f'{self.msg} - {hora}')


class SMS(ClasseQueGrava):
    def __init__(self, msg: str, numero: int):
        super().__init__(msg)
        self.numero = numero

    def gravar_msg(self):
        hora = obter_horario()
        with gerador_de_contexto('a') as arquivo:
            arquivo.write(f'SMS - {self.numero} - {self.msg} - {hora}\n')


class Ligacao(ClasseQueGrava):
    def __init__(self, numero: int, msg: str = ''):
        super().__init__(msg)
        self.numero = numero

    def gravar_msg(self):
        hora = obter_horario()
        with gerador_de_contexto('a') as arquivo:
            arquivo.write(f'Ligação - {self.numero} - {hora}\n')


enviar_msg = input('Deseja enviar uma mensagem? ').lower()[0]
if enviar_msg == 'n':
    sys.exit()
print(f'1 - {Opcoes.opc01.value}\n'
      f'2 - {Opcoes.opc02.value}\n'
      f'3 - {Opcoes.opc03.value}\n')
tipo_msg = input('Escolha uma das opções acima: ')

match tipo_msg:
    case 1:
        remetente_ = input('Qual o seu email? ')
        destinatario_ = input('Qual o email do destinatário? ')
        assunto_ = input('Qual o assunto do email? ')
        msg_ = input('Mensagem do email: ')
        ligar = Email(msg_, assunto_, remetente_, destinatario_)
    case 2:
        numero_ = int(input('Para qual número deseja ligar? '))
        msg_ = input('Mensagem do SMS: ')
        ligar = SMS(msg_, numero_)
    case 3:
        numero_ = int(input('Para qual número deseja ligar? '))
        ligar = Ligacao(numero_)
