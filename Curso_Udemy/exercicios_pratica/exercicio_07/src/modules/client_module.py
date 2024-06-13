import json
from pathlib import Path
import db_module


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


def get_client_data(account_number):
    client_list = []
    with open(db_module.db_path, 'r+') as database:
        data_obj = json.load(database)
        for client_id, client_data in data_obj.items():
            if client_data['account_number'] == account_number:
                data = {client_id: client_data}
            else:
                client_list.append(data_obj)
            json.dump(client_list, database)
        return data


def get_next_id():
    id_list = []
    with open(db_module.db_path, 'r') as database:
        data_obj = json.load(database)
        for id_ in data_obj.keys():
            id_list.append(id_)
        if id_list:
            return len(id_list) + 1
        return 1
