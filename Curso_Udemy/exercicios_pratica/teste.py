teste = {'1': {'nome': 'lucas', 'sobrenome': 'silva'}, '2': {'nome': 'daniel', 'sobrenome': 'souza'}}

for pessoa in teste.items():
    print(pessoa[1]['nome'])
