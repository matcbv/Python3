numeros = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

while True:
    num = int(input('\nInforme a seguir, o número entre 0 e 10, que deseja que seja escrito por extenso: '))
    while num < 0 or num > 10:
        num = int(input('Número inválido! Por favor, informe um número entre 0 e 10. '))

    print(f'{num} - {numeros[num - 1]}')
    print(('-' * 15))

    resp = input('Deseja continuar? ').title()
    if resp in 'SimNãoNaoSN':
        if resp in 'NãoNaoN':
            break
    else:
        resp = input('Resposta inválida. Tente novamente: ').title()
