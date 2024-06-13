import json
from datetime import datetime
from pathlib import Path

# LOGS PATH:
logs_path = Path().absolute().parent / "database/transitions_logs.txt"

# DATABASE PATH:
db_path = Path().absolute().parent / "database/clients_data.json"


# DATABASE FUNCTIONS:
def check_db():
    with open(db_path, 'r+') as database:
        data = database.read()
        if data == '':
            database.write('{}')


check_db()


def add_transaction_log(account_number, action):
    current_date = datetime.now().strftime('%H:%M:%S - %d/%m/%y')
    with open(logs_path, 'a') as database:
        database.write(f'{action}, {current_date}\nConta: {account_number}')


def get_transaction_logs(date):
    with open(logs_path, 'r') as database:
        data_list = database.readlines()
        extract_list = filter(lambda data: data if date in data else None, data_list)
        return extract_list


def add_client(data):
    with open(db_path, 'r') as db:
        clients = json.load(db)
    for client in clients:
        for client_id, data_client in client.items():
            if data_client['account_number'] == data['account_number']:
                return False
        with open(db_path, 'a') as db:
            db.write(data + '\n')
            return True
