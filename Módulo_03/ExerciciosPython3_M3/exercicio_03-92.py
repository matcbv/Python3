from datetime import date
dadosFuncionarios = {'NOME': [], 'SEXO': [], 'ANO DE NASCIMENTO': [], 'IDADE': [], 'CTPS': [], 'ANO DE ADMISSAO': [], 'SALARIO': [], 'IDADE DE APOSENTADORIA': []}
cod = editar = ctps = 0
anoAtual = date.today().year

while True:
    print(f'\n{cod+1}º funcionário(a):')
    dadosFuncionarios['NOME'].append(input(f'Informe o nome completo do(a) funcionário(a): ').title())
    while len(dadosFuncionarios['NOME'][cod].split()) < 2:
        del dadosFuncionarios['NOME'][cod]
        print('Nome incompleto.')
        dadosFuncionarios['NOME'].append(input(f'Informe o nome completo do(a) funcionário(a): ').title())
    dadosFuncionarios['SEXO'].append(input('Informe o sexo do(a) funcionário(a) [M/F]: ').upper())
    while dadosFuncionarios['SEXO'][cod] not in 'MF':
        del dadosFuncionarios['SEXO'][cod]
        print('Sexo inválido.')
        dadosFuncionarios['SEXO'].append(input('Informe o sexo do(a) funcionário(a) [M/F]: ').upper())
    dadosFuncionarios['ANO DE NASCIMENTO'].append(int(input(f'Informe o ano de nascimento do(a) funcionário(a): ')))
    while dadosFuncionarios['ANO DE NASCIMENTO'][cod] < 1900 or dadosFuncionarios['ANO DE NASCIMENTO'][cod] > anoAtual - 14:
        del dadosFuncionarios['ANO DE NASCIMENTO'][cod]
        print('Data inválida.')
        dadosFuncionarios['ANO DE NASCIMENTO'].append(int(input(f'Informe o ano de nascimento do(a) funcionário(a): ')))
    ctps = input('Informe o número de CTPS do(a) funcionário(a): ')
    for c in dadosFuncionarios['CTPS']:
        while c == ctps:
            print('CTPS já existente no banco de dados.')
            ctps = input('Informe o número de CTPS do(a) funcionário(a): ')
    dadosFuncionarios['CTPS'].append(ctps)
    if dadosFuncionarios['CTPS'][cod] != '0':
        while len(dadosFuncionarios['CTPS'][cod]) != 7:
            del dadosFuncionarios['CTPS'][cod]
            print('Número de CTPS inválido.')
            dadosFuncionarios['CTPS'].append(input('Informe o número de CTPS do(a) funcionário(a): '))
        dadosFuncionarios['ANO DE ADMISSAO'].append(int(input('Informe o ano de admissão do(a) funcionário(a): ')))
        while dadosFuncionarios['ANO DE ADMISSAO'][cod] > anoAtual or dadosFuncionarios['ANO DE ADMISSAO'][cod] < dadosFuncionarios['ANO DE NASCIMENTO'][cod] + 14:
            del dadosFuncionarios['ANO DE ADMISSAO'][cod]
            print('Data inválida.')
            dadosFuncionarios['ANO DE ADMISSAO'].append(int(input('Informe o ano de admissão do(a) funcionário(a): ')))
        dadosFuncionarios['SALARIO'].append(float(input('Informe o salário do(a) funcionário(a): R$')))
        while dadosFuncionarios['SALARIO'][cod] < 0:
            del dadosFuncionarios['SALARIO'][cod]
            print('Salário inválido.')
            dadosFuncionarios['SALARIO'].append(float(input('Informe o salário do(a) funcionário(a): R$')))
    else:
        dadosFuncionarios['ANO DE ADMISSAO'].append(0)
        dadosFuncionarios['SALARIO'].append(0)
    dadosFuncionarios['IDADE'].append(int(anoAtual - dadosFuncionarios['ANO DE NASCIMENTO'][cod]))
    if dadosFuncionarios['CTPS'][cod] == '0':
        cauculoAposentadoria = '?'
    else:
        if dadosFuncionarios['SEXO'][cod] == 'M':
            cauculoAposentadoria = int(dadosFuncionarios['IDADE'][cod] + (35 - (anoAtual - dadosFuncionarios['ANO DE ADMISSAO'][cod])))
        else:
            cauculoAposentadoria = int(dadosFuncionarios['IDADE'][cod] + (30 - (anoAtual - dadosFuncionarios['ANO DE ADMISSAO'][cod])))
    dadosFuncionarios['IDADE DE APOSENTADORIA'].append(cauculoAposentadoria)
    print('-'*50)
    cod += 1
    continuar = input('Deseja adicionar mais um(a) funcionário(a)? [S/N]').upper()
    while continuar not in 'SN':
        print('Resposta inválida:')
        continuar = input('Deseja adicionar mais um(a) funcionário(a)? [S/N]').upper()
    if continuar == 'N':
        break
exibir = input('Deseja ver/editar os dados de algum(a) funcionário(a)? [S/N]').upper()
while exibir not in 'SN':
    print('Resposta inválida.')
    exibir = input('Deseja ver/editar os dados de algum(a) funcionário(a)? [S/N]').upper()
