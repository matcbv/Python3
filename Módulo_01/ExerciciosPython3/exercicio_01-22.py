
nome = input('Digte a seguir o seu nome completo: ')
listaNome = nome.split()
print(f'O nome informado acima em letras maiúsculas é: {nome.upper()}')
print(f'O nome informado acima em letras minúsculas é: {nome.lower()}')
print('O nome informado acima tem', len(''.join(listaNome)), 'caracteres')
print(f'O primeiro nome tem {len(listaNome[0])}')
