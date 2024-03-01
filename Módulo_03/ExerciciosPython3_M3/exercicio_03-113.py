def verif(sn):
    while sn not in 'SN':
        print('\nResposta inválida!')
        sn = input('Deseja inserir mais um valor para verificação? [S/N] ').upper()[0]
        return sn


def leiaInt(conv):
    while True:
        try:
            num = int(conv)
        except (ValueError, TypeError):
            conv = input('\033[31mERRO! Insira um valor numérico inteiro: \033[0m')
            continue
        except KeyboardInterrupt:
            print('Programa interrompido pelo usuário.')
            break
        return num


def leiaFloat(conv):
    while True:
        try:
            num = float(conv.replace(',', '.'))
        except (ValueError, TypeError):
            conv = input('\033[31mERRO! Insira um valor numérico real: \033[0m')
            continue
        except KeyboardInterrupt:
            print('Programa interrompido pelo usuário.')
            break
        return num


while True:
    val = leiaInt(input('\nInsira um valor inteiro para ser verificado: '))
    valF = leiaFloat(input('Insira um valor real para ser verificado: '))
    print(f'\nOs números informados foram:'
          f'\nInteiro - {val}'
          f'\nReal - {valF:.2f}')
    cont = input('\nDeseja inserir mais um valor para verificação? [S/N] ').upper()[0]
    verif(cont)
    if cont == 'N':
        break
