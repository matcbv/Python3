# Com a classe Templates do módulo string, podemos definir variáveis para serem substituídas
# por determinados valores em nossos arquivos.
import locale
import string
from pathlib import Path
from datetime import datetime

locale.setlocale(locale.LC_ALL, '')
path = Path().absolute() / 'banco_de_dados.txt'


def conversion_to_brl(valor):
    valor_brl = locale.currency(val=valor, symbol=True, grouping=True)
    return valor_brl


substitute_dict = dict(
    nome='Matheus',
    valor=conversion_to_brl(1_250),
    telefone=24981002374,
    data=datetime(2024, 4, 17),
    empresa='Cerqueiras')


with open(path, 'r+') as file:
    file_text = ' '.join(file.readlines())
    print(file_text)
    template = string.Template(file_text)
    template.substitute()
