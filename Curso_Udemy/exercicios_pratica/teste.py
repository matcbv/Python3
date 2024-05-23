obj = {
    '1': {
        'Nome': 'Matheus',
        'Sobrenome': 'Cerqueira'
    },
    '2': {
        'Nome': 'Matheus',
        'Sobrenome': 'Cerqueira'
    },
    '3': {
        'Nome': 'Matheus',
        'Sobrenome': 'Cerqueira'
    }
}

num_list = [1, 2, 3, 4, 5, 6, 7, 8]

client_data = filter(lambda num: num if num % 2 == 0 else None, num_list)
for n in client_data:
    print(n, len(client_data))

for data in obj:
    print(data)

# obj02 = filter(lambda data: data)