while exibir == 'S':
    pos = 0
    verif = int(input('Deseja identificar o(a) funcionário(a) pelo número da CTPS [1] ou pelo nome [2]? '))
    while verif != 1 and verif != 2:
        print('Opção inválida.')
        verif = int(input('Deseja identificar o(a) funcionário(a) pelo número da CTPS [1] ou pelo nome [2]? '))
    if verif == 1:
        ctpsVerif = input('Informe o número da CTPS do(a) funcionário(a): ')
        if ctpsVerif == '0':
            print('-'*50)
            print('Funcionários sem CTPS devem ser identificados pelo nome.')
            editar = 'N'
        else:
            while len(ctpsVerif) != 7:
                print('Número de CTPS inválido.')
                ctpsVerif = input('Informe o número de CTPS do(a) funcionário(a) a ser exibido(a)/editado(a): ')
            print('-' * 50)
            while pos < len(dadosFuncionarios['CTPS']):
                if ctpsVerif == dadosFuncionarios['CTPS'][pos]:
                    for k, v in dadosFuncionarios.items():
                        if k == 'SALARIO':
                            print(f'{k}: R${v[pos]:.2f}')
                        else:
                            print(f'{k}: {v[pos]}')
                    editar = input('\nDeseja editar algum dos dados desse(a) funcionário(a)? [S/N] ').upper()
                    break
                if pos == len(dadosFuncionarios['CTPS']) - 1:
                    print('Nenhum(a) funcionário(a) com esse número de CTPS foi identicado(a) nos banco de dados.')
                    editar = 'N'
                pos += 1
    else:
        nomeVerif = input('Informe o nome do(a) funcionário(a) a ser exibido(a)/editado(a): ').title()
        while len(nomeVerif.split()) < 2:
            print('Nome inválido.')
            nomeVerif = input('Informe o nome do(a) funcionário(a) a ser exibido(a)/editado(a): ').title()
        print('-' * 50)
        while pos < len(dadosFuncionarios['NOME']):
            if nomeVerif == dadosFuncionarios['NOME'][pos]:
                for k, v in dadosFuncionarios.items():
                    if k == 'SALARIO':
                        print(f'{k}: R${v[pos]:.2f}')
                    else:
                        print(f'{k}: {v[pos]}')
                editar = input('\nDeseja editar algum dos dados desse(a) funcionário(a)? [S/N] ').upper()
                break
            if pos == len(dadosFuncionarios['NOME']) - 1:
                print('Nenhum(a) funcionário(a) com esse nome foi identicado no banco de dados.')
                editar = 'N'
            pos += 1
    print('-' * 50)
    while editar not in 'SN':
        print('Resposta inválida.')
        editar = input('Deseja editar algum dos dados desse(a) funcionário(a)? [S/N] ').upper()
    while editar == 'S':
        chaveEdicao = input('Informe com as mesma palavras da lista acima, o campo a ser editado: ').upper()
        if chaveEdicao == 'IDADE' or chaveEdicao == 'IDADE APOSENTADORIA':
            print('Não é possível alterar os dados dos campos IDADE e IDADE DE APOSENTADORIA pois são cauculados automaticamente.')
            editar = input('Deseja editar mais algum dos dados desse(a) funcionário(a)? [S/N] ').upper()
            while editar not in 'SN':
                print('Resposta inválida.')
                editar = input('Deseja editar algum dos dados desse(a) funcionário(a)? [S/N] ').upper()
            if editar == 'N':
                break
        else:
            for k, v in dadosFuncionarios.items():
                if k == chaveEdicao:
                    if chaveEdicao == 'ANO DE NASCIMENTO' or chaveEdicao == 'ANO DE ADMISSAO':
                        v[pos] = int(input('Informe o dado atualizado do(a) funcionário(a): '))
                    elif chaveEdicao == 'SALARIO':
                        v[pos] = float(input('Informe o dado atualizado do(a) funcionário(a): '))
                    else:
                        v[pos] = input('Informe o dado atualizado do(a) funcionário(a): ').title()
            print('-'*50)
            print(f'Dados do(a) funcionário(a) {dadosFuncionarios["NOME"][pos]} atualizados:\n')
            for k, v in dadosFuncionarios.items():
                if k == 'SALARIO':
                    print(f'{k}: R${v[pos]:.2f}')
                else:
                    print(f'{k}: {v[pos]}')
            print('-'*50)
            editar = input('Deseja editar mais algum dos dados desse(a) funcionário(a)? [S/N] ').upper()
            while editar not in 'SN':
                print('Resposta inválida.')
                editar = input('Deseja editar algum dos dados desse(a) funcionário(a)? [S/N] ').upper()
            if editar == 'N':
                break
    exibir = input('Deseja ver/editar os dados de mais algum(a) funcionário(a)? [S/N]').upper()
    while exibir not in 'SN':
        print('Resposta inválida.')
        exibir = input('Deseja ver/editar os dados de mais algum(a) funcionário(a)? [S/N]').upper()
