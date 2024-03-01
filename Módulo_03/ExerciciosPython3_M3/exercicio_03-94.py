pessoas = []
cont = 0
numPessoas = somaIdade = 0

while True:
    dadosPessoa = {'Nome': input(f'\nInforme o nome da pessoa Nº{cont + 1}: ').title(),
                   'Sexo': input('Informe o sexo da pessoa [M/F]: ').upper()[0],
                   'Idade': int(input('Informe a idade da pessoa: '))}
    while dadosPessoa['Sexo'] not in 'MF':
        print('Sexo inválido.')
        dadosPessoa['Sexo'] = input('Informe o sexo da pessoa [M/F]: ').upper()
    while dadosPessoa['Idade'] > 130 or dadosPessoa['Idade'] < 0:
        print('Idade inválida.')
        dadosPessoa['Idade'] = int(input('Informe a idade da pessoa: '))
    pessoas.append(dadosPessoa.copy())
    numPessoas += 1
    somaIdade += dadosPessoa['Idade']
    cont += 1
    cond = input('\nDeseja cadastrar mais alguém? [S/N]').upper()
    while cond not in 'SN':
        print('Resposta inválida.')
        cond = input('\nDeseja cadastrar mais alguém? [S/N]').upper()
    if cond == 'N':
        cont = 0
        break
print(f'O número de pessoas cadastrados foi: {numPessoas}')
print(f'A média de idade das pessoas cadastradas foi: {somaIdade / numPessoas:.2f}')
print('As mulheres cadastradas nessa lista foram:')
for c in pessoas:
    if c['Sexo'] == 'F':
        print(f'{cont+1}ª- {c["Nome"]}')
print('As pessoas acima da média de idade cadastradas nessa lista foram: ')
for c in pessoas:
    if c['Idade'] > somaIdade / numPessoas:
        print(f'1ª - {c["Nome"]}')
print('\nPrograma encerrado...')
