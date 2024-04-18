import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime
from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

current_date = str(datetime.now().date())

datas = {'company': 'Cerqueiras Company',
         'name': 'Matheus',
         'date': current_date}

load_dotenv()

# Obtendo os caminhos que utilizaremos:
email_path = Path().absolute() / 'email_model.html'
env_path = Path().absolute().parent / '.env'

# Obtendo o remetente e destinatário:
# Obs.: Neste exemplo, o remetente será o mesmo do destinatário.
remetente = os.getenv('EMAIL')
destinatario = remetente

# Abaixo, iremos obter as configurações do nosso servidor SMTP:
# Nome do servidor:
smtp_server = 'smtp.gmail.com'
# Porta de acesso:
smtp_port = 587
# Usuário:
smtp_user = os.getenv('EMAIL')
# Senha:
smtp_password = os.getenv('EMAIL_PASSWORD')

# Formatando nosso arquivo de email:
with open(email_path, 'r', encoding='utf-8') as email:
    texto_arquivo = email.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(datas)

# Convertendo nosso objeto para ser do tipo MIMEMultipart:
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Email Teste'

# O Sub-tipo também poderia ser plain, caso o arquivo contivesse apenas texto simples.
corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Enviando nosso email através do context generator with:
# Iremos inicializar nosso gerador de contextos através da classe SMTP, passando a ela,
# a servidor SMTP, junto de sua porta de acesso.
with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
    # Iniciando a comunicação com o servidor SMTP:
    server.ehlo()
    # Iniciando a comunicação segura através do protocolo TLS:
    server.starttls()
    # Logando no servidor SMTP:
    server.login(smtp_user, smtp_password)
    # Enviando nossa mensagem:
    server.send_message(mime_multipart)
    print('E-mail enviado com  sucesso!')
