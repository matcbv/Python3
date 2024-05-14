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

# DATABASE PATH
db_path = Path().absolute() / 'clients_data.json'

# EMAIL TEMPLATE PATH
email_template = Path().absolute() / 'email_template.html'

# ENVIRONMENT VARIABLES
main_email_password = os.getenv('EMAIL_PASSWORD')
main_email = os.getenv('EMAIL')
host_name = 'localhost'

# EMAIL SERVER DATA
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


def options_template():
    option = input('\nEscolha uma das opções abaixo:\n'
                   '1 - Editar dados da conta\n'
                   '2 - Excluir conta\n'
                   '3 - Sair\n'
                   '\nResposta: ')
    return option


def password_template():
    password = input('\nInforme uma senha com:\n'
                     '- Ao menos oito caracteres\n'
                     '- Ao menos um número decimal\n'
                     '- Ao menos uma letra\n'
                     '\nSenha: ')
    return password


def get_next_id():
    with my_context_generator(db_path, 'r') as db:
        data = json.load(db)
        return str(len(data)+1)


def get_client_id(data, username):
    for client in data.items():
        if client[1]['username'] == username:
            return client[0]
    return False


def import_data():
    with my_context_generator(db_path, 'r') as db:
        data = json.load(db)
    return data


def get_random_code():
    password = ''.join(random.SystemRandom().choices(''.join([string.digits, string.ascii_letters]), k=8))
    return password


def verify_password(password):
    has_digit = False
    has_alpha = False
    if len(password) < 8:
        return False
    for digit in password:
        if digit.isdigit():
            has_digit = True
        if digit.isalpha():
            has_alpha = True
        if has_digit and has_alpha:
            return True
    return False


def check_username(data, received_username):
    username_array = []
    for client in data.values():
        username_array.append(client['username'])
    if received_username in username_array:
        return True
    return False


def check_password(data, received_username, received_password):
    client_array = []
    for client in data.values():
        client_array.append([client['username'], client['password']])
    for client in client_array:
        if client[0] == received_username and client[1] == received_password:
            return True
    return False


class Client:
    def __init__(self, name, lastname, age, email, username, password):
        self._id = get_next_id()
        self._name = name
        self._lastname = lastname
        self._age = age
        self._email = email
        self._username = username
        self.__password = password
        self.add_new_client()

    client_keys = ['name', 'lastname', 'age', 'username', 'password', 'email']
    __verification_code = None

    def add_new_client(self):
        if Path.exists(db_path):
            data = import_data()
            checked_username = check_username(data, self._username)
            if checked_username:
                print('\n\033[92mCliente já cadastrado!\033[0m')
                return False
            client_data = {
                'name': self._name,
                'lastname': self._lastname,
                'age': self._age,
                'email': self._email,
                'username': self._username,
                'password': self.__password
            }
            data[self._id] = client_data
            with my_context_generator(db_path, 'w') as db:
                json.dump(data, db, indent=True, ensure_ascii=False)
        else:
            print('\033[91mUm erro inesperado ocorreu!\033[0m\n'
                  '\033[92mPossível solução\033[0m: Verifique o caminho para o banco de dados.')

    @staticmethod
    def get_client_data(client_id):
        data = import_data()
        return data[client_id]

    @classmethod
    def set_client_data(cls, data, client_id, key):
        if key == 'age':
            value = int(input('Qual será o novo valor? '))
        elif key == 'password':
            cls.send_verification_email()
            code = input('Informe o código obtido através do email: ')
            if code == Client.__verification_code:
                new_password = password_template()
                while not verify_password(new_password):
                    new_password = password_template()
                    verify_password(new_password)
        else:
            value = input('Qual será o novo valor? ').strip().title()

    def get_mime(self):
        mime = MIMEMultipart()
        mime['From'] = main_email
        mime['To'] = self._email
        mime['Subject'] = 'Confirmação de senha'

        with my_context_generator(email_template, 'r') as email:
            text = email.read()
            template = string.Template(text)
            Client.__verification_code = get_random_code()
            template = template.substitute(addressee=f'{self._name} {self._lastname}',
                                           password=Client.__verification_code,
                                           remitter='Equipe Etc')
            mime_txt = MIMEText(template, _subtype='html', _charset='utf-8')
        mime.attach(mime_txt)
        return mime

    @classmethod
    def send_verification_email(cls, mime):
        msg_ = mime
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
            confirmation = input('Confirma o recebimento do email? [S/N] ').lower()[0]
            while confirmation not in 'sn':
                print('\n\033[91mResposta inválida!\033[0m\n')
                confirmation = input('Confirma o recebimento do email? [S/N] ').lower()[0]
            if confirmation == 'n':
                print('Estaremos reenviando o email nos próximos 30 segundos.')
                sleep(10)
                cls.send_verification_email(msg_)
            return


while True:
    try:
        sign_up = int(input('Deseja realizar login [1] ou criar uma nova conta [2]? '))
    except ValueError:
        print('\n\033[91mOpção inválida!\033[0m\n')
    else:
        if sign_up == 1 or sign_up == 2:
            break
        print('\033[91mOpção inválida!\033[0m\n')

client_ = None

if sign_up == 1:
    login_username = input('\nNome de usuário: ')
    login_password = input('Senha: ')
    data_ = import_data()
    checked_username_ = check_username(data_, login_username)
    checked_password_ = check_password(data_, login_username, login_password)
    if checked_username_ and checked_password_:
        print(f'\n\033[92mSeja bem-vindo, {login_username}!\033[0m')
        chosen_option = options_template()
        while chosen_option not in '123':
            print('\n\033[Opção inválida!\033[0m\n')
            chosen_option = options_template()
        chosen_option = int(chosen_option)
        match chosen_option:
            case 1:
                chosen_key = input('\nEscolha uma das chaves abaixo para ser alterada:')
                if chosen_key not in Client.client_keys:
                    print(print('\n\033[Opção inválida!\033[0m\n'))
                client_id_ = get_client_id(data_, login_username)
                Client.set_client_data(data_, client_id_, chosen_key)
            case 2:
                pass
            case 3:
                pass
    else:
        print('\n\033[91mCredenciais inválidas!\033[0m\n')
else:
    name_ = input('\nInforme seu primeiro nome: ').strip().title()
    lastname_ = input('Informe seu sobrenome: ').strip().title()
    age_ = input('Informe sua idade: ').strip()
    email_ = input('Informe seu endereço de email: ').strip()
    username_ = input('Escolha um nome de usuário: ').strip()
    password_ = password_template()
    while not verify_password(password_):
        print('\033[91mSenha inválida!\033[0m\n')
        password_ = password_template()
        verify_password(password_)
    if name_ and lastname_ and age_.isdigit() and email_ and username_ and password_:
        client_ = Client(name_, lastname_, int(age_), email_, username_, password_)
        print('\n\033[92mCliente cadastrado com sucesso!\033[0m')
    else:
        print('\n\033[91mDados inválidos! Tente novamente.\033[0m')
