from pathlib import Path
from datetime import datetime
from abc import ABC, abstractmethod
from contextlib import contextmanager
import json
from string import Template
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

load_dotenv()

log_template = '$user logged at system $time'


def get_user_information():
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    return db_user, db_password


def get_date():
    current_date = datetime.now()
    current_date = current_date.strftime('%d/%m/%y %H:%M:%S')
    return current_date


class User:
    def __init__(self, user, password):
        self.user = password
        self.password = password


class Email:
    def send_log(self):
        pass
