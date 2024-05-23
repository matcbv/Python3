from abc import ABC, abstractmethod
from random import SystemRandom
import string
from pathlib import Path
import email_module

# LOGS PATH:
logs_path = 'transitions_log.txt'


def check_cpf(cpf, multiplier=10, i=0):
    counter = 0
    for d in cpf:
        if not d.isdecimal():
            return False
        if multiplier > 1:
            counter += int(d) * multiplier
            multiplier -= 1
    digit = get_digit(counter)
    cpf += str(digit)
    if i > 0:
        if str(cpf)[-2:] == str(cpf)[-4:-2]:
            return True
        return False
    return check_cpf(cpf, 11, 1)


def get_digit(value):
    if value % 11 > 2:
        return 11 - (value % 11)
    return 0


def answer_validator(answer):
    if answer not in 'sn':
        print('Resposta inválida!')
        return False
    return True


def get_new_password():
    new_password = ''.join(SystemRandom().choices([string.ascii_letters, string.digits], k=8))
    return new_password


def transitions_logs():
    pass


class Client:
    def __int__(self, name, lastname, age, cpf, address, salary):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.cpf = cpf
        self.address = address
        self.salary = salary
        self.bank_account = None


class BankAccount(ABC):
    def __init__(self, number_account, agency_number, retired=False, balance=0):
        self.numberAccount = number_account
        self.agencyNumber = agency_number
        self.password = get_new_password()
        self.retired = retired
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        print('Depósito bem sucedido.\n'
              f'Saldo atual: {self.balance}')
        return True

    @abstractmethod
    def withdraw(self, value): ...


class CurrentAccount(BankAccount):
    def __int__(self, number_account, agency_number, retired, balance, overdraft):
        super().__init__(number_account, agency_number, retired, balance)
        self.overdraft = overdraft

    def withdraw(self, value):
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


class SavingsAccount(BankAccount):
    def withdraw(self, value):
        if value > self.balance:
            print('Saldo indisponível para saque.')
            return False
        self.balance -= value
        print('Saque bem sucedido.\n'
              f'Saldo atual: {self.balance}')
        return True


class CashMachine:
    def __int__(self, account):
        self.account = account

    @property
    def extract(self):
        return
