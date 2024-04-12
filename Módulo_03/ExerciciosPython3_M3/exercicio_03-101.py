from datetime import date


def voto(an):
    idade = anoAtual - an
    if idade >= 70:
        print(f'Com {idade} anos, o voto desse cidadão é opcional.')
    elif 18 <= idade < 70:
        print(f'Com {idade} anos, o voto desse cidadão é obrigatório.')
    else:
        print(f'Com {idade} anos, o cidadão ainda não pode votar devido a idade insuficiente.')


# Programa principal
anoAtual = date.today().year
anoNasc = int(input('Informe o ano de nascimento do cidadão: '))
while not 1900 <= anoNasc <= anoAtual:
    print('Data inválida!')
    anoNasc = int(input('Informe o ano de nascimento do cidadão: '))
voto(anoNasc)
