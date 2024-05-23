import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from pathlib import Path
from dotenv import load_dotenv
from string import Template

load_dotenv()

# ENV DATA
env = {'main_email': os.getenv('EMAIL'), 'main_email_password': os.getenv('EMAIL_PASSWORD')}

# EMAIL SERVER DATA:
esd = {'server': 'smtp.gmail.com', 'port': 587}

# EMAIL TEMPLATE PATH
email_template = Path().absolute() / "/public/email_template.html"


class Email:
    def __int__(self, client_name, client_lastname, email, password, subject, message):
        self.client_name = client_name
        self.client_lastname = client_lastname
        self.email = email
        self.password = password
        self.subject = subject
        self.message = message

    def create_mime(self):
        mime = MIMEMultipart()
        mime['From'] = env['main_email_password']
        mime['To'] = self.email
        mime['Subject'] = self.subject
        mime.attach(self.get_email_body())
        return mime

    def get_email_body(self):
        email_html = Template(str(email_template))
        email_html.substitute(addressee=self.client_name + self.client_lastname,
                              content=self.message, remitter='M&M Bank')
        email_body = MIMEText(str(email_html), _subtype='html', _charset='utf-8')
        return email_body

    def send_email(self):
        with SMTP(self.email, esd['port'], timeout=15) as email:
            email.ehlo()
            email.starttls()
            email.login(env['main_email'], env['main_email_password'])
            email.send_message(self.create_mime())
            email.close()
