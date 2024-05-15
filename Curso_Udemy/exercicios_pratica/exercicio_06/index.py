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
        if file:
            file.close()


def check_db():
    with my_context_generator(db_path, 'r+') as init_database:
        content = init_database.read()
        if not content:
            init_database.write('{}')


check_db()


def options_template():
    option = input('\nEscolha uma das opções abaixo:\n'
                   '1 - Ver dados da conta\n'
                   '2 - Editar dados da conta\n'
                   '3 - Excluir conta\n'
                   '4 - Sair\n'
                   '\nResposta: ')
    return option


def password_template():
    password = input('\nInforme uma senha com:\n'
                     '- Ao menos oito caracteres\n'
                     '- Ao menos um número decimal\n'
                     '- Ao menos uma letra\n'
                     '\nSenha: ')
    return password


def key_template():
    print('Digite uma das chaves abaixo para ser alterada:')
    for i in range(0, 6):
        print(f'\033[93m{Client.client_keys[i]}', end=', ') if i < 5 else print(f'{Client.client_keys[i]}', end='.\n')
    chosen_key = input('\n\033[0mChave: ')
    return chosen_key


def get_next_id():
    with my_context_generator(db_path, 'r') as db:
        data = json.load(db)
        return str(len(data)+1)


def get_client_data(data, username):
    for value_ in data.values():
        if value_['username'] == username:
            return value_
    return False


def get_client_id(data, username):
    for key_, value_ in data.items():
        if value_['username'] == username:
            return key_


def import_data():
    with my_context_generator(db_path, 'r') as db:
        data = json.load(db)
    return data


def get_random_code():
    password = ''.join(random.SystemRandom().choices(''.join([string.digits, string.ascii_letters]), k=8))
    return password


def password_validator(password):
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


# CLASS TO CREATE EMAILS
class Email:
    def __init__(self, email, name, lastname):
        self.email = email
        self.name = name
        self.lastname = lastname

    verification_code = None

    def get_mime(self):
        mime = MIMEMultipart()
        mime['From'] = main_email
        mime['To'] = self.email
        mime['Subject'] = 'Confirmação de senha'

        with my_context_generator(email_template, 'r') as email:
            text = email.read()
            template = string.Template(text)
            Email.verification_code = get_random_code()
            template = template.substitute(addressee=f'{self.name} {self.lastname}',
                                           password=Email.verification_code,
                                           remitter='Equipe Etc')
            mime_txt = MIMEText(template, _subtype='html', _charset='utf-8')
        mime.attach(mime_txt)
        return mime

    def send_verification_email(self, mime):
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
            print('\nEmail enviado!')
            confirmation = input('Confirma o recebimento do email? [S/N] ').lower()[0]
            while confirmation not in 'sn':
                print('\n\033[91mResposta inválida!\033[0m\n')
                confirmation = input('Confirma o recebimento do email? [S/N] ').lower()[0]
            if confirmation == 'n':
                print('Estaremos reenviando o email nos próximos 30 segundos.')
                sleep(10)
                self.send_verification_email(msg_)
            return


