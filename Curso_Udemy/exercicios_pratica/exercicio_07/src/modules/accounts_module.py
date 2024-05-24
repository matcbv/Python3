from abc import ABC, abstractmethod
from random import SystemRandom
from pathlib import Path
from datetime import datetime
import string
import json
from messages_module import Messages

# LOGS PATH:
logs_path = Path().absolute().parent / "database/transitions_logs.txt"

# DATABASE PATH:
db_path = Path().absolute().parent / "database/clients_data.json"


def check_db():
    with open(db_path, 'r+') as database:
        data = database.read()
        if data == '':
            database.write('{}')


check_db()


def check_cpf(cpf, multiplier=10, i=0):
    counter = 0
    for digit in cpf:
        if not digit.isdecimal():
            return False
        if multiplier > 1:
            counter += int(digit) * multiplier
            multiplier -= 1
    new_digit = get_digit(counter)
    cpf += str(new_digit)
    if i > 0:
        if str(cpf)[-2:] == str(cpf)[-4:-2]:
            return True
        return False
    return check_cpf(cpf, 11, 1)


def get_digit(value):
    if value % 11 > 2:
        return 11 - (value % 11)
    return 0


def check_value(value):
    if not isinstance(value, (int, float)) or value <= 0:
        return False
    return True


def answer_validator(answer):
    if answer not in 'sn':
        print('Resposta inválida!')
        return False
    return True


def get_new_password():
    new_password = ''.join(SystemRandom().choices([string.ascii_letters, string.digits], k=8))
    return new_password


def get_next_id():
    id_list = []
    with open(db_path, 'r') as database:
        data_obj = json.load(database)
        for id_ in data_obj.keys():
            id_list.append(id_)
        if id_list:
            return len(id_list) + 1
        return 1


def add_transaction_log(account_number, action, date):
    with open(logs_path, 'a') as database:
        database.write(f'{account_number} ')


def get_transaction_logs(date):
    with open(logs_path, 'r') as database:
        data_list = database.readlines()
        extract_list = filter(lambda data: data if date in data else None, data_list)
        return extract_list


def get_client_data(account_number):
    with open(db_path, 'r') as database:
        data_obj = json.load(database)
        for client_id, client_data in data_obj.items():
            if client_data['account_number'] == account_number:
                return {client_id: client_data}


class Client:
    def __int__(self, name, lastname, age, cpf, address, salary):
        self.id = get_next_id()
        self.name = name
        self.lastname = lastname
        self.age = age
        self.cpf = cpf
        self.address = address
        self.salary = salary
        self.bank_account = None


class BankAccount(ABC):
    def __init__(self, account_number, agency_number, retired=False, balance=0):
        self.numberAccount = account_number
        self.agencyNumber = agency_number
        self.password = get_new_password()
        self.retired = retired
        self.balance = balance

    def deposit(self, value):
        valid_value = check_value(value)
        if valid_value:
            self.balance += value
            print('Depósito bem sucedido.\n'
                  f'Saldo atual: {self.balance}')
            add_transaction_log()
            return True
        return False

    @abstractmethod
    def withdraw(self, value): ...


class CurrentAccount(BankAccount):
    def __int__(self, account_number, agency_number, retired, balance, overdraft):
        super().__init__(account_number, agency_number, retired, balance)
        self.overdraft = overdraft

    def withdraw(self, value):
        valid_value = check_value(value)
        if valid_value:
            if value > self.balance:
                print('Saldo indisponível para saque.')
                active_overdraft = input('Deseja acionar seu cheque especial? [S/N] ').lower()
                answer_validator(active_overdraft)
                if not active_overdraft:
                    active_overdraft = input('Deseja acionar seu cheque especial? [S/N] ').lower()
                    answer_validator(active_overdraft)
                if active_overdraft == 's':
                    if value > self.balance + self.overdraft:
                        print('Sem limite disponível em seu cheque especial')
                        return False
                    self.overdraft -= value - self.balance
                    self.balance = 0
                    add_transaction_log()
                    return True
            self.balance -= value
            add_transaction_log()
            return True
        return False


class SavingsAccount(BankAccount):
    def withdraw(self, value):
        valid_value = check_value(value)
        if valid_value:
            if value > self.balance:
                print('Saldo indisponível para saque.')
                return False
            self.balance -= value
            print('Saque bem sucedido.\n'
                  f'Saldo atual: {self.balance}')
            add_transaction_log()
            return True
        return False


class CashMachine:
    def __int__(self, account_number, password):
        self.account_number = account_number
        self.password = password
        self.account = get_client_data(account_number)

    @property
    def extract(self):
        with open(logs_path, 'r'):
            return
