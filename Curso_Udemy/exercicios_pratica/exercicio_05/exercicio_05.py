from abc import abstractmethod
from datetime import datetime
import calendar
from pathlib import Path
from string import Template
from enum import Enum
from dataclasses import dataclass
from itertools import count, groupby
from functools import reduce, partial
import zipfile
from contextlib import contextmanager
from copy import deepcopy

banco_de_dados = Path().absolute() / 'banco_de_dados_bissextos.txt'


def verifica_resp(resp):
    if resp not in 'sn':
        print('Resposta inválida!')
        verifica_resp(input('Deseja obter a data atual? [S/N] ').lower()[0])
    if resp == 's':
        return True
    return False


def e_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            return False
        return True
    return False


class AnoBissexto(type):
    def __new__(cls, *args, **kwargs):
        cls = super().__new__(cls, *args, **kwargs)
        return cls

    def __call__(cls, *args, **kwargs):
        instancia = super().__call__(*args, **kwargs)
        if e_bissexto(instancia.ano):
            instancia.bissexto = True
            instancia.dias = 366
        for a in range(instancia.ano + 1):
            if e_bissexto(a):
                instancia.lista_anos_bissextos.append(f'\n{a}')
        return instancia


class Ano(metaclass=AnoBissexto):
    def __init__(self, ano):
        self.ano = ano
        self.bissexto = False
        self.dias = 365
        self.lista_anos_bissextos = []

    def obter_calendario_ano(self):
        cal_ano = calendar.calendar(self.ano)
        return cal_ano

    def obter_calendario_mes(self, mes):
        cal_mes = calendar.monthcalendar(self.ano, mes)
        return cal_mes

    def obter_dia_bissexto(self):
        if self.bissexto:
            dia_semana = calendar.day_name[calendar.weekday(self.ano, 2, 29)]
            return dia_semana
        print('O ano não é bissexto.')


@contextmanager
def gerador_de_contexto(path):
    try:
        arq_ = open(path, 'w', encoding='utf-8')
        yield arq_
    except FileNotFoundError:
        print('Verifique se o arquivo foi criado corretamente')
        print(FileExistsError.__name__, FileNotFoundError.__cause__)
    except FileExistsError:
        return True
    else:
        print('Arquivo aberto com sucesso!')


resp_ = verifica_resp(input('Deseja obter a data atual? [S/N] ').lower()[0])
if resp_:
    print(datetime.today().date())
    print()

obj_ano = Ano(2024)

with gerador_de_contexto(banco_de_dados) as arq:
    arq.writelines(obj_ano.lista_anos_bissextos)
