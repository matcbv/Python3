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


@contextmanager
def gerador_de_contexto(caminho, modo_abertura):
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
    def __init__(self, msg, nome_arquivo):
        self.msg = msg
        self.nome_arquivo = nome_arquivo

    @abstractmethod
    def gravar_msg(self): ...


class Email(ClasseQueGrava):
    def __init__(self, msg: str, caminho: str, assunto: str, remetente: str, destinatario: str):
        super().__init__(msg, caminho)
        self.assunto = assunto
        self.remetente = remetente
        self.destinatario = destinatario

    def gravar_msg(self):
        caminho_arquivo = gerar_arquivo(self.nome_arquivo)
        hora = obter_horario()
        with gerador_de_contexto(caminho_arquivo, 'a') as arquivo:
            arquivo.write(f'{self.msg} - {hora}')


class SMS(ClasseQueGrava):
    def __init__(self, msg: str, caminho: str, numero: int):
        super().__init__(msg, caminho)
        self.numero = numero

    def gravar_msg(self):
        caminho_arquivo = gerar_arquivo(self.nome_arquivo)
        hora = obter_horario()
        with gerador_de_contexto(caminho_arquivo, 'a') as arquivo:
            arquivo.write(f'{self.numero} - {self.msg} - {hora}')


class Ligacao(ClasseQueGrava):
    def __init__(self, msg: str, caminho: str, numero: int):
        super().__init__(msg, caminho)
        self.numero = numero

    def gravar_msg(self):
        caminho_arquivo = gerar_arquivo(self.nome_arquivo)
        hora = obter_horario()
        with gerador_de_contexto(caminho_arquivo, 'a') as arquivo:
            arquivo.write(f'{self.numero} - {self.msg} - {hora}')

