from pathlib import Path
from datetime import datetime
from abc import ABC, abstractmethod
from contextlib import contextmanager
import json
import string
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
import os
from dataclasses import dataclass
import secrets

load_dotenv()

server_user = 'admin'
server_password = None
server = 'smtp.gmail.com'
server_port = 587
log_template = '$type sent by $user at $date'
email_ = 'matheuscbv2334@gmail.com'


def get_user_information():
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    return db_user, db_password


def get_date():
    current_date = datetime.now()
    current_date = current_date.strftime('%d/%m/%y %H:%M:%S')
    return current_date


class Log(ABC):
    def __init__(self):
        self.msg_type = None
        self.user = None
        self.date = get_date()

    @abstractmethod
    def get_log(self): ...


@dataclass
class User:
    user: str = None
    password: str = None

    def __post_init__(self):
        self.user, self.password = get_user_information()


class Email(Log):

    def get_log(self):
        my_template = string.Template(log_template)
        my_template = my_template.substitute(type='Email', user=self.user, date=self.date)
        return my_template

    @staticmethod
    def get_email():
        mime = MIMEMultipart()
        mime['To'] = email_
        mime['From'] = email_
        mime['Subject'] = 'Documentação'

        msg_body = MIMEText(log_template)
        mime.attach(msg_body)
        return mime

    def send_email(self, my_email):
        with SMTP(server, server_port) as email:
            SMTP.starttls(email)
            SMTP.ehlo(email)
            SMTP.send_message(email, msg=my_email, from_addr=email_, to_addrs=email_)
            SMTP.close(email)
