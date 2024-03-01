def leiaInt(str):
    while not str.isnumeric():
        str = input('\033[31mERRO! Insira um valor numérico: \033[0m')
    return str


while True:
    num = leiaInt(input('Insira um valor para ser verificado: '))
    print(f'O número digitado foi: {num}')
    cond = input('\nDeseja inserir mais um valor para verificação? [S/N] ').upper()[0]
    while cond not in 'SN':
        print('\nResposta inválida!')
        cond = input('Deseja inserir mais um valor para verificação? [S/N] ').upper()[0]
    if cond == 'N':
        break
