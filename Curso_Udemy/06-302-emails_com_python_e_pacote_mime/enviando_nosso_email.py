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

# Criando nosso objeto do tipo MIMEMultipart:
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Email Teste'

# Criando e adicionado texto em nosso email:
corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

# Com o construtor with, estaremos criando um contexto de gerenciamento de recursos para o objeto smtplib.SMTP
# Junto a instância da nossa classe SMTP, devemos passar o servidor SMTP, junto de sua porta de acesso.
# O construtor with é recomendado sempre ao trabalharmos com abertura e fechamento de arquivos e
# protocolos de rede e banco de dados, pois ele garante um encerramento correto de todas as operações.
# O parâmetro timeout determina quanto tempo o cliente SMTP aguardará para se conectar ao servidor SMTP
# antes de desistir e lançar uma exceção de timeout.
with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
    # Iniciando a comunicação segura através do protocolo TLS:
    server.starttls()
    # Iniciando a comunicação com o servidor SMTP:
    server.ehlo()
    # Logando no servidor SMTP:
    server.login(smtp_user, smtp_password)
    # Enviando nossa mensagem:
    server.send_message(mime_multipart)
    print('E-mail enviado com  sucesso!')
