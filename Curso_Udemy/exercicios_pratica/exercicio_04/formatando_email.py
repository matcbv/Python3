from pathlib import Path
from datetime import datetime
from string import Template
from smtplib import SMTP
import os

file_path = Path(__file__).parent / 'text_template.txt'
email_file = Path(__file__).parent / 'email_template.html'
env_path = Path().absolute().parent.parent / '.env'

smtp_server = 'smtp.gmail.com'
smtp_port = 587

name = input('Seu nome:')
client = input('Nome do destinatário:')

template = Template(str(file_path))
template.substitute(name=name, client=client)

for file, env_path.walk()

with SMTP(smtp_server, smtp_port) as email:
    email.ehlo()
    email.starttls()
