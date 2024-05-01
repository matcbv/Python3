import sys
from pathlib import Path
from datetime import datetime
from abc import ABC, abstractmethod
from contextlib import contextmanager
import string
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import os
from dataclasses import dataclass
from secrets import SystemRandom
from enum import Enum

load_dotenv()
log_template = '$type sent by $user at $date\n'
db_path = Path().absolute() / 'db_logs.txt'
text_template_path = Path().absolute() / 'text_template.html'

# DADOS PARA O SERVIDOR SMTP
server_port = 587
server = 'smtp.gmail.com'


class OpenFileError(Exception):
    ...


class Options(Enum):
    email = 1
    sms = 2


@contextmanager
def log_context_generator(path, open_mode):
    file = None
    try:
        file = open(path, open_mode, encoding='utf-8')
        yield file
    except Exception:
        raise OpenFileError('Um erro ocorreu ao abrir o banco de dados.')
    else:
        print('Log registrado com sucesso.')
    finally:
        file.close()


def get_user_information():
    db_user = os.getenv('EMAIL')
    db_password = os.getenv('EMAIL_PASSWORD')
    user_email = os.getenv('EMAIL')
    return db_user, db_password, user_email


def get_date():
    current_date = datetime.now()
    current_date = current_date.strftime('%d/%m/%y %H:%M:%S')
    return current_date


def verification():
    password = ''.join(SystemRandom().choices(string.ascii_letters + string.digits + string.punctuation, k=8))
    print(password)
    answer = input('Digite a seguir, a senha aleatória apresentada acima: ')
    print('Senha correta!') if password == answer else sys.exit('Senha incorreta! Finalizando processo...')


class Log(ABC):
    def __init__(self):
        self.msg_type = None
        self.username = None
        self.date = get_date()

    @abstractmethod
    def do_log(self): ...


@dataclass
class User:
    user: str = None
    password: str = None
    email: str = None
    phone_number: int = None

    def __post_init__(self):
        self.user, self.password, self.email = get_user_information()


class Email(Log):
    def __init__(self):
        super().__init__()
        self.user = User()

    def do_log(self):
        my_log_template = string.Template(log_template)
        my_log_template = my_log_template.substitute(type='Email', user=self.user.user, date=self.date)
        with log_context_generator(db_path, 'a') as file:
            file.write(my_log_template)

    @staticmethod
    def email_format():
        with open(text_template_path, 'r', encoding='utf-8') as email_file:
            my_email_file = email_file.read()

        my_email_template = string.Template(my_email_file)
        my_email_template = my_email_template.substitute(addressee='Douglas', remitter='Matheus')
        return my_email_template

    def _get_email(self):
        mime = MIMEMultipart()
        mime['To'] = self.user.email
        mime['From'] = self.user.email
        mime['Subject'] = 'Documentação'

        msg_body = MIMEText(_text=self.email_format(), _subtype='html', _charset='utf-8')
        mime.attach(msg_body)
        return mime

    def send_email(self):
        verification()
        try:
            with SMTP(server, server_port, timeout=15) as smtp:
                SMTP.starttls(smtp)
                SMTP.ehlo(smtp)
                SMTP.login(smtp, self.user.user, self.user.password)
                SMTP.send_message(smtp, self._get_email())
                SMTP.close(smtp)
        except Exception:
            raise OpenFileError('Não foi possível realizar o envio do email. Tente novamente.')
        else:
            print('Email enviado com sucesso!')
            self.do_log()


class SMS(Log):
    def __init__(self):
        super().__init__()
        self.user = User()

    def do_log(self):
        my_log_template = string.Template(log_template)
        my_log_template = my_log_template.substitute(type='SMS', user=self.user.phone_number, date=self.date)
        with log_context_generator(db_path, 'a') as file:
            file.write(my_log_template)

    def send_sms(self):
        verification()
        if 10 < len(str(self.user.phone_number)) <= 12:
            sms_msg = input('Informe a seguir, a mensagem de texto a ser enviada: ')
            print('Notificação enviada!')
        else:
            print('Número inválido! Tente novamente mais tarde')


answer_ = int(input('Deseja enviar a mensagem via Email [1] ou SMS [2]? '))

if answer_ == Options.email.value:
    email = Email()
    email.send_email()
elif answer_ == Options.sms.value:
    sms = SMS()
    phone_number = int(input('Informe seu número de contato: '))
    while not isinstance(phone_number, int):
        print('Número inválido!')
        phone_number = int(input('Informe seu número de contato: '))
    sms.user.phone_number = phone_number
    sms.send_sms()
else:
    print('Opção inválida!')