# CLASS TO CREATE CLIENTS
class Client:
    def __init__(self, name, lastname, age, email, username, password):
        self._id = get_next_id()
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = Email(email, name, lastname)
        self.username = username
        self._password = password
        self.add_new_client()

    client_keys = ['name', 'lastname', 'age', 'username', 'password', 'email']

    def add_new_client(self):
        if Path.exists(db_path):
            data = import_data()
            checked_username = check_username(data, self.username)
            if checked_username:
                print('\n\033[92mCliente já cadastrado!\033[0m')
                return False
            client_data = {
                'name': self.name,
                'lastname': self.lastname,
                'age': self.age,
                'email': self.email.email,
                'username': self.username,
                'password': self._password
            }
            data[self._id] = client_data
            with my_context_generator(db_path, 'w') as db:
                json.dump(data, db, indent=True, ensure_ascii=False)
        else:
            print('\033[91mUm erro inesperado ocorreu!\033[0m\n'
                  '\033[92mPossível solução\033[0m: Verifique o caminho para o banco de dados.')

    @classmethod
    def set_client_data(cls, db_data, data_client_, key_):
        email = Email(data_client_['email'], data_client_['name'], data_client_['lastname'])
        value_ = None
        if key_ == 'age':
            value_ = int(input('Qual será o novo valor? '))
        elif key_ == 'password':
            mime = email.get_mime()
            email.send_verification_email(mime)
            code = input('Informe o código obtido através do email: ').strip()
            if code == email.verification_code:
                value_ = password_template()
                while not password_validator(value_):
                    value_ = password_template()
                    password_validator(value_)
        elif key_ == 'name' or key_ == 'lastname':
            value_ = input('Qual será o novo valor? ').strip().title()
        else:
            value_ = input('Qual será o novo valor? ').strip()
        if value_:
            data_client_[key_] = value_
            client_id_ = get_client_id(db_data, data_client_['username'])
            db_data[client_id_] = data_client_
            with my_context_generator(db_path, 'w') as database_:
                json.dump(db_data, database_, indent=True, ensure_ascii=False)
            return True
        else:
            print('\033[91mNovo valor inválido! Tente novamente.\033[0m')
            return False


while True:
    try:
        sign_up = int(input('Deseja realizar login \033[93m[1]\033[0m ou criar uma nova conta \033[93m[2]\033[0m? '))
    except ValueError:
        print('\n\033[91mOpção inválida!\033[0m\n')
    else:
        if sign_up == 1 or sign_up == 2:
            break
        print('\033[91mOpção inválida!\033[0m\n')


if sign_up == 1:
    login_username = input('\nNome de usuário: ')
    login_password = input('Senha: ')
    db_data_ = import_data()
    checked_username_ = check_username(db_data_, login_username)
    checked_password_ = check_password(db_data_, login_username, login_password)
    if checked_username_ and checked_password_:
        print(f'\n\033[92mSeja bem-vindo, {login_username}!\033[0m')
        chosen_option = options_template()
        while chosen_option not in '123':
            print('\n\033[91mOpção inválida!\033[0m\n')
            chosen_option = options_template()
        print()
        chosen_option = int(chosen_option)
        match chosen_option:
            case 1:
                client_id = get_client_id(db_data_, login_username)
                data_client = get_client_data(db_data_, login_username)
                for key, value in data_client.items():
                    print(f'{key}: {value}')
                print()
            case 2:
                chosen_key = key_template()
                while chosen_key not in Client.client_keys:
                    print(print('\n\033[91mOpção inválida!\033[0m\n'))
                    chosen_key = key_template()
                data_client = get_client_data(db_data_, login_username)
                Client.set_client_data(db_data_, data_client, chosen_key)
            case 3:
                client_id = get_client_id(db_data_, login_username)
                del db_data_[client_id]
                with my_context_generator(db_path, 'w') as database:
                    json.dump(db_data_, database, indent=True, ensure_ascii=False)
            case 4:
                print('Programa encerrado!')
    else:
        print('\n\033[91mCredenciais inválidas!\033[0m\n')
else:
    name_ = input('\nInforme seu primeiro nome: ').strip().title()
    lastname_ = input('Informe seu sobrenome: ').strip().title()
    age_ = input('Informe sua idade: ').strip()
    email_ = input('Informe seu endereço de email: ').strip()
    username_ = input('Escolha um nome de usuário: ').strip()
    password_ = password_template()
    while not password_validator(password_):
        print('\033[91mSenha inválida!\033[0m\n')
        password_ = password_template()
        password_validator(password_)
    if name_ and lastname_ and age_.isdigit() and email_ and username_ and password_:
        client_ = Client(name_, lastname_, int(age_), email_, username_, password_)
        print('\n\033[92mCliente cadastrado com sucesso!\033[0m')
    else:
        print('\n\033[91mDados inválidos! Tente novamente.\033[0m')
