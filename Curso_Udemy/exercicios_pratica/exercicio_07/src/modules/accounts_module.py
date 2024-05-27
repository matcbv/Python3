import client_module
import db_module
from abc import ABC, abstractmethod
from random import SystemRandom
import string


def get_new_password():
    new_password = ''.join(SystemRandom().choices([string.ascii_letters, string.digits], k=8))
    return new_password


def answer_validator(answer):
    if answer not in 'sn':
        print('Resposta inválida!')
        return False
    return True


def check_answer():
    pass


# CPF VALIDATION FUNCTIONS:
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
# ----------------------------


class BankAccount(ABC):
    def __init__(self, account_number, agency_number, retired=False, balance=0):
        self.account_number = account_number
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
            db_module.add_transaction_log(self.account_number, f'Depósito de {self.balance}')
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
                    db_module.add_transaction_log(self.account_number, f'Saque de {self.balance}')
                    return True
            self.balance -= value
            db_module.add_transaction_log(self.account_number, f'Saque de {self.balance}')
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
            db_module.add_transaction_log(self.account_number, f'Saque de {self.balance}')
            return True
        return False


class CashMachine:
    def __int__(self, account_number, password):
        self.account_number = account_number
        self.password = password
        self.account = client_module.get_client_data(account_number)

    @property
    def extract(self):
        client_extract = db_module.get_transaction_logs(self.account_number)
        return client_extract

    def banking(self):
        operation = input('Qual operação bancária deseja realizar?\n'
                          'Saque [1] ou Depósito [2]')
        while operation not in '12':
            operation = input('Qual operação bancária deseja realizar?\n'
                              'Saque [1] ou Depósito [2]')