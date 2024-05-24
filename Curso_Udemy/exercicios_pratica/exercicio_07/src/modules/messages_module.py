from enum import Enum


class Messages(Enum):
    deposit_success = 'Depósito realizado com sucesso!'
    deposit_failure = 'Depósito negado!'
    withdraw_success = 'Saque realizado com sucesso.'
    withdraw_failure = 'Houve uma falha no depósito. Tente novamente.'
