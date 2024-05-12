import json
import random
from contextlib import contextmanager
from pathlib import Path
import string
import os
from dotenv import load_dotenv
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

load_dotenv()

# CAMINHO PARA O BANCO DE DADOS
db_path = Path().absolute() / 'clients_data.json'

# CAMINHO PARA A TEMPLATE DO EMAIL
email_template = Path().absolute() / 'email_template.html'

# VARIÁVEIS DE AMBIENTE
main_email_password = os.getenv('EMAIL_PASSWORD')
main_email = os.getenv('EMAIL')
host_name = 'localhost'


# DADOS DO SERVIDOR DE EMAIL
server_domain = 'smtp.gmail.com'
server_port = 587

@contextmanager
def my_context_generator(path, opening_mode):
    file = None
    try:
        file = open(path, opening_mode, encoding='utf-8')
        yield file
    except Exception as e:
        print(e)
    finally:
        file.close() if file else None


def get_next_id():
    with my_context_generator(db_path, 'r') as db:
        data = json.load(db)
        return str(len(data))


def import_data():
    with my_context_generator(db_path, 'r') as db:
        data = json.load(db)
    return data


class Client:
    def __init__(self, name, lastname, age, username, email):
        self._id = get_next_id()
        self._name = name
        self._lastname = lastname
        self._username = username
        self._age = age
        self._email = email
        self.__password = self.__get_password()
        self.client_keys = ['name', 'lastname', 'age', 'username', 'password']

    @staticmethod
    def __get_password():
        password = ''.join(random.SystemRandom().choices(''.join([string.digits, string.ascii_letters]), k=8))
        return password

    def add_new_client(self):
        if Path.exists(db_path):
            data = import_data()
            username_array = []
            for client in data.values():
                username_array.append(client['username'])
            username = self._username
            if username in username_array:
                return print('\033[92mCliente já cadastrado!\033[0m')
            client_data = {
                'name': self._name,
                'lastname': self._lastname,
                'age': self._age,
                'username': self._username,
                'email': self._email,
                'password': self.__password
            }
            data[self._id] = client_data
            with my_context_generator(db_path, 'w') as db:
                json.dump(data, db, indent=True, ensure_ascii=False, )
        else:
            print('\033[91mUm erro inesperado ocorreu!\033[0m\n'
                  '\033[92mPossível solução\033[0m: Verifique o caminho para o banco de dados.')

    @property
    def client_data(self):
        data = import_data()
        return data[self._id]

    @client_data.setter
    def client_data(self, value):
        data = import_data()
        [key, value] = self.get_data_info()
        if key and value:
            data[self._id][key] = value
        with my_context_generator(db_path, 'w') as db:
            json.dump(data, db, indent=True, ensure_ascii=False, )

    def get_data_info(self):
        key = input('De qual chave deseja alterar o valor: ').lower()
        value = None
        if key not in self.client_keys:
            raise KeyError('Chave inválida! Tente novamente.')
        if key == 'age':
            value = int(input('Qual será o novo valor? ').lower())
        elif key == 'password':
            self.send_verification_email()
            code = input('Informe o código obtido através do email: ')
            if code == self.__password:
                new_password = input('Informe sua nova senha com, no mínimo, 8 caracteres: ')
                while len(new_password) < 8:
                    print('\033[91mSenha inválida!\033[0m')
                    new_password = input('Informe sua nova senha com, no mínimo, 8 caracteres: ')
        else:
            value = input('Qual será o novo valor? ').lower()
        return key, value

    def get_mime(self):
        mime = MIMEMultipart()
        mime['From'] = main_email
        mime['To'] = self._email
        mime['Subject'] = 'Confirmação de senha'

        with my_context_generator(email_template, 'r') as email:
            text = email.read()
            template = string.Template(text)
            template = template.substitute(addressee=f'{self._name} {self._lastname}',
                                           password=self.__password,
                                           remitter='Equipe MathMat')
            mime_txt = MIMEText(template, _subtype='html', _charset='utf-8')
        mime.attach(mime_txt)
        return mime

    def send_verification_email(self):
        msg_ = self.get_mime()
        with SMTP(host=server_domain, port=server_port, local_hostname=host_name, timeout=15) as server:
            try:
                server.ehlo()
                server.starttls()
                server.login(main_email, main_email_password)
                server.send_message(msg=msg_)
                server.close()
            except Exception as e:
                print(e)
            print('Email enviado!')
            confirmation = input('Confirma o recebimento do email? [S/N]').lower()[0]
            while confirmation not in 'sn':
                print('Resposta inválida!')
                confirmation = input('Confirma o recebimento do email? [S/N]').lower()[0]
            if confirmation == 'n':
                print('Estaremos reenviando o email nos próximos 30 segundos.')
                sleep(10)
                self.send_verification_email()
            return


sign_up = input('Deseja realizar login [1] ou criar uma nova conta [2]? ')
client01 = Client('Matheus', 'Cerqueira', 22, 'matcbv', 'matheuscbv23@gmail.com')
client01.add_new_client()
